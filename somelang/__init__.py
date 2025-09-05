# SomeLang - Advanced Language Detection Library
# High-accuracy language detection with optimized language set

__version__ = "0.0.3"
__author__ = "SomeAB"

# Import main functionality from somelang module
from .somelang import (
    best_detected_language,
    all_detected_languages,
    LANGUAGE_TRIGRAMS
)

# Import from default_whitelist module
from .default_whitelist import (
    DEFAULT_WHITELIST,
    LANGUAGE_CODE_TO_NAME
)

def somelang(text, whitelist=None, min_length=10, max_length=2048, verbose=False):
    """
    Detect the language of the given text using optimized DEFAULT_WHITELIST.
    
    Args:
        text (str): Text to analyze
        whitelist (list, optional): List of language codes to consider
                                   If None, uses optimized DEFAULT_WHITELIST
        min_length (int): Minimum text length (default: 10)
        max_length (int): Maximum text length (default: 2048)
        verbose (bool): If True, return language name instead of code (default: False)
    
    Returns:
        str: ISO 639-3 language code (or name if verbose=True), or 'Undetermined' if undetermined
    """
    # Handle text length constraints
    if not text or len(text) < min_length:
        return 'Undetermined' if verbose else 'und'
    
    text = text[:max_length]
    
    # Use DEFAULT_WHITELIST if no whitelist provided
    if whitelist is None:
        whitelist = list(DEFAULT_WHITELIST)
    
    code = best_detected_language(text, whitelist)
    
    if verbose:
        return LANGUAGE_CODE_TO_NAME.get(code, code)
    return code

def somelang_all(text, whitelist=None, min_length=10, max_length=2048, verbose=False):
    """
    Detect all probable languages using optimized DEFAULT_WHITELIST.
    
    Args:
        text (str): Text to analyze
        whitelist (list, optional): List of language codes to consider
                                   If None, uses optimized DEFAULT_WHITELIST
        min_length (int): Minimum text length (default: 10)
        max_length (int): Maximum text length (default: 2048)
        verbose (bool): If True, return language names instead of codes (default: False)
    
    Returns:
        list: List of (language_code/name, confidence_score) tuples sorted by confidence
    """
    # Handle text length constraints
    if not text or len(text) < min_length:
        return [['Undetermined', 1]] if verbose else [['und', 1]]
    
    text = text[:max_length]
    
    # Use DEFAULT_WHITELIST if no whitelist provided
    if whitelist is None:
        whitelist = list(DEFAULT_WHITELIST)
    
    results = all_detected_languages(text, whitelist)
    
    if verbose:
        return [[LANGUAGE_CODE_TO_NAME.get(code, code), confidence] for code, confidence in results]
    return results

def somelang_no_whitelist(text, min_length=10, max_length=2048, verbose=False):
    """
    Detect language using all 202 supported languages (no whitelist).
    
    Args:
        text (str): Text to analyze
        min_length (int): Minimum text length (default: 10)
        max_length (int): Maximum text length (default: 2048)
        verbose (bool): If True, return language name instead of code (default: False)
    
    Returns:
        str: ISO 639-3 language code (or name if verbose=True), or 'Undetermined' if undetermined
    """
    # Handle text length constraints
    if not text or len(text) < min_length:
        return 'Undetermined' if verbose else 'und'
    
    text = text[:max_length]
    
    code = best_detected_language(text, None)
    
    if verbose:
        return LANGUAGE_CODE_TO_NAME.get(code, code)
    return code

def somelang_all_no_whitelist(text, min_length=10, max_length=2048, verbose=False):
    """
    Detect all probable languages using all 202 supported languages.
    
    Args:
        text (str): Text to analyze
        min_length (int): Minimum text length (default: 10)
        max_length (int): Maximum text length (default: 2048)
        verbose (bool): If True, return language names instead of codes (default: False)
    
    Returns:
        list: List of (language_code/name, confidence_score) tuples sorted by confidence
    """
    # Handle text length constraints
    if not text or len(text) < min_length:
        return [['Undetermined', 1]] if verbose else [['und', 1]]
    
    text = text[:max_length]
    
    results = all_detected_languages(text, None)
    
    if verbose:
        return [[LANGUAGE_CODE_TO_NAME.get(code, code), confidence] for code, confidence in results]
    return results

def show_supported_languages(whitelist=False, verbose=False):
    """
    Get list of supported language codes or names.
    
    Args:
        whitelist (bool): If True, return only DEFAULT_WHITELIST languages (158),
                         If False, return all supported languages (202) (default: False)
        verbose (bool): If True, return language names instead of codes (default: False)
    
    Returns:
        list: Language codes or names based on parameters
    """
    if whitelist:
        # Return the default whitelist (158 languages)
        codes = list(DEFAULT_WHITELIST)
    else:
        # Return all supported languages (202 languages)
        codes = []
        for script_languages in LANGUAGE_TRIGRAMS.values():
            codes.extend(script_languages.keys())
        codes = sorted(codes)
    
    if verbose:
        return [LANGUAGE_CODE_TO_NAME.get(code, code) for code in codes]
    return codes

def main():
    """Entry point for command line usage"""
    import sys
    
    # Handle help flags
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h', 'help']:
        print(f"SomeLang v{__version__} - Advanced Language Detection")
        print()
        print("COMMAND LINE USAGE:")
        print("  python -m somelang 'text to analyze'")
        print("  python -m somelang --help")
        print("  python -m somelang --version")
        print()
        print("PYTHON API USAGE:")
        print("  # Basic detection (returns language code)")
        print("  from somelang import somelang")
        print("  lang = somelang('Hello world')  # Returns: 'eng'")
        print()
        print("  # Verbose detection (returns language name)")
        print("  lang = somelang('Hello world', verbose=True)  # Returns: 'English'")
        print()
        print("  # Get all probable languages with confidence scores")
        print("  from somelang import somelang_all")
        print("  results = somelang_all('Hello world')  # Returns: [['eng', 1.0], ...]")
        print()
        print("  # Use all 194 languages (no whitelist restriction)")
        print("  from somelang import somelang_no_whitelist")
        print("  lang = somelang_no_whitelist('Text in rare language')")
        print()
        print("  # List supported languages")
        print("  from somelang import show_supported_languages")
        print("  all_langs = show_supported_languages()  # All 194 languages")
        print("  whitelist = show_supported_languages(whitelist=True)  # 158 common languages")
        print()
        print("EXAMPLES:")
        print("  python -m somelang 'Hello world'                    # Output: eng")
        print("  python -m somelang 'Bonjour tout le monde'          # Output: fra")
        print("  python -m somelang 'Hola como estas'                # Output: spa")
        print("  python -m somelang 'Guten Tag, wie geht es dir'     # Output: deu")
        print()
        print("LANGUAGE SUPPORT:")
        print(f"  Total languages supported: {len(show_supported_languages())}")
        print(f"  Default whitelist (optimized for accuracy): {len(show_supported_languages(whitelist=True))} languages")
        print("  Minimum text length: 10 characters")
        print("  Optimal accuracy: 100+ characters")
        return
    
    # Handle version flag
    if len(sys.argv) > 1 and sys.argv[1] in ['--version', '-v', 'version']:
        print(f"SomeLang v{__version__}")
        return
    
    # Handle text analysis
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        result = somelang(text)
        print(f"Detected language: {result}")
    else:
        print(f"SomeLang v{__version__} - Advanced Language Detection")
        print("Usage: python -m somelang 'text to analyze'")
        print("Use --help for more information")
        print(f"Supports {len(show_supported_languages())} languages")

if __name__ == "__main__":
    main()
