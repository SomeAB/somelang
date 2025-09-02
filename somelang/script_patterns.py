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

_thai_pattern = re.compile(r'[\u0E00-\u0E7F]')

_ethiopic_pattern = re.compile(r'[\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2F\U0001E7E0-\U0001E7FF]')

_myanmar_pattern = re.compile(r'[\u1000-\u109F\uAA60-\uAA7F\uA9E0-\uA9FF\U000116D0-\U000116FF]')

_khmer_pattern = re.compile(r'[\u1780-\u17FF\u19E0-\u19FF]')

_greek_pattern = re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF\U00010140-\U0001018F]')

_hebrew_pattern = re.compile(r'[\u0590-\u05FF\uFB00-\uFB4F]')

_lao_pattern = re.compile(r'[\u0E80-\u0EFF]')

_tibetan_pattern = re.compile(r'[\u0F00-\u0FFF]')

_armenian_pattern = re.compile(r'[\u0530-\u058F\uFB00-\uFB4F]')

_mongolian_pattern = re.compile(r'[\u1800-\u18AF\U00011660-\U0001167F]')

_georgian_pattern = re.compile(r'[\u10A0-\u10FF\u1C90-\u1CBF\u2D00-\u2D2F]')

_tifinagh_pattern = re.compile(r'[\u2D30-\u2D7F]')

_unified_canadian_aboriginal_syllabics_pattern = re.compile(r'[\u1400-\u167F\u18B0-\u18FF\U00011AB0-\U00011ABF]')

_javanese_pattern = re.compile(r'[\uA980-\uA9DF]')

_balinese_pattern = re.compile(r'[\u1B00-\u1B7F]')

_sundanese_pattern = re.compile(r'[\u1B80-\u1BBF\u1CC0-\u1CCF]')

_yi_pattern = re.compile(r'[\uA000-\uA48F\uA490-\uA4CF]')

_syriac_pattern = re.compile(r'[\u0700-\u074F\u0860-\u086F]')

_vai_pattern = re.compile(r'[\uA500-\uA63F]')

_cherokee_pattern = re.compile(r'[\u13A0-\u13FF\uAB70-\uABBF]')

_tai_tham_pattern = re.compile(r'[\u1A20-\u1AAF]')

_tai_viet_pattern = re.compile(r'[\uAA80-\uAADF]')

_nko_pattern = re.compile(r'[\u07C0-\u07FF]')

_adlam_pattern = re.compile(r'[\U0001E900-\U0001E95F]')

_bamum_pattern = re.compile(r'[\uA6A0-\uA6FF\U00016800-\U00016A3F]')

_hanifi_rohingya_pattern = re.compile(r'[\U00010D00-\U00010D3F]')

_cham_pattern = re.compile(r'[\uAA00-\uAA5F]')

_kayah_li_pattern = re.compile(r'[\uA900-\uA92F]')

_batak_pattern = re.compile(r'[\u1BC0-\u1BFF]')

_buginese_pattern = re.compile(r'[\u1A00-\u1A1F]')

_tagalog_pattern = re.compile(r'[\u1700-\u171F]')

_buhid_pattern = re.compile(r'[\u1740-\u175F]')

_hanunoo_pattern = re.compile(r'[\u1720-\u173F]')

_rejang_pattern = re.compile(r'[\uA930-\uA95F]')

_tagbanwa_pattern = re.compile(r'[\u1760-\u177F]')

_bopomofo_pattern = re.compile(r'[\u3100-\u312F]')

_lisu_pattern = re.compile(r'[\uA4D0-\uA4FF\U00011FB0-\U00011FBF]')

_miao_pattern = re.compile(r'[\U00016F00-\U00016F9F]')

_osage_pattern = re.compile(r'[\U000104B0-\U000104FF]')

_bassa_vah_pattern = re.compile(r'[\U00016AD0-\U00016AFF]')

_coptic_pattern = re.compile(r'[\u2C80-\u2CFF\u0370-\u03FF\U000102E0-\U000102FF]')

_braille_pattern = re.compile(r'[\u2800-\u28FF]')

_tai_le_pattern = re.compile(r'[\u1950-\u197F]')

_new_tai_lue_pattern = re.compile(r'[\u1980-\u19DF]')

_tangsa_pattern = re.compile(r'[\U00016A70-\U00016ACF]')

_makasar_pattern = re.compile(r'[\U00011EE0-\U00011EFF]')

_mende_kikakui_pattern = re.compile(r'[\U0001E800-\U0001E8DF]')



# Next we map script names (both code & verbose name per ISO 15924) to the regex patterns
# In order of most widely used script first (roughly)
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

    # The spelling in Unicode uses 'ee' vs 'ei' in ISO 15924 and common use
    
    'Mtei': _meetei_mayek_pattern,
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

    # Unicode uses both 'Oriya' and 'Odia' while ISO 15924 uses 'Odia' and 'Oriya' is more common
    
    'Orya': _oriya_pattern,
    'Odia': _oriya_pattern,

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

    # ISO 15924 includes the hyphen while Unicode doesn't in 'Tulu Tigalari'
    
    'Tutg': _tulu_tigalari_pattern,
    'Tulu-Tigalari': _tulu_tigalari_pattern,

    'Wcho': _wancho_pattern,
    'Wancho': _wancho_pattern,

    # The spelling in Unicode uses 'Warang Citi' vs 'Varang Kshiti' in ISO 15924

    'Wara': _warang_citi_pattern,
    'Varang Kshiti': _warang_citi_pattern,

    # Indic Scripts Group ENDS above

    'Thai': _thai_pattern, # Both code and verbose name are same

    'Ethi': _ethiopic_pattern,
    'Ethiopic': _ethiopic_pattern,

    'Mymr': _myanmar_pattern,
    'Myanmar': _myanmar_pattern,

    'Khmr': _khmer_pattern,
    'Khmer': _khmer_pattern,

    'Grek': _greek_pattern,
    'Greek': _greek_pattern,

    'Hebr': _hebrew_pattern,
    'Hebrew': _hebrew_pattern,

    # ISO 15924 code for Lao is 'Laoo' with the extra 'o'
    
    'Laoo': _lao_pattern, 
    'Lao': _lao_pattern,

    'Tibt': _tibetan_pattern,
    'Tibetan': _tibetan_pattern,

    'Armn': _armenian_pattern,
    'Armenian': _armenian_pattern,

    'Mong': _mongolian_pattern,
    'Mongolian': _mongolian_pattern,

    # Didn't add 'Geok' aka 'Georgian Khutsuri' separately as Georgian contains it
    
    'Geor': _georgian_pattern,
    'Georgian': _georgian_pattern,

    'Tfng': _tifinagh_pattern,
    'Tifinagh': _tifinagh_pattern,

    # This is the longest verbose name in ISO 15924

    'Cans': _unified_canadian_aboriginal_syllabics_pattern,
    'Unified Canadian Aboriginal Syllabics': _unified_canadian_aboriginal_syllabics_pattern,

    'Java': _javanese_pattern,
    'Javanese': _javanese_pattern,

    'Bali': _balinese_pattern,
    'Balinese': _balinese_pattern,

    'Sund': _sundanese_pattern,
    'Sundanese': _sundanese_pattern,

    'Yiii': _yi_pattern,
    'Yi': _yi_pattern,

    # Didn't add 3 sub variants for syriac separately yet
    
    'Syrc': _syriac_pattern,
    'Syriac': _syriac_pattern,

    'Vaii': _vai_pattern,
    'Vai': _vai_pattern,

    'Cher': _cherokee_pattern,
    'Cherokee': _cherokee_pattern,

    # Unicode uses the name 'Tai Tham' vs 'Lanna' in ISO 15924

    'Lana': _tai_tham_pattern,
    'Lanna': _tai_tham_pattern,

    'Tavt': _tai_viet_pattern,
    'Tai Viet': _tai_viet_pattern,

    # Unicode uses the name 'Nko' vs 'N'Ko' in ISO 15924. Used 'Right Single Quotation Mark' instead of apostrophe for avoiding syntax issues

    'Nkoo': _nko_pattern,
    'N’Ko': _nko_pattern,

    'Adlm': _adlam_pattern,
    'Adlam': _adlam_pattern,

    'Bamu': _bamum_pattern,
    'Bamum': _bamum_pattern,

    # Unicode uses the name 'Hanifi Rohingya' vs only 'Hanifi' in ISO 15924

    'Rohg': _hanifi_rohingya_pattern,
    'Hanifi': _hanifi_rohingya_pattern,

    'Cham': _cham_pattern, # Both the code and verbose name are same

    'Kali': _kayah_li_pattern,
    'Kayah Li': _kayah_li_pattern,

    'Batk': _batak_pattern,
    'Batak': _batak_pattern,

    'Bugi': _buginese_pattern,
    'Buginese': _buginese_pattern,

    # Filipino is written mostly in Latin script but also in 'Baybayin' known as 'Tagalog'

    'Tglg': _tagalog_pattern,
    'Tagalog': _tagalog_pattern,

    'Buhd': _buhid_pattern,
    'Buhid': _buhid_pattern,

    'Hano': _hanunoo_pattern,
    'Hanunoo': _hanunoo_pattern,

    'Rjng': _rejang_pattern,
    'Rejang': _rejang_pattern,

    'Tagb': _tagbanwa_pattern,
    'Tagbanwa': _tagbanwa_pattern,

    'Bopo': _bopomofo_pattern,
    'Bopomofo': _bopomofo_pattern,

    'Lisu': _lisu_pattern,
    'Fraser': _lisu_pattern,

    # Created by Samuel Pollard, used by Chinese Minorities

    'Plrd': _miao_pattern,
    'Pollard Phonetic': _miao_pattern,

    'Osge': _osage_pattern,
    'Osage': _osage_pattern,

    'Bass': _bassa_vah_pattern,
    'Bassa Vah': _bassa_vah_pattern,

    'Copt': _coptic_pattern,
    'Coptic': _coptic_pattern,

    'Brai': _braille_pattern,
    'Braille': _braille_pattern,

    'Tale': _tai_le_pattern,
    'Tai Le': _tai_le_pattern,

    'Talu': _new_tai_lue_pattern,
    'New Tai Lue': _new_tai_lue_pattern,

    'Tnsa': _tangsa_pattern,
    'Tangsa': _tangsa_pattern,

    'Maka': _makasar_pattern,
    'Makasar': _makasar_pattern,

    # Unicode uses the name 'Mende Kikakui' vs only 'Mende' in ISO 15924

    'Mend': _mende_kikakui_pattern,
    'Mende': _mende_kikakui_pattern

})

