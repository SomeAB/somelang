"""
Default whitelist of language codes with verbose names.
USE THIS FOR BETTER ACCURACY ON SHORTER TEXT ( text < 100 characters )
"""

# Core python imports
from types import MappingProxyType # For dictionary mutability protection
from typing import Dict # For type hinting

DEFAULT_WHITELIST: frozenset = frozenset([
    # Major European languages
    'eng', # English
    'fra', # French
    'deu', # German
    'ita', # Italian
    'spa', # Spanish
    'por', # Portuguese
    'nld', # Dutch
    'pol', # Polish
    'rus', # Russian
    'ukr', # Ukrainian
    'ces', # Czech
    'hun', # Hungarian
    'ron', # Romanian
    'hrv', # Croatian
    'srp', # Serbian
    'bos', # Bosnian
    'slv', # Slovenian
    'slk', # Slovak
    'bul', # Bulgarian
    'lit', # Lithuanian
    'lvs', # Latvian (variant)
    'ekk', # Estonian (variant)
    'fin', # Finnish
    'swe', # Swedish
    'nob', # Norwegian Bokmal
    'nno', # Norwegian Nynorsk
    'dan', # Danish
    'isl', # Icelandic
    'fao', # Faroese
    'eus', # Basque
    'cat', # Catalan
    'glg', # Galician
    'cos', # Corsican
    'fry', # Frisian
    'ltz', # Luxembourgish
    'gle', # Irish
    'gla', # Scottish Gaelic
    'cym', # Welsh
    'mlt', # Maltese
    'bel', # Belarusian
    'hsb', # Upper Sorbian
    'lad', # Ladino (Judeo-Spanish)

    # Major Asian languages (including Eastern languages without trigram data)
    'arb', # Arabic (standard)
    'heb', # Hebrew
    'tur', # Turkish
    'azb', # Azerbaijani (South)
    'azj', # Azerbaijani (North)
    'kaz', # Kazakh
    'kir', # Kyrgyz
    'tuk', # Turkmen
    'tgk', # Tajik
    'prs', # Dari
    'pes', # Persian (Farsi)
    'urd', # Urdu
    'hin', # Hindi
    'mar', # Marathi
    'bod', # Tibetan
    'uig', # Uyghur
    'ind', # Indonesian
    'jav', # Javanese
    'sun', # Sundanese
    'mad', # Madurese
    'ban', # Balinese
    'ace', # Acehnese
    'vie', # Vietnamese
    'tgl', # Tagalog
    'ceb', # Cebuano
    'hil', # Hiligaynon
    'pam', # Kapampangan (Pampanga)
    'ilo', # Ilocano
    'mya', # Burmese
    'amh', # Amharic
    'tir', # Tigrinya
    'cmn', # Mandarin Chinese
    'jpn', # Japanese
    'kor', # Korean

    # Major African languages
    'hau', # Hausa
    'yor', # Yoruba
    'ibo', # Igbo
    'swh', # Swahili
    'zul', # Zulu
    'xho', # Xhosa
    'afr', # Afrikaans
    'nso', # Northern Sotho (Sepedi)
    'ven', # Venda
    'ssw', # Swazi (Swati)
    'nbl', # Ndebele
    'run', # Kirundi (Rundi)
    'kin', # Kinyarwanda
    'men', # Mende
    'tem', # Temne
    'kri', # Krio
    'pcm', # Nigerian Pidgin
    'ewe', # Ewe
    'gaa', # Ga
    'mos', # Mossi (Moor)
    'sna', # Shona
    'nya', # Nyanja (Chichewa)
    'loz', # Lozi
    'ndo', # Ndonga
    'suk', # Sukuma
    'tiv', # Tiv
    'srr', # Serer
    'dyu', # Dyula (Jula)
    'bam', # Bambara
    'fon', # Fon
    'fat', # Fante
    'dag', # Dagbani

    # Major American languages
    'que', # Quechua
    'quc', # K'iche'
    'qug', # Quichua (variant)
    'quy', # Quechua (variant)
    'quz', # Quechua (Cusco)
    'nav', # Navajo
    'cak', # Kaqchikel
    'mam', # Mam
    'kek', # Q'eqchi'
    'tzm', # Central Atlas Tamazight
    'arn', # Mapudungun (Mapuche)
    'auc', # Awajun / Waorani (approx.)
    'cab', # Cabecar (Cabecar)
    'cof', # Cofan (Cofan / Cofan)
    'maz', # Mazatec
    'ote', # Mezquital Otomi
    'guc', # Wayuu

    # Pacific and other major languages
    'haw', # Hawaiian
    'fij', # Fijian
    'ton', # Tongan
    'rar', # Rarotongan (Cook Islands Maori)
    'pau', # Palauan
    'pon', # Pohnpeian
    'yap', # Yapese
    'bis', # Bislama
    'niu', # Niuean
    'tah', # Tahitian

    # Additional important/classical languages
    'lat', # Latin
    'san', # Sanskrit
    'ido', # Ido

    # Regional languages with significant populations (only with trigram data)
    'aar', # Afar
    'khk', # Khakas
    'sah', # Yakut (Sakha)
    'evn', # Even
    'chv', # Chuvash
    'koi', # Komi-Permyak / Komi
    'krl', # Karelian
    'crh', # Crimean Tatar
    'gag', # Gagauz
    'kaa', # Karakalpak
    'tyv', # Tuvinian
    'alt', # Altai
    'niv', # Nivkh
    'oss', # Ossetian
    'kbd', # Kabardian (Kabardino-Circassian)
    'ady', # Adyghe
    'abk', # Abkhaz
    'gsw', # Swiss German (Alemannic)
    'wln', # Walloon
    'rup', # Aromanian
])

# Mapping of language codes to verbose names (only supported languages)
LANGUAGE_CODE_TO_NAME: Dict[str, str] = MappingProxyType({
    'ace': 'Achinese',
    'acm': 'Mesopotamian Arabic',
    'acq': 'Ta\'izzi-Adeni Arabic',
    'aeb': 'Tunisian Arabic',
    'afr': 'Afrikaans',
    'als': 'Tosk Albanian',
    'amh': 'Amharic',
    'apc': 'North Levantine Arabic',
    'arb': 'Standard Arabic',
    'ars': 'Najdi Arabic',
    'ary': 'Moroccan Arabic',
    'arz': 'Egyptian Arabic',
    'asm': 'Assamese',
    'ast': 'Asturian',
    'awa': 'Awadhi',
    'ayr': 'Central Aymara',
    'azb': 'South Azerbaijani',
    'azj': 'North Azerbaijani',
    'bak': 'Bashkir',
    'bam': 'Bambara',
    'ban': 'Balinese',
    'bel': 'Belarusian',
    'bem': 'Bemba (Zambia)',
    'ben': 'Bengali',
    'bho': 'Bhojpuri',
    'bjn': 'Banjar',
    'bod': 'Tibetan',
    'bos': 'Bosnian',
    'bug': 'Buginese',
    'bul': 'Bulgarian',
    'cat': 'Catalan',
    'ceb': 'Cebuano',
    'ces': 'Czech',
    'cjk': 'Chokwe',
    'ckb': 'Central Kurdish',
    'cmn': 'Mandarin Chinese',
    'crh': 'Crimean Tatar',
    'cym': 'Welsh',
    'dan': 'Danish',
    'deu': 'German',
    'dik': 'Southwestern Dinka',
    'dyu': 'Dyula',
    'dzo': 'Dzongkha',
    'ekk': 'Standard Estonian',
    'ell': 'Modern Greek (1453-)',
    'eng': 'English',
    'epo': 'Esperanto',
    'eus': 'Basque',
    'ewe': 'Ewe',
    'fao': 'Faroese',
    'fij': 'Fijian',
    'fil': 'Filipino',
    'fin': 'Finnish',
    'fon': 'Fon',
    'fra': 'French',
    'fur': 'Friulian',
    'fuv': 'Nigerian Fulfulde',
    'gaz': 'West Central Oromo',
    'gla': 'Scottish Gaelic',
    'gle': 'Irish',
    'glg': 'Galician',
    'gug': 'Paraguayan Guaraní',
    'guj': 'Gujarati',
    'hat': 'Haitian',
    'hau': 'Hausa',
    'heb': 'Hebrew',
    'hin': 'Hindi',
    'hne': 'Chhattisgarhi',
    'hrv': 'Croatian',
    'hun': 'Hungarian',
    'hye': 'Armenian',
    'ibo': 'Igbo',
    'ilo': 'Iloko',
    'ind': 'Indonesian',
    'isl': 'Icelandic',
    'ita': 'Italian',
    'jav': 'Javanese',
    'jpn': 'Japanese',
    'kab': 'Kabyle',
    'kac': 'Kachin',
    'kam': 'Kamba (Kenya)',
    'kan': 'Kannada',
    'kas': 'Kashmiri',
    'kat': 'Georgian',
    'kaz': 'Kazakh',
    'kbp': 'Kabiyè',
    'kea': 'Kabuverdianu',
    'khk': 'Halh Mongolian',
    'khm': 'Khmer',
    'kik': 'Kikuyu',
    'kin': 'Kinyarwanda',
    'kir': 'Kirghiz',
    'kmb': 'Kimbundu',
    'kmr': 'Northern Kurdish',
    'knc': 'Central Kanuri',
    'kor': 'Korean',
    'ktu': 'Kituba (Democratic Republic of Congo)',
    'lao': 'Lao',
    'lij': 'Ligurian',
    'lim': 'Limburgan',
    'lin': 'Lingala',
    'lit': 'Lithuanian',
    'lmo': 'Lombard',
    'ltg': 'Latgalian',
    'ltz': 'Luxembourgish',
    'lua': 'Luba-Lulua',
    'lug': 'Ganda',
    'luo': 'Luo (Kenya and Tanzania)',
    'lus': 'Lushai',
    'lvs': 'Standard Latvian',
    'mag': 'Magahi',
    'mai': 'Maithili',
    'mal': 'Malayalam',
    'mar': 'Marathi',
    'min': 'Minangkabau',
    'mkd': 'Macedonian',
    'mlt': 'Maltese',
    'mni': 'Manipuri',
    'mos': 'Mossi',
    'mri': 'Maori',
    'mya': 'Burmese',
    'nld': 'Dutch',
    'nno': 'Norwegian Nynorsk',
    'nob': 'Norwegian Bokmål',
    'npi': 'Nepali (individual language)',
    'nso': 'Pedi',
    'nus': 'Nuer',
    'nya': 'Nyanja',
    'oci': 'Occitan (post 1500)',
    'ory': 'Odia',
    'pag': 'Pangasinan',
    'pan': 'Panjabi',
    'pap': 'Papiamento',
    'pbt': 'Southern Pashto',
    'pes': 'Iranian Persian',
    'plt': 'Plateau Malagasy',
    'pol': 'Polish',
    'por': 'Portuguese',
    'prs': 'Dari',
    'quy': 'Ayacucho Quechua',
    'ron': 'Romanian',
    'run': 'Rundi',
    'rus': 'Russian',
    'sag': 'Sango',
    'san': 'Sanskrit',
    'sat': 'Santali',
    'scn': 'Sicilian',
    'shn': 'Shan',
    'sin': 'Sinhala',
    'slk': 'Slovak',
    'slv': 'Slovenian',
    'smo': 'Samoan',
    'sna': 'Shona',
    'snd': 'Sindhi',
    'som': 'Somali',
    'sot': 'Southern Sotho',
    'spa': 'Spanish',
    'srd': 'Sardinian',
    'srp': 'Serbian',
    'ssw': 'Swati',
    'sun': 'Sundanese',
    'swe': 'Swedish',
    'swh': 'Swahili (individual language)',
    'szl': 'Silesian',
    'tam': 'Tamil',
    'taq': 'Tamasheq',
    'tat': 'Tatar',
    'tel': 'Telugu',
    'tgk': 'Tajik',
    'tha': 'Thai',
    'tir': 'Tigrinya',
    'tpi': 'Tok Pisin',
    'tsn': 'Tswana',
    'tso': 'Tsonga',
    'tuk': 'Turkmen',
    'tum': 'Tumbuka',
    'tur': 'Turkish',
    'twi': 'Twi',
    'uig': 'Uighur',
    'ukr': 'Ukrainian',
    'umb': 'Umbundu',
    'urd': 'Urdu',
    'uzn': 'Northern Uzbek',
    'vec': 'Venetian',
    'vie': 'Vietnamese',
    'war': 'Waray (Philippines)',
    'wol': 'Wolof',
    'xho': 'Xhosa',
    'ydd': 'Eastern Yiddish',
    'yor': 'Yoruba',
    'yue': 'Yue Chinese',
    'zgh': 'Standard Moroccan Tamazight',
    'zsm': 'Standard Malay',
    'zul': 'Zulu'
})
