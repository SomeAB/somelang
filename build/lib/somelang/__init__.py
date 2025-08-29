# SomeLang - Advanced Language Detection Library
# High-accuracy language detection with optimized language set

__version__ = "0.0.2"
__author__ = "SomeAB"

# Import main functionality from somelang module
from .somelang import (
    best_detected_language,
    all_detected_languages,
    DEFAULT_WHITELIST,
    LANGUAGE_TRIGRAMS
)

def detect(text, whitelist=None):
    """
    Detect the language of the given text.
    
    Args:
        text (str): Text to analyze
        whitelist (list, optional): List of language codes to consider
                                   Defaults to optimized DEFAULT_WHITELIST
    
    Returns:
        str: ISO 639-3 language code of detected language, or 'und' if undetermined
    """
    return best_detected_language(text, whitelist)

def get_supported_languages():
    """
    Get list of all supported language codes.
    
    Returns:
        list: All supported ISO 639-3 language codes
    """
    languages = []
    for script_languages in LANGUAGE_TRIGRAMS.values():
        languages.extend(script_languages.keys())
    return sorted(languages)

def get_default_whitelist():
    """
    Get the optimized default whitelist of languages.
    
    Returns:
        list: Default language codes with best accuracy
    """
    return DEFAULT_WHITELIST.copy()

def main():
    """Entry point for command line usage"""
    import sys
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        result = detect(text)
        print(f"Detected language: {result}")
    else:
        print("SomeLang v0.1.0 - Advanced Language Detection")
        print("Usage: python -m somelang 'text to analyze'")
        print(f"Supports {len(get_supported_languages())} languages")

if __name__ == "__main__":
    main()
