"""
SomeLang - by SomeAB

This is a natural language detection library

"""

# Core Python Imports
import re # For regular expressions
from typing import Dict, List, Tuple, Optional # For type hinting

# Import NEW script patterns & code-to-name mapping
from .script_patterns import ALL_SCRIPT_PATTERNS, SCRIPT_CODE_TO_NAME

# Import NEW trigrams data
from .trigrams_data_0003D import LANGUAGE_TRIGRAMS

# Import default whitelist
# USE THIS FOR BETTER ACCURACY ON SHORTER TEXT ( text < 100 characters )
from .default_whitelist import DEFAULT_WHITELIST

# Constants
PENALTY_FACTOR = 300 # This is based on no of trigrams we have for each language. Update this, if no of trigrams changes in future
MIN_LENGTH = 10 # Minimum length of text. Below this, undefined result will be returned
MAX_LENGTH = 2048 # Maximum length of text. Beyond this, it will be truncated
TRIGRAMS_DATA = None # Initialize as empty
SHORT_TEXT_LENGTH = 50
MEDIUM_TEXT_LENGTH = 100

# ========================================
# TEXT PROCESSING AND NORMALIZATION
# ========================================

# This is equivalent to 'v' and 'j' variables in js version
# /g is global flag in js regex, thus not used here in python
PATTERN_01 = r'[\t\n\v\f\r ]+' # This matches tab, new line, vertical tab, form feed, carriage return and space only
PATTERN_02 = r'\s+' # This matches all whitespace characters including some unicode characters


def normalize_whitespace(text: str, options: dict = None) -> str:
    """Direct port of JavaScript function d(i, a)"""

    # Because dict is a 'mutable' type, we do not initialize it in the function definition itself, but here instead
    # This way, a fresh dictionary is created each time, instead of once, thus avoiding unpredictable behavior
    if options is None:
        options = {}

    # This is equivalent to functions 'f' and 'z' in js version
    # This helps preserve line break characters, while converting only the other whitespace characters to a single space
    # group(0) returns all groups of matches found
    def preserve_line_ending(match):
        line_break = re.search(r'\r?\n|\r', match.group(0))  # Looks for line breaks i.e., '\n'(Linux), '\r'(Mac), '\r\n'(Windows) anywhere in the text
        return line_break.group(0) if line_break else " "  # Returns the line breaks as it is (preserved) and converts to single space any other whitespace characters
    
    # Replace all whitespace characters with a single space
    def replace_with_space(match):
        return " "
    
    # This is equivalent to function 'q' in js version - creates wrapper for edge trimming
    # The outer function just wraps around the original function which can be either of the above two functions
    # The inner function performs the actual conditional trimming
    def create_trim_wrapper(original_func):
        def trim_wrapper(match):
            start_pos = match.start()
            end_pos = match.end()
            full_length = len(text)
            # If matched whitespace is at start or end of string, trim it fully (instead of converting to single space)
            if start_pos == 0 or end_pos == full_length:
                return ""
            # If matched whitespace is in the middle of the string, convert to single space
            else:
                return original_func(match)
        return trim_wrapper
    
    # Choose & Store which function to use, from above two, based on the provided option
    # Uses 'get' method to safely get key from 'options' dictionary or return None
    replacer = preserve_line_ending if options.get('preserveLineEndings') else replace_with_space
    
    # Apply trim wrapper if trim option is enabled (equivalent to: a.trim ? q(n) : n)
    if options.get('trim'):
        replacer = create_trim_wrapper(replacer) # Reassign by further wrapping around what we already had

    
    # If html is encountered, use pattern 1 otherwise 2
    # Uses 'get' method to safely get key from 'options' dictionary or return None
    pattern = PATTERN_01 if options.get('style') == 'html' else PATTERN_02

    # Finally, deal with the whitespace characters & return the string
    # Explicitly convert 'text' to string, in case a non-string type is passed. Type hints don't guarantee type safety
    return re.sub(pattern, replacer, str(text))

def clean_text_t01(text: str) -> str:
    """Direct port of JavaScript function x(i)"""
    
    # Handle null/None input (JavaScript: i == null)
    if text is None:
        return ""
    
    # Convert to string explicitly (for safety) and replace punctuation with spaces
    # The range u0021 to u0040 covers ASCII special symbols & numbers 0-9
    text_no_punct = re.sub(r'[\u0021-\u0040]+', ' ', str(text))
    
    # Normalize whitespace using our normalize_whitespace function
    text_normalized = normalize_whitespace(text_no_punct)
    
    # Strip on both ends and convert to lowercase
    return text_normalized.strip().lower()

# ========================================
# BLUEPRINT OF N-GRAMS EXTRACTION FUNCTIONS
# ========================================

def ngrams_base_function(n: int):
    """Direct port of JavaScript function h(i)"""

    # Check if n is either int/float, n is a number, n is a bigger than 1, n is not infinity
    # n != n is a clever check, since all numbers are equal to themselves, and NaN (Not a Number) is not, as per IEEE 754
    # n == float('inf') checks if the number is positive infinity, as per IEEE 754
    if not isinstance(n, (int, float)) or n != n or n < 1 or n == float('inf'):
        raise ValueError(f"'{n}' is not a valid argument for n-gram extraction function")
    
    # Convert to int, if it's a valid float
    n = int(n)

    def extract_ngrams(text):
        """Inner function that extracts n-grams from text"""

        # Initialize a list
        ngrams = []

        # Handle null/None input
        if text is None:
            return ngrams
        
        # Convert to string (if needed, as per defensive programming)
        text_str = str(text)

        # Calculate how many n-grams we can extract
        max_ngrams = (len(text_str) - n) + 1

        # If text is too short, return empty list
        if max_ngrams < 1:
            return ngrams
        
        # Extract n-grams using 'sliding window' concept
        # We are using python slicing of the form s[a:b], where we ask for 'a' upto (but not including) 'b' like 0:2, 1:3, etc
        for i in range(max_ngrams):
            one_ngram = text_str[i:i + n]
            ngrams.append(one_ngram)
        
        # Return the list containing all the ngrams
        return ngrams
    
    return extract_ngrams

# N-gram extractors for bigrams and trigrams (equivalent to JavaScript: var O = h(2), m = h(3))
# Used for statistical language detection
bigrams_extractor = ngrams_base_function(2)
trigrams_extractor = ngrams_base_function(3)

# ========================================
# TRIGRAMS LIST & SORTED FREQUENCY MAP GENERATION
# ========================================

def extract_trigrams(text: str) -> List[str]:
    """Direct port of JavaScript function D(i)"""

    # Add some padding on both ends, and use our trigrams extractor function on cleaned text
    # Equivalent to js: m(" " + x(i) + " ")
    trigrams_list = trigrams_extractor(" " + clean_text_t01(text) + " ")

    # Return the list of trigrams
    return trigrams_list

def generate_trigrams_frequency_map(text: str) -> Dict[str, int]:
    """Direct port of JavaScript function F(i)"""

    # Get the list of trigrams using our extract_trigrams function
    trigrams_list = extract_trigrams(text)

    # Initialize an empty frequency map (dictionary)
    frequency_map = {}

    # Count frequencies of each trigram
    for trigram in trigrams_list:
        if trigram in frequency_map:
            frequency_map[trigram] += 1
        else:
            frequency_map[trigram] = 1

    # Return the generated frequency map (dictionary)
    return frequency_map

def sort_trigrams_by_frequency(text: str) -> List[List]:
    """Direct port of JavaScript functions y(i) & A(i, a)"""

    # Get frequency map using our generator function
    frequency_map = generate_trigrams_frequency_map(text)

    # Convert dictionary to list of [trigram, frequency] pairs
    # The small cost of conversion here is outweighed by use of dictionary in previous function
    tf_pairs = [] # List initialized

    for trigram, frequency in frequency_map.items():
        tf_pairs.append([trigram, frequency])

    # Sort the list of [trigram, frequency] pairs in ascending order by frequency
    tf_pairs.sort(key=lambda column: column[1])

    # Return the sorted list of [trigram, frequency] pairs
    return tf_pairs

# ========================================
# SCRIPT DETECTION
# ========================================

def calculate_script_ratio(text: str, pattern: re.Pattern) -> float:
    """Direct port of JavaScript function T(i, a)"""

    # Return zero, if no text provided
    if not text:
        return 0.0

    # Find all character matches for the given script pattern in the text. 'findall' is part of the re module
    # Returns a list of all matches
    matches = pattern.findall(text)
    
    # Measure no of matches (and not no of characters)
    match_count = len(matches)
    
    # Return ratio of no of matches divided by total no of characters in the text (0.0 to 1.0)
    return match_count / len(text)

def detect_dominant_script(text: str, script_patterns: Dict[str, re.Pattern] = None) -> Tuple[Optional[str], float]:
    """Direct port of JavaScript function N(i, a) & T(i, a)"""

    # Fallback to use the patterns defined above, if no other custom pattern is passed
    if script_patterns is None:
        script_patterns = ALL_SCRIPT_PATTERNS
    
    # Handle empty/None text case - return no detection
    if not text or len(text.strip()) == 0:
        return None, 0.0

    # Initialize best_score, best_script
    best_score = -1.0 # Negative value means no patterns tested yet
    best_script = None

    # Check each script pattern against the text
    for script, pattern in script_patterns.items():
        current_score = calculate_script_ratio(text, pattern)

        if current_score > best_score:
            best_score = current_score
            best_script = script

    # Return None if no script patterns actually matched
    if best_score == 0.0:
        return None, 0.0

    # Return the name of the best matching script and its score
    return best_script, best_score

# ========================================
# SCORING & HELPER FUNCTIONS
# ========================================

def calculate_trigrams_distance(input_trigrams: List[List], language_model: Dict[str, int]) -> int:
    """ Direct port of Javascript function I(i, a) """

    total_distance = 0 # lower means better match

    # Iterate through each trigram, frequency pair, start with maximum penalty
    for trigram_pair in input_trigrams:
        current_trigram = trigram_pair[0]
        penalty = PENALTY_FACTOR

        # If trigram exists in language model
        if current_trigram in language_model:
            # Calculate position difference
            input_freq_rank = trigram_pair[1] # u[1] in js
            model_position = language_model[current_trigram] # a[u[0]] in js
            penalty = input_freq_rank - model_position - 1

            # Take absolute value if negative
            if penalty < 0:
                penalty = -penalty

        # Calculate total distance by adding the penalty per trigram
        total_distance += penalty

    # Return the total distance. Lower means better match
    return total_distance

def is_language_allowed(lang_code: str, whitelist: List[str], blacklist: List[str]) -> bool:
    """ Direct port of Javascript function c(i, a, n)"""

    # If no whitelist provided, initialize an empty whitelist
    if not whitelist:
        whitelist = []

    # If no blacklist provided, initialize an empty blacklist
    if not blacklist:
        blacklist = []

    # If both whitelist and blacklist are empty, the language is allowed
    if len(whitelist) == 0 and len(blacklist) == 0:
        return True

    # Returns a single bool value
    # Don't worry, handles all scenarios correctly
    return (len(whitelist) == 0 or lang_code in whitelist) and (lang_code not in blacklist)

def filter_languages_by_whitelist_blacklist(languages_dict: Dict[str, Dict], whitelist: List[str], blacklist: List[str]) -> Dict[str, Dict]:
    """ Direct port of Javascript function _(i, a, n)"""

    # If no whitelist provided, initialize an empty whitelist
    if not whitelist:
        whitelist = []

    # If no blacklist provided, initialize an empty blacklist
    if not blacklist:
        blacklist = []

    # If no filters, return all languages
    if len(whitelist) == 0 and len(blacklist) == 0:
        return languages_dict
    
    # Initialize a dictionary to hold only the allowed languages
    allowed_languages = {}

    # Iterate through the languages & their trigram data
    for lang_code, lang_data in languages_dict.items():
        # Check if the language is allowed using our helper function
        if is_language_allowed(lang_code, whitelist, blacklist):
            # If allowed, add the allowed language & its trigram data to allowed_languages dictionary
            allowed_languages[lang_code] = lang_data

    # Return the subset dictionary containing only the allowed languages
    return allowed_languages

def handle_undefined_result() -> List[List]:
    """ Direct port of Javascript function r() """
    return [["und", 1]]

def handle_single_result(lang_code: str) -> List[List]:
    """ Direct port of Javascript function w(i) """
    return [[lang_code, 1]]

def score_languages(input_trigrams: List[List], candidate_languages: Dict[str, Dict], whitelist: List[str] = None, blacklist: List[str] = None) -> List[List]:
    """ Direct port of Javascript function S(i, a, n, e) """

    # Get list of allowed languages using our helper function
    allowed_languages = filter_languages_by_whitelist_blacklist(candidate_languages, whitelist, blacklist)

    # If no languages are allowed, return undefined result
    if not allowed_languages:
        return handle_undefined_result()

    # Initialize a list to hold the results in the form language_code, distance_score
    results = []

    # Score each allowed language by calculating trigram distance (lower is better)
    for lang_code, lang_data in allowed_languages.items():
        # Calculate the distance score for the current language
        distance_score = calculate_trigrams_distance(input_trigrams, lang_data)

        # Append the language code and its distance score to the results
        results.append([lang_code, distance_score])

    # Return undefined, if no results
    if len(results) == 0:
        return handle_undefined_result()
    
    # Sort the results by distance_score (lower is better)
    # This is equivalent to js function M(i, a)
    results.sort(key=lambda x: x[1])

    # Return the final sorted results as a list
    return results

def normalize_scores(text: str, raw_scores: List[List]) -> List[List]:
    """ Direct port of Javascript function L(i, a) """

    # No need for empty check due to handle_undefined_results being used in helper function

    # Get best(lowest) distance score from the already sorted results list. 0 is the first pair, and 1 is the score of that language
    best_score = raw_scores[0][1]

    # len(text)*PENALTY_FACTOR is the theoritical maximum possible distance for a given text
    # score_range is just how much room is left after best_score is substracted from maximum distance, for placing the the rest of the languages & their scores
    score_range = len(text) * PENALTY_FACTOR - best_score

    # Iterate through the list of raw scores
    for i in range(len(raw_scores)):

        # Extract the language code which is the first element hence '0'
        lang_code = raw_scores[i][0]

        # Extract the language distance score which is the second element hence '1'
        raw_distance = raw_scores[i][1]
        
        # In the case of first language, confidence gets calculated as 1, as it is already sorted to have best score
        # For the rest the score is between 1 and 0, getting proportionally lower with each language
        if score_range > 0:
            confidence = 1 - (raw_distance - best_score) / score_range
        else:
            confidence = 0
        
        # If confidence is negative, return 0
        confidence = confidence if confidence >= 0 else 0

        # Update the second element in raw_scores to be the normalized score i.e., confidence
        raw_scores[i][1] = confidence
    
    # Return the final language, normalized score combo as a list
    return raw_scores

# ========================================
# MAIN FUNCTIONS
# ========================================

def all_detected_languages(text: str, options = None) -> List[List]:
    """ Direct Port of Javascript function B() """

    # Handle simplified usage: if options is a list, treat it as whitelist
    if isinstance(options, list):
        options = {'whitelist': options}

    # Because dict is a 'mutable' type, we do not initialize it in the function definition itself, but here instead
    # This way, a fresh dictionary is created each time, instead of once, thus avoiding unpredictable behavior
    # This also handles the case where no options are provided
    if options is None:
        options = {}

    # Extract whitelist languages from options
    whitelist = []
    if options.get('whitelist'):
        whitelist.extend(options['whitelist'])

    # Use the alternate option name 'only'
    if options.get('only'):
        whitelist.extend(options['only'])

    # Extract blacklist languages from options
    blacklist = []
    if options.get('blacklist'):
        blacklist.extend(options['blacklist'])

    # Use the alternate option name 'ignore'
    if options.get('ignore'):
        blacklist.extend(options['ignore'])

    # Can also get minimum length from options
    min_length = options.get('minLength', MIN_LENGTH)

    # If the text is too short, return undefined
    if not text or len(text) < min_length:
        return handle_undefined_result()
    
    # Truncate text to maximum length
    text = text[:MAX_LENGTH]

    # Placeholder comment (will be changed later)
    TRIGRAMS_DATA = LANGUAGE_TRIGRAMS

    # Detect dominant script
    script, confidence = detect_dominant_script(text, ALL_SCRIPT_PATTERNS)

    # If no known script detected, return undefined
    if not script:
        return handle_undefined_result()

    # Check if script is in our top-level of our LANGUAGE_TRIGRAMS dictionary, which is scripts actually
    # Also Returns 'script name' if no trigrams data is found for that script in trigrams file, i.e., it says the script is the language itself
    if script not in TRIGRAMS_DATA:
        if confidence == 0 or not is_language_allowed(script, whitelist, blacklist):
            return handle_undefined_result()
        return handle_single_result(script)

    # Generate trigrams from input text
    input_trigrams = sort_trigrams_by_frequency(text)

    # Get list of languages in the given script from all languages available to us
    select_languages = TRIGRAMS_DATA[script]

    # Calculate and get raw scores
    raw_scores = score_languages(input_trigrams, select_languages, whitelist, blacklist)

    # Return the pairs of detected languages and their scores as a list after normalizing scores
    return normalize_scores(text, raw_scores)

def best_detected_language(text: str, options = None) -> str:
    """Direct port of Javascript function K(i, a)"""
    
    # Handle simplified usage: if options is a list, treat it as whitelist
    if isinstance(options, list):
        options = {'whitelist': options}
    
    return all_detected_languages(text, options)[0][0]
