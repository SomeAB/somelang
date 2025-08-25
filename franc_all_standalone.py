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

    

    

