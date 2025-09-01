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

_devanagari_pattern = re.compile(r'[\u0900-\u097F\uA8E0-\uA8FF\U00011B00-\U00011B5F\u1CD0-\u1CFF]')

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

# Indic Scripts (besides Devanagari and Bengali above)
_ahom_pattern = re.compile(r'[\U00011700-\U0001174F]')
_bhaiksuki_pattern = re.compile(r'[\U00011C00-\U00011C6F]')
_brahmi_pattern = re.compile(r'[\U00011000-\U0001107F]')
_chakma_pattern = re.compile(r'[\U00011100-\U0001114F]')
_dives_akuru_pattern = re.compile(r'[\U00011900-\U0001195F]')
_dogra_pattern = re.compile(r'[\U00011800-\U0001184F]')
_grantha_pattern = re.compile(r'[\U00011300-\U0001137F]')
_gujarati_pattern = re.compile(r'[\u0A80-\u0AFF]')
_gunjala_gondi_pattern = re.compile(r'[\U00011D60-\U00011DAF]')
_gurmukhi_pattern = re.compile(r'[\u0A00-\u0A7F]')
_gurung_khema_pattern = re.compile(r'[\U00016100-\U0001613F]')
_kaithi_pattern = re.compile(r'[\U00011080-\U000110CF]')
_kannada_pattern = re.compile(r'[\u0C80-\u0CFF]')
_kharoshthi_pattern = re.compile(r'[\U00010A00-\U00010A5F]')
_khojki_pattern = re.compile(r'[\U00011200-\U0001124F]')
_kirat_rai_pattern = re.compile(r'[\U00016D40-\U00016D7F]')
_khudawadi_pattern = re.compile(r'[\U000112B0-\U000112FF]')
_lepcha_pattern = re.compile(r'[\u1C00-\u1C4F]')
_limbu_pattern = re.compile(r'[\u1900-\u194F]')
_mahajani_pattern = re.compile(r'[\U00011150-\U0001117F]')
_masaram_gondi_pattern = re.compile(r'[\U00011D00-\U00011D5F]')
_malayalam_pattern = re.compile(r'[\u0D00-\u0D7F]')
_meetei_mayek_pattern = re.compile(r'[\uABC0-\uABFF\uAAE0-\uAAFF]')
_modi_pattern = re.compile(r'[\U00011600-\U0001165F]')
_mro_pattern = re.compile(r'[\U00016A40-\U00016A6F]')
_multani_pattern = re.compile(r'[\U00011280-\U000112AF]')
_nag_mundari_pattern = re.compile(r'[\U0001E4D0-\U0001E4FF]')
_nandinagari_pattern = re.compile(r'[\U000119A0-\U000119FF]')
_newa_pattern = re.compile(r'[\U00011400-\U0001147F]')
_ol_chiki_pattern = re.compile(r'[\u1C50-\u1C7F]')
_ol_onal_pattern = re.compile(r'[\U0001E5D0-\U0001E5FF]')
_oriya_pattern = re.compile(r'[\u0B00-\u0B7F]')
_saurashtra_pattern = re.compile(r'[\uA880-\uA8DF]')
_sharada_pattern = re.compile(r'[\U00011180-\U000111DF]')
_siddham_pattern = re.compile(r'[\U00011580-\U000115FF]')
_sinhala_pattern = re.compile(r'[\u0D80-\u0DFF\U000111E0-\U000111FF]')
_sora_sompeng_pattern = re.compile(r'[\U000110D0-\U000110FF]')
_sunuwar_pattern = re.compile(r'[\U00011BC0-\U00011BFF]')
_syloti_nagri_pattern = re.compile(r'[\uA800-\uA82F]')
_takri_pattern = re.compile(r'[\U00011680-\U000116CF]')
_tamil_pattern = re.compile(r'[\u0B80-\u0BFF\U00011FC0-\U00011FFF]')
_telugu_pattern = re.compile(r'[\u0C00-\u0C7F]')
_thaana_pattern = re.compile(r'[\u0780-\u07BF]')
_tirhuta_pattern = re.compile(r'[\U00011480-\U000114DF]')
_toto_pattern = re.compile(r'[\U0001E290-\U0001E2BF]')
_tulu_tigalari_pattern = re.compile(r'[\U00011380-\U000113FF]')
_wancho_pattern = re.compile(r'[\U0001E2C0-\U0001E2FF]')
_warang_citi_pattern = re.compile(r'[\U000118A0-\U000118FF]')

# Next we map script names (both code & verbose name per ISO 15924) to the regex patterns
# In order of most widely used script first
# We use Mapping from typing module for type hinting
# We use MappingProxyType for mutability protection
ALL_SCRIPT_PATTERNS: Mapping[str, re.Pattern] = MappingProxyType({
    
    'Latn': _latin_pattern,
    'Latin': _latin_pattern,

    # Chinese Scripts Group

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

    # Japanese Scripts Group

    'Jpan': _full_japanese_pattern,
    'Japanese': _full_japanese_pattern,

    'Hrkt': _japanese_without_chinese_pattern,
    'Japanese syllabaries': _japanese_without_chinese_pattern,

    'Hira': _hiragana_pattern,
    'Hiragana': _hiragana_pattern,

    'Kana': _katakana_pattern,
    'Katakana': _katakana_pattern,

    # Korean Scripts Group

    'Kore': _korean_pattern,
    'Korean': _korean_pattern,

    'Hang': _hangul_pattern,
    'Hangul': _hangul_pattern,

    # Indic Scripts Group

    'Ahom': _ahom_pattern, # Both code and verbose name are same

    'Bhks': _bhaiksuki_pattern,
    'Bhaiksuki': _bhaiksuki_pattern,

    'Brah': _brahmi_pattern,
    'Brahmi': _brahmi_pattern,

    'Cakm': _chakma_pattern,
    'Chakma': _chakma_pattern,

    'Diak': _dives_akuru_pattern,
    'Dives Akuru': _dives_akuru_pattern,

    'Dogr': _dogra_pattern,
    'Dogra': _dogra_pattern,

    'Gran': _grantha_pattern,
    'Grantha': _grantha_pattern,

    'Gujr': _gujarati_pattern,
    'Gujarati': _gujarati_pattern,

    'Gong': _gunjala_gondi_pattern,
    'Gunjala Gondi': _gunjala_gondi_pattern,

    'Guru': _gurmukhi_pattern,
    'Gurmukhi': _gurmukhi_pattern,

    'Gukh': _gurung_khema_pattern,
    'Gurung Khema': _gurung_khema_pattern,

    'Kthi': _kaithi_pattern,
    'Kaithi': _kaithi_pattern,

    'Knda': _kannada_pattern,
    'Kannada': _kannada_pattern,

    'Khar': _kharoshthi_pattern,
    'Kharoshthi': _kharoshthi_pattern,

    'Khoj': _khojki_pattern,
    'Khojki': _khojki_pattern,

    'Krai': _kirat_rai_pattern,
    'Kirat Rai': _kirat_rai_pattern,

    'Sind': _khudawadi_pattern,
    'Khudawadi': _khudawadi_pattern,

    'Lepc': _lepcha_pattern,
    'Lepcha': _lepcha_pattern,

    'Limb': _limbu_pattern,
    'Limbu': _limbu_pattern,

    'Mahj': _mahajani_pattern,
    'Mahajani': _mahajani_pattern,

    'Mlym': _malayalam_pattern,
    'Malayalam': _malayalam_pattern,

    'Gonm': _masaram_gondi_pattern,
    'Masaram Gondi': _masaram_gondi_pattern,

    'Mtei': _meetei_mayek_pattern, # The spelling in Unicode uses 'ee' vs 'ei' in ISO 15924 and common use
    'Meitei Mayek': _meetei_mayek_pattern,

    'Modi': _modi_pattern, # Both code and verbose name are same

    'Mroo': _mro_pattern,
    'Mro': _mro_pattern,

    'Mult': _multani_pattern,
    'Multani': _multani_pattern,

    'Nagm': _nag_mundari_pattern,
    'Nag Mundari': _nag_mundari_pattern,

    'Nand': _nandinagari_pattern,
    'Nandinagari': _nandinagari_pattern,

    'Newa': _newa_pattern, # Both code and verbose name are same

    'Olck': _ol_chiki_pattern,
    'Ol Chiki': _ol_chiki_pattern,

    'Onao': _ol_onal_pattern,
    'Ol Onal': _ol_onal_pattern,

    'Orya': _oriya_pattern,
    'Odia': _oriya_pattern, # Unicode uses both 'Oriya' and 'Odia' while ISO 15924 uses 'Odia' and 'Oriya' is more common

    'Saur': _saurashtra_pattern,
    'Saurashtra': _saurashtra_pattern,

    'Shrd': _sharada_pattern,
    'Sharada': _sharada_pattern,

    'Sidd': _siddham_pattern,
    'Siddham': _siddham_pattern,

    'Sinh': _sinhala_pattern,
    'Sinhala': _sinhala_pattern,

    'Sora': _sora_sompeng_pattern,
    'Sora Sompeng': _sora_sompeng_pattern,

    'Sunu': _sunuwar_pattern,
    'Sunuwar': _sunuwar_pattern,

    'Sylo': _syloti_nagri_pattern,
    'Syloti Nagri': _syloti_nagri_pattern,

    'Takr': _takri_pattern,
    'Takri': _takri_pattern,

    'Taml': _tamil_pattern,
    'Tamil': _tamil_pattern,

    'Telu': _telugu_pattern,
    'Telugu': _telugu_pattern,

    'Thaa': _thaana_pattern,
    'Thaana': _thaana_pattern,

    'Tirh': _tirhuta_pattern,
    'Tirhuta': _tirhuta_pattern,

    'Toto': _toto_pattern, # Both code and verbose name are same

    'Tutg': _tulu_tigalari_pattern,
    'Tulu-Tigalari': _tulu_tigalari_pattern, # ISO 15924 includes the hyphen while Unicode doesn't

    'Wcho': _wancho_pattern,
    'Wancho': _wancho_pattern,

    'Wara': _warang_citi_pattern,
    'Varang Kshiti': _warang_citi_pattern, # The spelling in Unicode uses 'Warang Citi' vs 'Varang Kshiti' in ISO 15924



})

