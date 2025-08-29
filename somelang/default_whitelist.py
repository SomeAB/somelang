"""
Default whitelist of language codes with verbose names.
USE THIS FOR BETTER ACCURACY ON SHORTER TEXT ( text < 100 characters )
"""

DEFAULT_WHITELIST = [
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
    'ast', # Asturian
    'cos', # Corsican
    'vec', # Venetian
    'lij', # Ligurian
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
    'min', # Minangkabau
    'bug', # Buginese
    'ban', # Balinese
    'ace', # Acehnese
    'vie', # Vietnamese
    'tgl', # Tagalog
    'ceb', # Cebuano
    'hil', # Hiligaynon
    'war', # Waray
    'pam', # Kapampangan (Pampanga)
    'ilo', # Ilocano
    'mya', # Burmese
    'amh', # Amharic
    'tir', # Tigrinya
    'cmn', # Mandarin Chinese
    'jpn', # Japanese
    'kor', # Korean

    # Major African languages
    'som', # Somali
    'hau', # Hausa
    'fuv', # Fula / Fulfulde
    'yor', # Yoruba
    'ibo', # Igbo
    'swh', # Swahili
    'zul', # Zulu
    'xho', # Xhosa
    'afr', # Afrikaans
    'nso', # Northern Sotho (Sepedi)
    'tsn', # Tswana
    'ven', # Venda
    'ssw', # Swazi (Swati)
    'nbl', # Ndebele
    'run', # Kirundi (Rundi)
    'kin', # Kinyarwanda
    'lug', # Luganda
    'lin', # Lingala
    'wol', # Wolof
    'men', # Mende
    'tem', # Temne
    'kri', # Krio
    'pcm', # Nigerian Pidgin
    'twi', # Twi
    'ewe', # Ewe
    'gaa', # Ga
    'mos', # Mossi (Moor)
    'sna', # Shona
    'nya', # Nyanja (Chichewa)
    'bem', # Bemba
    'loz', # Lozi
    'kmb', # Kimbundu
    'umb', # Umbundu
    'ndo', # Ndonga
    'sag', # Sango
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
    'hat', # Haitian Creole
    'nav', # Navajo
    'cak', # Kaqchikel
    'mam', # Mam
    'kek', # Q'eqchi'
    'tzm', # Central Atlas Tamazight
    'arn', # Mapudungun (Mapuche)
    'auc', # Awajun / Waorani (approx.)
    'gyr', # (unknown / regional) - verify
    'cab', # Cabecar (Cabecar)
    'cof', # Cofan (Cofan / Cofan)
    'pbb', # (unknown) - verify
    'gug', # (unknown / Guarani variant) - verify
    'hus', # (unknown) - verify
    'maz', # Mazatec
    'ote', # (unknown) - verify
    'pap', # Papiamento
    'guc', # Wayuu

    # Pacific and other major languages
    'haw', # Hawaiian
    'smo', # Samoan
    'fij', # Fijian
    'ton', # Tongan
    'rar', # Rarotongan (Cook Islands Maori)
    'pau', # Palauan
    'pon', # Pohnpeian
    'yap', # Yapese
    'bis', # Bislama
    'niu', # Niuean
    'tah', # Tahitian
    'mri', # Maori

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
    'fur', # Friulian
    'gsw', # Swiss German (Alemannic)
    'lij', # Ligurian
    'wln', # Walloon
    'rup', # Aromanian
]
