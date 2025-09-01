"""
This file contains the comprehensive script detection patterns for various languages
Unicode version: 16.0
"""

# Core python imports
import re # For regular patterns
from types import MappingProxyType # For dictionary mutability protection
from typing import Dict, Mapping # For type hinting

# First we declare the regex patterns for reuse in dictionary
# Each regex matches characters specific to a script
# Pre-compiled regex patterns are faster then recompiling on each use
# We are using python private variables for encapsulation
# We are using lowercase verbose name of script for the private variables
# We are using proper unicode blocks for safety & predictability
# Unicode block name is preferred over ISO 15924 codes in this step

_latin_pattern = re.compile(r'[A-Za-z\u00AA\u00BA\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF\u0100-\u017F\u0180-\u024F\u2C60-\u2C7F\uA720-\uA7FF\uAB30-\uAB6F\u1E00-\u1EFF\uFB00-\uFB06\u0250-\u02AF\u1D00-\u1D7F\u1D80-\u1DBF]')

# Covers modern chinese fully. Also chinese characters in Japanese (Kanji) and Korean (Hanja)
_cjk_pattern = re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF]')

_arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\u0870-\u089F\uFB50-\uFDFF\uFE70-\uFEFF]')

_devanagari_pattern = re.compile(r'[\u0900-\u097F\uA8E0-\uA8FF]')

_cyrillic_pattern = re.compile(r'[\u0400-\u04FF\u0500-\u052F\u2DE0-\u2DFF\uA640-\uA69F\u1C80-\u1C8F]')

_bengali_assamese_pattern = re.compile(r'[\u0980-\u09FF]')

# Full Japanese
_full_japanese_pattern = re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF\u3040-\u309F\U0001B100-\U0001B12F\U0001AFF0-\U0001AFFF\U0001B000-\U0001B0FF\U0001B130-\U0001B16F\u3190-\u319F\u30A0-\u30FF\u31F0-\u31FF\uFF00-\uFFEF]')

# Full minus Kanji (from CJK) and Kanbun (Kanji with annotations, Kanbun block)
_japanese_without_chinese_pattern = re.compile(r'[\u3040-\u309F\U0001B100-\U0001B12F\U0001AFF0-\U0001AFFF\U0001B000-\U0001B0FF\U0001B130-\U0001B16F\u30A0-\u30FF\u31F0-\u31FF\uFF00-\uFFEF]')

# Hiragana only
_hiragana_pattern = re.compile(r'[\u3040-\u309F]')

# Katakana plus Kana
_katakana_pattern = re.compile(r'[\U0001B100-\U0001B12F\U0001AFF0-\U0001AFFF\U0001B000-\U0001B0FF\U0001B130-\U0001B16F\u30A0-\u30FF\u31F0-\u31FF\uFF00-\uFFEF]')

# Full Korean
_korean_pattern = re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF\u1100-\u11FF\uA960-\uA97F\uD7B0-\uD7FF\u3130-\u318F\uFF00-\uFFEF\uAC00-\uD7AF]')

# Hangul only (Korean without Hanja from CJK block)
_hangul_pattern = re.compile(r'[\u1100-\u11FF\uA960-\uA97F\uD7B0-\uD7FF\u3130-\u318F\uFF00-\uFFEF\uAC00-\uD7AF]')

# Next we map script names (both code & verbose name per ISO 15924) to the regex patterns
# In order of most widely used script first
# We use Mapping from typing module for type hinting
# We use MappingProxyType for mutability protection
ALL_SCRIPT_PATTERNS: Mapping[str, re.Pattern] = MappingProxyType({
    
    'Latn': _latin_pattern,
    'Latin': _latin_pattern,

    'Hant': _cjk_pattern,
    'Traditional': _cjk_pattern,

    'Hans': _cjk_pattern,
    'Simplified': _cjk_pattern,

    'Arab': _arabic_pattern,
    'Arabic': _arabic_pattern,

    'Deva': _devanagari_pattern,
    'Devanagari': _devanagari_pattern,
    
    'Cyrl': _cyrillic_pattern,
    'Cyrillic': _cyrillic_pattern,

    'Beng': _bengali_assamese_pattern,
    'Bangla': _bengali_assamese_pattern,

    'Jpan': _full_japanese_pattern,
    'Japanese': _full_japanese_pattern,

    'Hrkt': _japanese_without_chinese_pattern,
    'Japanese syllabaries': _japanese_without_chinese_pattern,

    'Hira': _hiragana_pattern,
    'Hiragana': _hiragana_pattern,

    'Kana': _katakana_pattern,
    'Katakana': _katakana_pattern,

    'Kore': _korean_pattern,
    'Korean': _korean_pattern,

    'Hang': _hangul_pattern,
    'Hangul': _hangul_pattern

})

