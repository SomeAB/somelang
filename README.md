# SomeLang

## Natural Language Detection Library

SomeLang is a lightweight and decently accurate natural language detection library. It is designed to be fast, python native, with no external dependencies for the main script, and highly customizable with support for whitelists and blacklists.

## Installation

```bash
pip install somelang
```

## Features

- **Fast Natural Language Detection** - Trigrams-based approach for accurate results
- **Default 158+ language whitelist** - The default whitelist provides better accuracy on short texts (3-100 characters)
- **Supports 194+ languages** - Can detect a wide range of languages in full mode
- **Modern Training Data** - Trained on OpenLID-v2 & many other modern datasets
- **Python-native** - No external dependencies for main script
- **Customizable** - Configurable whitelist/blacklist support

## Usage

### Basic Detection
```python
from somelang import somelang

# Basic language detection
lang = somelang("Bonjour tout le monde")  # Returns: 'fra'

# Get language name instead of code
lang = somelang("Hello world", verbose=True)  # Returns: 'English'
```

### Command Line
```python
python -m somelang 'text to analyze'
```

### Advanced Usage
```python

from somelang import somelang_all, somelang_no_whitelist

# Get all probable languages with confidence scores
results = somelang_all("Hello world")  # Returns: [['eng', 1.0], ...]

# Use all 194 languages (no whitelist)
lang = somelang_no_whitelist("Text in rare language")
```

### Note
```
Currently, the library expects a minimum text length of 10 characters, but due to the current trigram-based approach, it may give a false positive on less than 100 character texts. This will be remedied in future updates.
```

## Citations 
Trained mainly on the [OpenLID-v2 dataset](https://huggingface.co/datasets/laurievb/OpenLID-v2) and a few other datasets (for refinement). 

Inspired by [franc](https://github.com/wooorm/franc) by [Titus Wormer](https://github.com/wooorm).

See [CITATIONS](./CITATIONS.md) file for more details.

## License
This project is licensed under the [MIT](./LICENSE) license. Authored by [SomeAB](https://github.com/SomeAB).

