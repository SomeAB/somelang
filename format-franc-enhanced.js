/**
 * Enhanced Script to format the minified franc-all-720-offline.js file
 * Uses proper JavaScript parsers for better formatting
 */

const fs = require('fs');
const path = require('path');
const beautify = require('js-beautify').js;

// Configuration
const INPUT_FILE = 'franc-all-720-offline.js';
const OUTPUT_FILE = 'franc-all-720-standalone.js';

/**
 * Advanced formatting with proper code structure
 */
function formatFrancFileAdvanced() {
    try {
        console.log('Reading input file:', INPUT_FILE);
        const inputPath = path.join(__dirname, INPUT_FILE);
        
        if (!fs.existsSync(inputPath)) {
            throw new Error(`Input file ${INPUT_FILE} not found`);
        }
        
        const minifiedCode = fs.readFileSync(inputPath, 'utf8');
        console.log('Original file size:', minifiedCode.length, 'characters');
        
        // Extract the header comment
        let headerComment = '';
        let codeWithoutHeader = minifiedCode;
        
        if (minifiedCode.startsWith('/*')) {
            const commentEnd = minifiedCode.indexOf('*/') + 2;
            headerComment = minifiedCode.substring(0, commentEnd);
            codeWithoutHeader = minifiedCode.substring(commentEnd).trim();
        }
        
        console.log('Beautifying JavaScript...');
        
        // Use js-beautify for proper formatting
        const beautifyOptions = {
            indent_size: 2,
            indent_char: ' ',
            max_preserve_newlines: 2,
            preserve_newlines: true,
            keep_array_indentation: false,
            break_chained_methods: false,
            indent_scripts: 'normal',
            brace_style: 'collapse',
            space_before_conditional: true,
            unescape_strings: false,
            jslint_happy: false,
            end_with_newline: false,
            wrap_line_length: 100,
            indent_inner_html: false,
            comma_first: false,
            e4x: false,
            indent_empty_lines: false
        };
        
        let formattedCode = beautify(codeWithoutHeader, beautifyOptions);
        
        // Add meaningful section comments
        formattedCode = addSectionComments(formattedCode);
        
        // Combine header and formatted code
        const finalCode = headerComment + '\n\n' + formattedCode;
        
        console.log('Writing output file:', OUTPUT_FILE);
        const outputPath = path.join(__dirname, OUTPUT_FILE);
        fs.writeFileSync(outputPath, finalCode, 'utf8');
        
        console.log('Formatted file size:', finalCode.length, 'characters');
        console.log('Size increase:', Math.round((finalCode.length / minifiedCode.length - 1) * 100), '%');
        console.log('✅ Successfully created', OUTPUT_FILE);
        
        // Show structure overview
        showCodeStructure(finalCode);
        
    } catch (error) {
        console.error('❌ Error formatting file:', error.message);
        process.exit(1);
    }
}

/**
 * Add meaningful section comments to organize the code
 */
function addSectionComments(code) {
    let enhanced = code;
    
    // N-gram functions
    enhanced = enhanced.replace(
        /var O = h\(2\), m = h\(3\);/, 
        '// ========================================\n// N-GRAM GENERATION UTILITIES\n// ========================================\n\n// Create 2-gram and 3-gram generators\nvar O = h(2), m = h(3);'
    );
    
    enhanced = enhanced.replace(
        /function h\(i\) \{/, 
        '\n/**\n * N-gram function generator\n * Creates functions that extract n-grams from text\n * @param {number} i - The n-gram size\n * @returns {function} Function that extracts n-grams\n */\nfunction h(i) {'
    );
    
    // Text processing functions
    enhanced = enhanced.replace(
        /var j = \/\\s\+\/g,\s*v = \/\[\\t\\n\\v\\f\\r \]\+\/g;/, 
        '\n// ========================================\n// TEXT PROCESSING AND NORMALIZATION\n// ========================================\n\n// Regular expressions for whitespace handling\nvar j = /\\s+/g,\n    v = /[\\t\\n\\v\\f\\r ]+/g;'
    );
    
    enhanced = enhanced.replace(
        /function d\(i, a\) \{/, 
        '\n/**\n * Text normalization function\n * Normalizes whitespace in text strings\n * @param {string} i - Input text\n * @param {object} a - Options for normalization\n * @returns {string} Normalized text\n */\nfunction d(i, a) {'
    );
    
    enhanced = enhanced.replace(
        /function x\(i\) \{/, 
        '\n/**\n * Text cleaning function\n * Removes punctuation and normalizes text for analysis\n * @param {string} i - Input text\n * @returns {string} Cleaned text\n */\nfunction x(i) {'
    );
    
    // Unicode patterns
    enhanced = enhanced.replace(
        /var b = \{/, 
        '\n// ========================================\n// UNICODE SCRIPT DETECTION PATTERNS\n// ========================================\n\n/**\n * Unicode character patterns for different writing systems\n * Each pattern matches characters specific to a script\n */\nvar b = {'
    );
    
    // Language patterns
    enhanced = enhanced.replace(
        /var s = \{/, 
        '\n// ========================================\n// LANGUAGE-SPECIFIC TRIGRAM PATTERNS\n// ========================================\n\n/**\n * Language detection patterns based on character trigrams\n * Each language has its most common trigrams with frequency data\n */\nvar s = {'
    );
    
    // Main functions
    enhanced = enhanced.replace(
        /function K\(i, a\) \{/, 
        '\n// ========================================\n// MAIN LANGUAGE DETECTION FUNCTIONS\n// ========================================\n\n/**\n * Main franc function - detects the most likely language\n * @param {string} i - Input text to analyze\n * @param {object} a - Detection options\n * @returns {string} ISO 639-3 language code\n */\nfunction K(i, a) {'
    );
    
    enhanced = enhanced.replace(
        /function B\(i, a\) \{/, 
        '\n/**\n * Franc all function - returns all language matches with confidence scores\n * @param {string} i - Input text to analyze\n * @param {object} a - Detection options\n * @returns {Array} Array of [language, confidence] pairs\n */\nfunction B(i, a) {'
    );
    
    // Helper functions
    enhanced = enhanced.replace(
        /function L\(i, a\) \{/, 
        '\n/**\n * Normalize confidence scores\n * @param {string} i - Input text\n * @param {Array} a - Raw scores\n * @returns {Array} Normalized scores\n */\nfunction L(i, a) {'
    );
    
    enhanced = enhanced.replace(
        /function N\(i, a\) \{/, 
        '\n/**\n * Detect script using Unicode patterns\n * @param {string} i - Input text\n * @param {object} a - Script patterns\n * @returns {Array} [script, confidence]\n */\nfunction N(i, a) {'
    );
    
    // Export section
    enhanced = enhanced.replace(
        /export \{/, 
        '\n// ========================================\n// MODULE EXPORTS\n// ========================================\n\nexport {'
    );
    
    return enhanced;
}

/**
 * Display code structure overview
 */
function showCodeStructure(code) {
    console.log('\n📊 Code Structure Overview:');
    console.log('================================');
    
    const lines = code.split('\n');
    const sections = [];
    
    lines.forEach((line, index) => {
        if (line.includes('// ========================================')) {
            const nextLine = lines[index + 1];
            if (nextLine && nextLine.startsWith('//')) {
                sections.push({
                    line: index + 1,
                    title: nextLine.replace(/^\/\/ /, '').trim()
                });
            }
        }
    });
    
    sections.forEach(section => {
        console.log(`📍 Line ${section.line.toString().padStart(3)}: ${section.title}`);
    });
    
    console.log('\n📈 Statistics:');
    console.log(`   Total lines: ${lines.length}`);
    console.log(`   Functions: ${(code.match(/function \w+/g) || []).length}`);
    console.log(`   Variables: ${(code.match(/var \w+/g) || []).length}`);
    console.log(`   Comments: ${(code.match(/\/\*/g) || []).length + (code.match(/\/\//g) || []).length}`);
}

// Run the enhanced formatter
if (require.main === module) {
    formatFrancFileAdvanced();
}

module.exports = { formatFrancFileAdvanced, addSectionComments };
