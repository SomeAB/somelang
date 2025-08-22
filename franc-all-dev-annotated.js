/**
 * FRANC-ALL Language Detection Library - Development Version
 * 
 * This is an extensively commented, development-friendly version of the franc-all
 * language detection library, reconstructed from the original source code.
 * 
 * Key Features:
 * - Detects 419 languages using trigram analysis
 * - Uses statistical analysis of character patterns
 * - Supports script detection for multi-script texts
 * - Enterprise-grade performance and accuracy
 * 
 * Algorithm Overview:
 * 1. Input validation and normalization
 * 2. Script detection (Latin, Arabic, Cyrillic, etc.)
 * 3. Trigram extraction from input text
 * 4. Statistical comparison with language models
 * 5. Distance calculation and ranking
 * 
 * Original source: https://github.com/wooorm/franc
 * License: MIT
 */

/**
 * TypeScript type definitions for better development experience
 * 
 * @typedef {import('trigram-utils').TrigramTuple} TrigramTuple
 * A tuple containing [trigram_string, frequency_count]
 *
 * @typedef Options
 * Configuration object for language detection
 * @property {Array<string>} [only] - Languages to allow (ISO 639-3 codes)
 * @property {Array<string>} [ignore] - Languages to ignore (ISO 639-3 codes)
 * @property {number} [minLength=10] - Minimum text length to process
 */

/* ===================================================================
 * DEPENDENCIES AND IMPORTS
 * =================================================================== */

/**
 * Import trigram utility functions
 * Trigrams are 3-character sequences used for statistical analysis
 */
import { asTuples } from 'trigram-utils'

/**
 * Import regular expressions for script detection
 * These patterns identify different writing systems (Latin, Arabic, etc.)
 */
import { expressions } from './expressions.js'

/**
 * Import compressed language model data
 * Contains trigram frequency data for 419 languages
 * This is where most of the file size comes from (~750KB of compressed data)
 */
import { data } from './data.js'

/* ===================================================================
 * ALGORITHM CONSTANTS
 * =================================================================== */

/**
 * Maximum length of text to analyze
 * Longer texts are truncated to improve performance
 * 2KB is sufficient for accurate language detection
 */
const MAX_LENGTH = 2048

/**
 * Minimum text length required for analysis
 * Shorter texts don't have enough statistical patterns
 * Can be overridden via options.minLength
 */
const MIN_LENGTH = 10

/**
 * Maximum penalty score for missing trigrams
 * When a trigram doesn't exist in a language model,
 * this value is added to the distance calculation
 */
const MAX_DIFFERENCE = 300

/**
 * Object.prototype.hasOwnProperty shorthand
 * Used throughout for safe property checking
 */
const own = {}.hasOwnProperty

/* ===================================================================
 * DATA PREPROCESSING AND OPTIMIZATION
 * =================================================================== */

/**
 * Preprocessed trigram data structure
 * Converts string-based data to numeric lookup tables for performance
 * 
 * Structure: {
 *   script_name: {
 *     language_code: {
 *       trigram: frequency_rank
 *     }
 *   }
 * }
 */
const numericData = {}

/**
 * Convert compressed trigram data to optimized lookup structures
 * 
 * The original data comes as pipe-separated strings like:
 * "the|and|ing|ion|..." (most frequent trigrams first)
 * 
 * We convert this to numeric rankings for faster comparison:
 * { "the": 0, "and": 1, "ing": 2, "ion": 3, ... }
 */
console.log('🔄 Preprocessing language models...')

let script
for (script in data) {
  if (own.call(data, script)) {
    const languages = data[script]
    let name

    // Initialize script container
    numericData[script] = {}

    // Process each language in this script
    for (name in languages) {
      if (own.call(languages, name)) {
        // Split pipe-separated trigram string into array
        const model = languages[name].split('|')
        const trigrams = {}
        let weight = model.length

        // Convert to frequency rankings (lower number = more frequent)
        while (weight--) {
          trigrams[model[weight]] = weight
        }

        numericData[script][name] = trigrams
      }
    }
  }
}

console.log('✅ Language models ready')

/* ===================================================================
 * PUBLIC API FUNCTIONS
 * =================================================================== */

/**
 * Get the most probable language for the given text
 * 
 * This is the main convenience function that returns just the
 * top language code (e.g., 'eng', 'spa', 'fra')
 *
 * @param {string} [value] - The text to analyze
 * @param {Options} [options] - Configuration options
 * @return {string} - ISO 639-3 language code or 'und' for undetermined
 * 
 * @example
 * franc('Hello world') // 'eng'
 * franc('Bonjour le monde') // 'fra'
 * franc('Hola mundo') // 'spa'
 */
export function franc(value, options) {
  // Simply return the top result from the full analysis
  return francAll(value, options)[0][0]
}

/**
 * Get a ranked list of probable languages for the given text
 * 
 * This is the core analysis function that returns all language
 * candidates with their confidence scores
 *
 * @param {string} [value] - The text to analyze
 * @param {Options} [options] - Configuration options
 * @return {Array<TrigramTuple>} - Array of [language_code, confidence] pairs
 * 
 * @example
 * francAll('Hello world')
 * // [['eng', 0.92], ['sco', 0.89], ['frr', 0.84], ...]
 */
export function francAll(value, options = {}) {
  // ========================================
  // STEP 1: Parse and validate options
  // ========================================
  
  /**
   * Language filtering: only allow these languages
   * Supports legacy 'whitelist' option for backwards compatibility
   */
  const only = [...(options.whitelist || []), ...(options.only || [])]
  
  /**
   * Language filtering: ignore these languages
   * Supports legacy 'blacklist' option for backwards compatibility
   */
  const ignore = [...(options.blacklist || []), ...(options.ignore || [])]
  
  /**
   * Minimum text length threshold
   * Use provided value or default to MIN_LENGTH
   */
  const minLength = 
    options.minLength !== null && options.minLength !== undefined
      ? options.minLength
      : MIN_LENGTH

  // ========================================
  // STEP 2: Input validation and preprocessing
  // ========================================
  
  /**
   * Handle edge cases: empty, null, or too short text
   * Return 'undetermined' for insufficient input
   */
  if (!value || value.length < minLength) {
    console.log(`ℹ️ Text too short (${value?.length || 0} < ${minLength}), returning 'und'`)
    return und()
  }

  /**
   * Truncate overly long text for performance
   * Statistical patterns are evident within first 2KB
   */
  if (value.length > MAX_LENGTH) {
    console.log(`ℹ️ Text truncated from ${value.length} to ${MAX_LENGTH} characters`)
    value = value.slice(0, MAX_LENGTH)
  }

  // ========================================
  // STEP 3: Script detection
  // ========================================
  
  /**
   * Determine the primary writing system used in the text
   * This helps narrow down the language candidates significantly
   * 
   * For example:
   * - Latin script: English, Spanish, French, German, etc.
   * - Cyrillic script: Russian, Bulgarian, Serbian, etc.
   * - Arabic script: Arabic, Persian, Urdu, etc.
   */
  const script = getTopScript(value, expressions)
  console.log(`🔍 Detected script: ${script[0] || 'unknown'} (${Math.round(script[1] * 100)}% confidence)`)

  // ========================================
  // STEP 4: Handle single-language scripts
  // ========================================
  
  /**
   * Some scripts map to only one language or no languages
   * Handle these cases efficiently without full trigram analysis
   */
  if (!script[0] || !(script[0] in numericData)) {
    // No script detected or script not in our database
    if (!script[0] || script[1] === 0 || !allow(script[0], only, ignore)) {
      console.log('❌ No suitable script detected or script filtered out')
      return und()
    }

    // Single language for this script
    console.log(`✅ Single-language script detected: ${script[0]}`)
    return singleLanguageTuples(script[0])
  }

  // ========================================
  // STEP 5: Full trigram analysis
  // ========================================
  
  /**
   * Perform statistical analysis using trigram frequencies
   * This is the core of the language detection algorithm
   */
  console.log('🧮 Performing trigram analysis...')
  
  const trigrams = asTuples(value)
  console.log(`📊 Extracted ${trigrams.length} unique trigrams`)
  
  const distances = getDistances(trigrams, numericData[script[0]], only, ignore)
  const results = normalize(value, distances)
  
  console.log(`🎯 Analyzed ${results.length} language candidates`)
  console.log(`🏆 Top result: ${results[0][0]} (${Math.round(results[0][1] * 100)}% confidence)`)
  
  return results
}

/* ===================================================================
 * CORE ALGORITHM FUNCTIONS
 * =================================================================== */

/**
 * Normalize confidence scores to 0-1 range
 * 
 * Raw distance scores are converted to confidence percentages
 * Lower distance = higher confidence
 *
 * @param {string} value - Original input text
 * @param {Array<TrigramTuple>} distances - Raw distance scores
 * @return {Array<TrigramTuple>} - Normalized confidence scores
 */
function normalize(value, distances) {
  if (distances.length === 0) return und()
  
  // Find the minimum distance (best match)
  const min = distances[0][1]
  
  // Calculate the theoretical maximum distance
  const max = value.length * MAX_DIFFERENCE - min
  
  let index = -1
  
  // Convert distances to confidence scores (0-1)
  while (++index < distances.length) {
    distances[index][1] = 1 - (distances[index][1] - min) / max || 0
  }

  return distances
}

/**
 * Detect the primary writing system (script) in the text
 * 
 * Uses regular expressions to count characters from different scripts
 * Returns the script with the highest character count
 *
 * @param {string} value - Text to analyze
 * @param {Record<string, RegExp>} scripts - Script detection patterns
 * @return {[string|undefined, number]} - [script_name, occurrence_ratio]
 */
function getTopScript(value, scripts) {
  let topCount = -1
  let topScript
  let script

  // Test each script pattern against the text
  for (script in scripts) {
    if (own.call(scripts, script)) {
      const count = getOccurrence(value, scripts[script])

      // Track the script with highest character count
      if (count > topCount) {
        topCount = count
        topScript = script
      }
    }
  }

  return [topScript, topCount]
}

/**
 * Calculate what percentage of text matches a pattern
 * 
 * @param {string} value - Text to analyze
 * @param {RegExp} expression - Pattern to match
 * @return {number} - Ratio of matches (0.0 to 1.0)
 */
function getOccurrence(value, expression) {
  const count = value.match(expression)
  return (count ? count.length : 0) / value.length || 0
}

/**
 * Calculate distance scores for all candidate languages
 * 
 * Compares input trigrams against each language model
 * Returns sorted list of languages by similarity
 *
 * @param {Array<TrigramTuple>} trigrams - Input text trigrams
 * @param {Record<string, Record<string, number>>} languages - Language models
 * @param {Array<string>} only - Allowed languages filter
 * @param {Array<string>} ignore - Ignored languages filter
 * @return {Array<TrigramTuple>} - Sorted language-distance pairs
 */
function getDistances(trigrams, languages, only, ignore) {
  // Apply language filters
  languages = filterLanguages(languages, only, ignore)

  const distances = []
  let language

  // Calculate distance for each candidate language
  if (languages) {
    for (language in languages) {
      if (own.call(languages, language)) {
        const distance = getDistance(trigrams, languages[language])
        distances.push([language, distance])
      }
    }
  }

  // Return sorted results (lowest distance first)
  return distances.length === 0 ? und() : distances.sort(sort)
}

/**
 * Calculate statistical distance between input and language model
 * 
 * This is the core similarity metric. It compares the trigram
 * frequency patterns of the input against a language's model.
 *
 * @param {Array<TrigramTuple>} trigrams - Input trigrams with frequencies
 * @param {Record<string, number>} model - Language trigram model
 * @return {number} - Distance score (lower = more similar)
 */
function getDistance(trigrams, model) {
  let distance = 0
  let index = -1

  // Compare each input trigram against the language model
  while (++index < trigrams.length) {
    const trigram = trigrams[index]
    let difference = MAX_DIFFERENCE

    // If trigram exists in language model, calculate rank difference
    if (trigram[0] in model) {
      difference = trigram[1] - model[trigram[0]] - 1

      // Use absolute difference
      if (difference < 0) {
        difference = -difference
      }
    }

    distance += difference
  }

  return distance
}

/* ===================================================================
 * LANGUAGE FILTERING FUNCTIONS
 * =================================================================== */

/**
 * Filter language candidates based on user preferences
 * 
 * @param {Record<string, Record<string, number>>} languages - All languages
 * @param {Array<string>} only - Whitelist (empty = allow all)
 * @param {Array<string>} ignore - Blacklist
 * @return {Record<string, Record<string, number>>} - Filtered languages
 */
function filterLanguages(languages, only, ignore) {
  // No filtering needed
  if (only.length === 0 && ignore.length === 0) {
    return languages
  }

  const filteredLanguages = {}
  let language

  // Apply filters to each language
  for (language in languages) {
    if (allow(language, only, ignore)) {
      filteredLanguages[language] = languages[language]
    }
  }

  return filteredLanguages
}

/**
 * Check if a language passes the filtering criteria
 * 
 * @param {string} language - Language code to check
 * @param {Array<string>} only - Whitelist (empty = allow all)
 * @param {Array<string>} ignore - Blacklist
 * @return {boolean} - Whether language is allowed
 */
function allow(language, only, ignore) {
  // No restrictions
  if (only.length === 0 && ignore.length === 0) {
    return true
  }

  // Must be in whitelist (if specified) AND not in blacklist
  return (
    (only.length === 0 || only.includes(language)) && 
    !ignore.includes(language)
  )
}

/* ===================================================================
 * UTILITY FUNCTIONS
 * =================================================================== */

/**
 * Create an 'undetermined' result
 * Used when language cannot be detected
 * 
 * @return {Array<TrigramTuple>} - [['und', 1]]
 */
function und() {
  return singleLanguageTuples('und')
}

/**
 * Create a single-language result with 100% confidence
 * 
 * @param {string} language - Language code
 * @return {Array<TrigramTuple>} - [[language, 1]]
 */
function singleLanguageTuples(language) {
  return [[language, 1]]
}

/**
 * Sort function for distance arrays
 * Sorts by distance (ascending - lower is better)
 * 
 * @param {TrigramTuple} a - First tuple
 * @param {TrigramTuple} b - Second tuple
 * @return {number} - Sort comparison result
 */
function sort(a, b) {
  return a[1] - b[1]
}

/* ===================================================================
 * DEVELOPMENT AND DEBUGGING UTILITIES
 * =================================================================== */

/**
 * Get detailed analysis information (development helper)
 * 
 * @param {string} text - Text to analyze
 * @return {Object} - Detailed analysis breakdown
 */
export function francDebug(text) {
  const start = performance.now()
  
  console.log('🔍 FRANC DEBUG ANALYSIS')
  console.log('=' .repeat(50))
  console.log(`📝 Input: "${text.slice(0, 100)}${text.length > 100 ? '...' : ''}"`)
  console.log(`📏 Length: ${text.length} characters`)
  
  const results = francAll(text)
  const end = performance.now()
  
  console.log(`⏱️ Analysis time: ${Math.round(end - start)}ms`)
  console.log(`🎯 Top 5 results:`)
  
  results.slice(0, 5).forEach((result, i) => {
    console.log(`  ${i + 1}. ${result[0]}: ${Math.round(result[1] * 100)}%`)
  })
  
  return {
    input: text,
    length: text.length,
    analysisTime: end - start,
    results: results,
    topLanguage: results[0][0],
    confidence: results[0][1]
  }
}

/**
 * Get information about supported languages
 * 
 * @return {Object} - Language statistics
 */
export function francInfo() {
  let totalLanguages = 0
  const scriptCounts = {}
  
  for (const script in numericData) {
    const languages = Object.keys(numericData[script])
    scriptCounts[script] = languages.length
    totalLanguages += languages.length
  }
  
  return {
    totalLanguages,
    scriptCounts,
    supportedScripts: Object.keys(scriptCounts),
    version: 'franc-all@7.2.0-dev'
  }
}

// Log library information on load
console.log('🌍 FRANC Language Detection Library')
console.log(`📚 Supporting ${francInfo().totalLanguages} languages`)
console.log('🚀 Ready for enterprise-scale language detection')

export default franc
