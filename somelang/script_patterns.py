"""
This file contains the comprehensive script detection patterns for various scripts standardized in both Unicode and ISO 15924
Unicode version: 16.0
"""

# Core python imports
import re # For regular patterns
from types import MappingProxyType # For dictionary mutability protection
from typing import Dict, Mapping # For type hinting

# First we map script names (both code & verbose name per ISO 15924) to the regex patterns
# Each regex matches characters specific to a script
# Pre-compiled regex patterns are faster then recompiling on each use
# We are using proper unicode blocks for safety & predictability
# In order of most widely used script first (roughly)
# We use Mapping from typing module for type hinting
# We use MappingProxyType for mutability protection

ALL_SCRIPT_PATTERNS: Mapping[str, re.Pattern] = MappingProxyType({
    
    'Latn': re.compile(r'[A-Za-z\u00AA\u00BA\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF\u0100-\u017F\u0180-\u024F\u2C60-\u2C7F\uA720-\uA7FF\uAB30-\uAB6F\u1E00-\u1EFF\uFB00-\uFB06\u0250-\u02AF\u1D00-\u1D7F\u1D80-\u1DBF]'),

    # Chinese Script Group
    
    'Hant': re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF]'),

    'Hans': re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF]'),

    'Arab': re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\u0870-\u089F\uFB50-\uFDFF\uFE70-\uFEFF]'),

    'Deva': re.compile(r'[\u0900-\u097F\uA8E0-\uA8FF\U00011B00-\U00011B5F\u1CD0-\u1CFF]'),

    'Cyrl': re.compile(r'[\u0400-\u04FF\u0500-\u052F\u2DE0-\u2DFF\uA640-\uA69F\u1C80-\u1C8F]'),

    'Beng': re.compile(r'[\u0980-\u09FF]'),

    # Japanese Script Group

    'Jpan': re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF\u3040-\u309F\U0001B100-\U0001B12F\U0001AFF0-\U0001AFFF\U0001B000-\U0001B0FF\U0001B130-\U0001B16F\u3190-\u319F\u30A0-\u30FF\u31F0-\u31FF\uFF00-\uFFEF]'),

    'Hrkt': re.compile(r'[\u3040-\u309F\U0001B100-\U0001B12F\U0001AFF0-\U0001AFFF\U0001B000-\U0001B0FF\U0001B130-\U0001B16F\u30A0-\u30FF\u31F0-\u31FF\uFF00-\uFFEF]'),

    'Hira': re.compile(r'[\u3040-\u309F]'),

    'Kana': re.compile(r'[\U0001B100-\U0001B12F\U0001AFF0-\U0001AFFF\U0001B000-\U0001B0FF\U0001B130-\U0001B16F\u30A0-\u30FF\u31F0-\u31FF\uFF00-\uFFEF]'),

    # Korean Script Group

    'Kore': re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF\u2F00-\u2FDF\u2E80-\u2EFF\u31C0-\u31EF\U00020000-\U0002A6DF\u1100-\u11FF\uA960-\uA97F\uD7B0-\uD7FF\u3130-\u318F\uFF00-\uFFEF\uAC00-\uD7AF]'),

    'Hang': re.compile(r'[\u1100-\u11FF\uA960-\uA97F\uD7B0-\uD7FF\u3130-\u318F\uFF00-\uFFEF\uAC00-\uD7AF]'),

    # Indic Script Group

    'Ahom': re.compile(r'[\U00011700-\U0001174F]'),

    'Bhks': re.compile(r'[\U00011C00-\U00011C6F]'),

    'Brah': re.compile(r'[\U00011000-\U0001107F]'),

    'Cakm': re.compile(r'[\U00011100-\U0001114F]'),

    'Diak': re.compile(r'[\U00011900-\U0001195F]'),

    'Dogr': re.compile(r'[\U00011800-\U0001184F]'),

    'Gran': re.compile(r'[\U00011300-\U0001137F]'),

    'Gujr': re.compile(r'[\u0A80-\u0AFF]'),

    'Gong': re.compile(r'[\U00011D60-\U00011DAF]'),

    'Guru': re.compile(r'[\u0A00-\u0A7F]'),

    'Gukh': re.compile(r'[\U00016100-\U0001613F]'),

    'Kthi': re.compile(r'[\U00011080-\U000110CF]'),

    'Knda': re.compile(r'[\u0C80-\u0CFF]'),

    'Khar': re.compile(r'[\U00010A00-\U00010A5F]'),

    'Khoj': re.compile(r'[\U00011200-\U0001124F]'),

    'Krai': re.compile(r'[\U00016D40-\U00016D7F]'),

    'Sind': re.compile(r'[\U000112B0-\U000112FF]'),

    'Lepc': re.compile(r'[\u1C00-\u1C4F]'),

    'Limb': re.compile(r'[\u1900-\u194F]'),

    'Mahj': re.compile(r'[\U00011150-\U0001117F]'),

    'Mlym': re.compile(r'[\u0D00-\u0D7F]'),

    'Gonm': re.compile(r'[\U00011D00-\U00011D5F]'),

    'Mtei': re.compile(r'[\uABC0-\uABFF\uAAE0-\uAAFF]'),

    'Modi': re.compile(r'[\U00011600-\U0001165F]'),

    'Mroo': re.compile(r'[\U00016A40-\U00016A6F]'),

    'Mult': re.compile(r'[\U00011280-\U000112AF]'),

    'Nagm': re.compile(r'[\U0001E4D0-\U0001E4FF]'),

    'Nand': re.compile(r'[\U000119A0-\U000119FF]'),

    'Newa': re.compile(r'[\U00011400-\U0001147F]'),

    'Olck': re.compile(r'[\u1C50-\u1C7F]'),

    'Onao': re.compile(r'[\U0001E5D0-\U0001E5FF]'),

    'Orya': re.compile(r'[\u0B00-\u0B7F]'),

    'Saur': re.compile(r'[\uA880-\uA8DF]'),

    'Shrd': re.compile(r'[\U00011180-\U000111DF]'),

    'Sidd': re.compile(r'[\U00011580-\U000115FF]'),

    'Sinh': re.compile(r'[\u0D80-\u0DFF\U000111E0-\U000111FF]'),

    'Sora': re.compile(r'[\U000110D0-\U000110FF]'),

    'Sunu': re.compile(r'[\U00011BC0-\U00011BFF]'),

    'Sylo': re.compile(r'[\uA800-\uA82F]'),

    'Takr': re.compile(r'[\U00011680-\U000116CF]'),

    'Taml': re.compile(r'[\u0B80-\u0BFF\U00011FC0-\U00011FFF]'),

    'Telu': re.compile(r'[\u0C00-\u0C7F]'),

    'Thaa': re.compile(r'[\u0780-\u07BF]'),

    'Tirh': re.compile(r'[\U00011480-\U000114DF]'),

    'Toto': re.compile(r'[\U0001E290-\U0001E2BF]'),

    'Tutg': re.compile(r'[\U00011380-\U000113FF]'),

    'Wcho': re.compile(r'[\U0001E2C0-\U0001E2FF]'),

    'Wara': re.compile(r'[\U000118A0-\U000118FF]'),

    # Indic Scripts Group ENDS above

    'Thai': re.compile(r'[\u0E00-\u0E7F]'),

    'Ethi': re.compile(r'[\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF\uAB00-\uAB2F\U0001E7E0-\U0001E7FF]'),

    'Mymr': re.compile(r'[\u1000-\u109F\uAA60-\uAA7F\uA9E0-\uA9FF\U000116D0-\U000116FF]'),

    'Khmr': re.compile(r'[\u1780-\u17FF\u19E0-\u19FF]'),

    'Grek': re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF\U00010140-\U0001018F]'),

    'Hebr': re.compile(r'[\u0590-\u05FF\uFB00-\uFB4F]'),
    
    'Laoo': re.compile(r'[\u0E80-\u0EFF]'),

    'Tibt': re.compile(r'[\u0F00-\u0FFF]'),

    'Armn': re.compile(r'[\u0530-\u058F\uFB00-\uFB4F]'),

    'Mong': re.compile(r'[\u1800-\u18AF\U00011660-\U0001167F]'),

    'Geor': re.compile(r'[\u10A0-\u10FF\u1C90-\u1CBF\u2D00-\u2D2F]'),

    'Tfng': re.compile(r'[\u2D30-\u2D7F]'),

    'Cans': re.compile(r'[\u1400-\u167F\u18B0-\u18FF\U00011AB0-\U00011ABF]'),

    'Java': re.compile(r'[\uA980-\uA9DF]'),

    'Bali': re.compile(r'[\u1B00-\u1B7F]'),

    'Sund': re.compile(r'[\u1B80-\u1BBF\u1CC0-\u1CCF]'),

    'Yiii': re.compile(r'[\uA000-\uA48F\uA490-\uA4CF]'),

    'Syrc': re.compile(r'[\u0700-\u074F\u0860-\u086F]'),

    'Vaii': re.compile(r'[\uA500-\uA63F]'),

    'Cher': re.compile(r'[\u13A0-\u13FF\uAB70-\uABBF]'),

    'Lana': re.compile(r'[\u1A20-\u1AAF]'),

    'Tavt': re.compile(r'[\uAA80-\uAADF]'),

    'Nkoo': re.compile(r'[\u07C0-\u07FF]'),

    'Adlm': re.compile(r'[\U0001E900-\U0001E95F]'),

    'Bamu': re.compile(r'[\uA6A0-\uA6FF\U00016800-\U00016A3F]'),

    'Rohg': re.compile(r'[\U00010D00-\U00010D3F]'),

    'Cham': re.compile(r'[\uAA00-\uAA5F]'),

    'Kali': re.compile(r'[\uA900-\uA92F]'),

    'Batk': re.compile(r'[\u1BC0-\u1BFF]'),

    'Bugi': re.compile(r'[\u1A00-\u1A1F]'),

    'Tglg': re.compile(r'[\u1700-\u171F]'),

    'Buhd': re.compile(r'[\u1740-\u175F]'),

    'Hano': re.compile(r'[\u1720-\u173F]'),

    'Rjng': re.compile(r'[\uA930-\uA95F]'),

    'Tagb': re.compile(r'[\u1760-\u177F]'),

    'Bopo': re.compile(r'[\u3100-\u312F]'),

    'Lisu': re.compile(r'[\uA4D0-\uA4FF\U00011FB0-\U00011FBF]'),

    'Plrd': re.compile(r'[\U00016F00-\U00016F9F]'),

    'Osge': re.compile(r'[\U000104B0-\U000104FF]'),

    'Bass': re.compile(r'[\U00016AD0-\U00016AFF]'),

    'Copt': re.compile(r'[\u2C80-\u2CFF\u0370-\u03FF\U000102E0-\U000102FF]'),

    'Brai': re.compile(r'[\u2800-\u28FF]'),

    'Tale': re.compile(r'[\u1950-\u197F]'),

    'Talu': re.compile(r'[\u1980-\u19DF]'),

    'Tnsa': re.compile(r'[\U00016A70-\U00016ACF]'),
    
    'Maka': re.compile(r'[\U00011EE0-\U00011EFF]'),
    
    'Mend': re.compile(r'[\U0001E800-\U0001E8DF]')

})

# Next we map script code to their verbose name (as per ISO 15924)
# Also see the individual comments for extra but useful notes
SCRIPT_CODE_TO_NAME: Mapping[str, str] = MappingProxyType({

    'Latn': 'Latin',
    'Hant': 'Traditional', # Chinese Scripts Group
    'Hans': 'Simplified',
    'Arab': 'Arabic',
    'Deva': 'Devanagari',
    'Cyrl': 'Cyrillic',
    'Beng': 'Bangla',
    'Jpan': 'Japanese', # Japanese Scripts Group
    'Hrkt': 'Japanese syllabaries',
    'Hira': 'Hiragana',
    'Kana': 'Katakana',
    'Kore': 'Korean', # Korean Scripts Group
    'Hang': 'Hangul',
    'Ahom': 'Ahom', # Indic Scripts Group STARTS here. Both code and verbose name are same
    'Bhks': 'Bhaiksuki',
    'Brah': 'Brahmi',
    'Cakm': 'Chakma',
    'Diak': 'Dives Akuru',
    'Dogr': 'Dogra',
    'Gran': 'Grantha',
    'Gujr': 'Gujarati',
    'Gong': 'Gunjala Gondi',
    'Guru': 'Gurmukhi',
    'Gukh': 'Gurung Khema',
    'Kthi': 'Kaithi',
    'Knda': 'Kannada',
    'Khar': 'Kharoshthi',
    'Khoj': 'Khojki',
    'Krai': 'Kirat Rai',
    'Sind': 'Khudawadi',
    'Lepc': 'Lepcha',
    'Limb': 'Limbu',
    'Mahj': 'Mahajani',
    'Mlym': 'Malayalam',
    'Gonm': 'Masaram Gondi',
    'Mtei': 'Meitei Mayek', # The spelling in Unicode uses 'ee' vs 'ei' in ISO 15924 and common use
    'Modi': 'Modi', # Both code and verbose name are same
    'Mroo': 'Mro',
    'Mult': 'Multani',
    'Nagm': 'Nag Mundari',
    'Nand': 'Nandinagari',
    'Newa': 'Newa', # Both code and verbose name are same
    'Olck': 'Ol Chiki',
    'Onao': 'Ol Onal',
    'Orya': 'Odia', # Unicode uses both 'Oriya' and 'Odia' while ISO 15924 uses 'Odia' and 'Oriya' is more common
    'Saur': 'Saurashtra',
    'Shrd': 'Sharada',
    'Sidd': 'Siddham',
    'Sinh': 'Sinhala',
    'Sora': 'Sora Sompeng',
    'Sunu': 'Sunuwar',
    'Sylo': 'Syloti Nagri',
    'Takr': 'Takri',
    'Taml': 'Tamil',
    'Telu': 'Telugu',
    'Thaa': 'Thaana',
    'Tirh': 'Tirhuta',
    'Toto': 'Toto', # Both code and verbose name are same
    'Tutg': 'Tulu-Tigalari', # ISO 15924 includes the hyphen while Unicode doesn't in 'Tulu Tigalari'
    'Wcho': 'Wancho',
    'Wara': 'Varang Kshiti', # Indic Scripts Group ENDS here. The spelling in Unicode uses 'Warang Citi' vs 'Varang Kshiti' in ISO 15924
    'Thai': 'Thai', # Both code and verbose name are same
    'Ethi': 'Ethiopic',
    'Mymr': 'Myanmar',
    'Khmr': 'Khmer',
    'Grek': 'Greek',
    'Hebr': 'Hebrew',
    'Laoo': 'Lao', # ISO 15924 code for Lao is 'Laoo' with the extra 'o'
    'Tibt': 'Tibetan',
    'Armn': 'Armenian',
    'Mong': 'Mongolian',
    'Geor': 'Georgian', # Didn't add 'Geok' aka 'Georgian Khutsuri' separately as Georgian contains it
    'Tfng': 'Tifinagh',
    'Cans': 'Unified Canadian Aboriginal Syllabics', # This is the longest verbose name in ISO 15924
    'Java': 'Javanese',
    'Bali': 'Balinese',
    'Sund': 'Sundanese',
    'Yiii': 'Yi',
    'Syrc': 'Syriac', # Didn't add 3 sub variants due to lack of separated unicode charts for them
    'Vaii': 'Vai',
    'Cher': 'Cherokee',
    'Lana': 'Lanna', # Unicode uses the name 'Tai Tham' vs 'Lanna' in ISO 15924
    'Tavt': 'Tai Viet',
    'Nkoo': 'N’Ko', # Unicode uses the name 'Nko' vs 'N'Ko' in ISO 15924. Used 'Right Single Quotation Mark' instead of apostrophe for avoiding syntax issues
    'Adlm': 'Adlam',
    'Bamu': 'Bamum',
    'Rohg': 'Hanifi', # Unicode uses the name 'Hanifi Rohingya' vs only 'Hanifi' in ISO 15924
    'Cham': 'Cham', # Both the code and verbose name are same
    'Kali': 'Kayah Li',
    'Batk': 'Batak',
    'Bugi': 'Buginese',
    'Tglg': 'Tagalog', # Filipino is written mostly in Latin script but also in 'Baybayin' known as 'Tagalog'
    'Buhd': 'Buhid',
    'Hano': 'Hanunoo',
    'Rjng': 'Rejang',
    'Tagb': 'Tagbanwa',
    'Bopo': 'Bopomofo',
    'Lisu': 'Fraser',
    'Plrd': 'Pollard Phonetic', # Created by Samuel Pollard, used by Chinese Minorities
    'Osge': 'Osage',
    'Bass': 'Bassa Vah',
    'Copt': 'Coptic',
    'Brai': 'Braille',
    'Tale': 'Tai Le',
    'Talu': 'New Tai Lue',
    'Tnsa': 'Tangsa',
    'Maka': 'Makasar',
    'Mend': 'Mende' # Unicode uses the name 'Mende Kikakui' vs only 'Mende' in ISO 15924

}) 