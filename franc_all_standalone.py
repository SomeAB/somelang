"""
Franc All Standalone - Python Port by SomeAB
Version: 0.01

This is a single file standalone implementation of the Franc language detection library. This is based on the 'all' version that contains the maximum number of supported languages.

"""

# Core Python Imports
import re # for regular expressions
from typing import Dict, List, Tuple, Optional, Union # for type hinting
from collections import defaultdict # for default dictionary

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

# Unicode character patterns for different writing systems
# Each regex matches characters specific to a script/language
# Used for quick script detection before statistical analysis
# Pre-compiled regex patterns are faster then recompiling on each use
# Scripts that are used by multiple languages have verbose names below
# Scripts that are 'Language Specific' use the more concise ISO 639-3 codes
UNICODE_SCRIPT_PATTERNS: Dict[str, re.Pattern] = {
    'Latin': re.compile(r'[A-Za-z\u00AA\u00BA\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02B8\u02E0-\u02E4\u1D00-\u1D25\u1D2C-\u1D5C\u1D62-\u1D65\u1D6B-\u1D77\u1D79-\u1DBE\u1E00-\u1EFF\u2071\u207F\u2090-\u209C\u212A\u212B\u2132\u214E\u2160-\u2188\u2C60-\u2C7F\uA722-\uA787\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA7FF\uAB30-\uAB5A\uAB5C-\uAB64\uAB66-\uAB69\uFB00-\uFB06\uFF21-\uFF3A\uFF41-\uFF5A]|\uD801[\uDF80-\uDF85\uDF87-\uDFB0\uDFB2-\uDFBA]|\uD837[\uDF00-\uDF1E\uDF25-\uDF2A]'),
    'Cyrillic': re.compile(r'[\u0400-\u0484\u0487-\u052F\u1C80-\u1C88\u1D2B\u1D78\u2DE0-\u2DFF\uA640-\uA69F\uFE2E\uFE2F]|\uD838[\uDC30-\uDC6D\uDC8F]'),
    'Arabic': re.compile(r'[\u0600-\u0604\u0606-\u060B\u060D-\u061A\u061C-\u061E\u0620-\u063F\u0641-\u064A\u0656-\u066F\u0671-\u06DC\u06DE-\u06FF\u0750-\u077F\u0870-\u088E\u0890\u0891\u0898-\u08E1\u08E3-\u08FF\uFB50-\uFBC2\uFBD3-\uFD3D\uFD40-\uFD8F\uFD92-\uFDC7\uFDCF\uFDF0-\uFDFF\uFE70-\uFE74\uFE76-\uFEFC]|\uD803[\uDE60-\uDE7E\uDEFD-\uDEFF]|\uD83B[\uDE00-\uDE03\uDE05-\uDE1F\uDE21\uDE22\uDE24\uDE27\uDE29-\uDE32\uDE34-\uDE37\uDE39\uDE3B\uDE42\uDE47\uDE49\uDE4B\uDE4D-\uDE4F\uDE51\uDE52\uDE54\uDE57\uDE59\uDE5B\uDE5D\uDE5F\uDE61\uDE62\uDE64\uDE67-\uDE6A\uDE6C-\uDE72\uDE74-\uDE77\uDE79-\uDE7C\uDE7E\uDE80-\uDE89\uDE8B-\uDE9B\uDEA1-\uDEA3\uDEA5-\uDEA9\uDEAB-\uDEBB\uDEF0\uDEF1]'),
    'Devanagari': re.compile(r'[\u0900-\u0950\u0955-\u0963\u0966-\u097F\uA8E0-\uA8FF]|\uD806[\uDF00-\uDF09]'),
    'Myanmar': re.compile(r'[\u1000-\u109F\uA9E0-\uA9FE\uAA60-\uAA7F]'),
    'Ethiopic': re.compile(r'[\u1200-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u135D-\u137C\u1380-\u1399\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E]|\uD839[\uDFE0-\uDFE6\uDFE8-\uDFEB\uDFED\uDFEE\uDFF0-\uDFFE]'),
    'Tibetan': re.compile(r'[\u0F00-\u0F47\u0F49-\u0F6C\u0F71-\u0F97\u0F99-\u0FBC\u0FBE-\u0FCC\u0FCE-\u0FD4\u0FD9\u0FDA]'),
    'Hebrew': re.compile(r'[\u0591-\u05C7\u05D0-\u05EA\u05EF-\u05F4\uFB1D-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFB4F]'),
    'Canadian_Aboriginal': re.compile(r'[\u1400-\u167F\u18B0-\u18F5]|\uD806[\uDEB0-\uDEBF]'),
    'cmn': re.compile(r'[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9]|\uD81B[\uDFE2\uDFE3\uDFF0\uDFF1]|[\uD840-\uD868\uD86A-\uD86C\uD86F-\uD872\uD874-\uD879\uD880-\uD883\uD885-\uD887][\uDC00-\uDFFF]|\uD869[\uDC00-\uDEDF\uDF00-\uDFFF]|\uD86D[\uDC00-\uDF39\uDF40-\uDFFF]|\uD86E[\uDC00-\uDC1D\uDC20-\uDFFF]|\uD873[\uDC00-\uDEA1\uDEB0-\uDFFF]|\uD87A[\uDC00-\uDFE0]|\uD87E[\uDC00-\uDE1D]|\uD884[\uDC00-\uDF4A\uDF50-\uDFFF]|\uD888[\uDC00-\uDFAF]'),
    'ben': re.compile(r'[\u0980-\u0983\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BC-\u09C4\u09C7\u09C8\u09CB-\u09CE\u09D7\u09DC\u09DD\u09DF-\u09E3\u09E6-\u09FE]'),
    'jpn': re.compile(r'[\u3041-\u3096\u309D-\u309F]|\uD82C[\uDC01-\uDD1F\uDD32\uDD50-\uDD52]|\uD83C\uDE00|[\u30A1-\u30FA\u30FD-\u30FF\u31F0-\u31FF\u32D0-\u32FE\u3300-\u3357\uFF66-\uFF6F\uFF71-\uFF9D]|\uD82B[\uDFF0-\uDFF3\uDFF5-\uDFFB\uDFFD\uDFFE]|\uD82C[\uDC00\uDD20-\uDD22\uDD55\uDD64-\uDD67]|[\u3400-\u4DB5\u4E00-\u9FAF]'),
    'jav': re.compile(r'[\uA980-\uA9CD\uA9D0-\uA9D9\uA9DE\uA9DF]'),
    'kor': re.compile(r'[\u1100-\u11FF\u302E\u302F\u3131-\u318E\u3200-\u321E\u3260-\u327E\uA960-\uA97C\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uFFA0-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC]'),
    'tel': re.compile(r'[\u0C00-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3C-\u0C44\u0C46-\u0C48\u0C4A-\u0C4D\u0C55\u0C56\u0C58-\u0C5A\u0C5D\u0C60-\u0C63\u0C66-\u0C6F\u0C77-\u0C7F]'),
    'tam': re.compile(r'[\u0B82\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BBE-\u0BC2\u0BC6-\u0BC8\u0BCA-\u0BCD\u0BD0\u0BD7\u0BE6-\u0BFA]|\uD807[\uDFC0-\uDFF1\uDFFF]'),
    'guj': re.compile(r'[\u0A81-\u0A83\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABC-\u0AC5\u0AC7-\u0AC9\u0ACB-\u0ACD\u0AD0\u0AE0-\u0AE3\u0AE6-\u0AF1\u0AF9-\u0AFF]'),
    'kan': re.compile(r'[\u0C80-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBC-\u0CC4\u0CC6-\u0CC8\u0CCA-\u0CCD\u0CD5\u0CD6\u0CDD\u0CDE\u0CE0-\u0CE3\u0CE6-\u0CEF\u0CF1-\u0CF3]'),
    'mal': re.compile(r'[\u0D00-\u0D0C\u0D0E-\u0D10\u0D12-\u0D44\u0D46-\u0D48\u0D4A-\u0D4F\u0D54-\u0D63\u0D66-\u0D7F]'),
    'pan': re.compile(r'[\u0A01-\u0A03\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A3C\u0A3E-\u0A42\u0A47\u0A48\u0A4B-\u0A4D\u0A51\u0A59-\u0A5C\u0A5E\u0A66-\u0A76]'),
    'tha': re.compile(r'[\u0E01-\u0E3A\u0E40-\u0E5B]'),
    'sin': re.compile(r'[\u0D81-\u0D83\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0DCA\u0DCF-\u0DD4\u0DD6\u0DD8-\u0DDF\u0DE6-\u0DEF\u0DF2-\u0DF4]|\uD804[\uDDE1-\uDDF4]'),
    'ell': re.compile(r'[\u0370-\u0373\u0375-\u0377\u037A-\u037D\u037F\u0384\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03E1\u03F0-\u03FF\u1D26-\u1D2A\u1D5D-\u1D61\u1D66-\u1D6A\u1DBF\u1F00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FC4\u1FC6-\u1FD3\u1FD6-\u1FDB\u1FDD-\u1FEF\u1FF2-\u1FF4\u1FF6-\u1FFE\u2126\uAB65]|\uD800[\uDD40-\uDD8E\uDDA0]|\uD834[\uDE00-\uDE45]'),
    'khm': re.compile(r'[\u1780-\u17DD\u17E0-\u17E9\u17F0-\u17F9\u19E0-\u19FF]'),
    'hye': re.compile(r'[\u0531-\u0556\u0559-\u058A\u058D-\u058F\uFB13-\uFB17]'),
    'sat': re.compile(r'[\u1C50-\u1C7F]'),
    'kat': re.compile(r'[\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u10FF\u1C90-\u1CBA\u1CBD-\u1CBF\u2D00-\u2D25\u2D27\u2D2D]'),
    'lao': re.compile(r'[\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EBD\u0EC0-\u0EC4\u0EC6\u0EC8-\u0ECE\u0ED0-\u0ED9\u0EDC-\u0EDF]'),
    'zgh': re.compile(r'[\u2D30-\u2D67\u2D6F\u2D70\u2D7F]'),
    'iii': re.compile(r'[\uA000-\uA48C\uA490-\uA4C6]'),
    'aii': re.compile(r'[\u0700-\u070D\u070F-\u074A\u074D-\u074F\u0860-\u086A]'),
    'div': re.compile(r'[\u0780-\u07B1]'),
    'vai': re.compile(r'[\uA500-\uA62B]'),
    'chr': re.compile(r'[\u13A0-\u13F5\u13F8-\u13FD\uAB70-\uABBF]'),
    'kkh': re.compile(r'[\u1A20-\u1A5E\u1A60-\u1A7C\u1A7F-\u1A89\u1A90-\u1A99\u1AA0-\u1AAD]'),
    'blt': re.compile(r'[\uAA80-\uAAC2\uAADB-\uAADF]'),
}

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
        script_patterns = UNICODE_SCRIPT_PATTERNS

    # Initialize best_score, best_script
    best_score = -1.0 # Negative value means no patterns tested yet
    best_script = None

    # Check each script pattern against the text
    for script, pattern in script_patterns.items():
        current_score = calculate_script_ratio(text, pattern)

        if current_score > best_score:
            best_score = current_score
            best_script = script

    # Return the name of the best matching script and its score
    return best_script, best_score