"""
SomeLang Trainer - by SomeAB

This module generates reference trigrams from training data, nicely packaging them into a .py file, in a compatible format for use by main SomeLang functions

"""

# Core python imports
import argparse # For command line argument handling
import glob # For file pattern matching
import os # For file existence checks
import pandas as pd # For reading parquet files easily & data manipulation
from pathlib import Path # For cross platform paths handling
import pyarrow.parquet as pq # For manipulating parquet files
from typing import Dict, List, Tuple, Optional # For type hinting

# Import functions from the main file somelang.py
from .somelang import (
    generate_trigrams_frequency_map
)

# Constants
MAX_TRAINING_FILE_SIZE = 10240 # Maximum file size for training data in MB
REQUIRED_COLUMNS = ['text', 'language', 'script'] # This is the list of expected columns in parquet file. Change these if using a different dataset. Keep first element as text
MIN_TEXT_LENGTH = 3 # Minimum length of the text inside each text column in each row
MAX_TEXT_LENGTH = 2048 # Maximum length of the text inside each text column in each row
SELECTED_TRIGRAMS_COUNT = 300 # Number of most frequent trigrams to select from among the generated trigrams
DEFAULT_OUTPUT_DIR = Path('trigrams_data') # Default output directory for the generated trigram files if no output path is provided
DEFAULT_INPUT_DIR = Path('training_data') # Default input directory for the training data files if no input path is provided
OUTPUT_FILE_PREFIX = 'trigrams_data' # Default prefix for the output trigram files
INPUT_FILE_PREFIX = 'training_data' # Default prefix for the input training data files

def split_training_data(file_path: Path = DEFAULT_INPUT_DIR, max_size_mb: int = MAX_TRAINING_FILE_SIZE) -> pd.DataFrame:
    """Convert large parquet files into manageable batches"""
    
    # 1. Use Path.stat and st_size to get file size in bytes
    total_size_bytes = file_path.stat().st_size
    batch_size_bytes = max_size_mb * (1024**2)  # Convert MB to bytes

    # 2. Using pandas, read a small sample (1000 rows)
    sample_df_01 = pd.read_parquet(file_path, engine='pyarrow').head(1000)

    # 3. Measure the memory usage of 1000 rows that are already loaded, then divide it by no of rows, to get estimated memory usage per row
    estimated_row_size = sample_df_01.memory_usage(deep=True).sum() / len(sample_df_01)

    # 4. Calculate approximate no of rows per batch 
    rows_per_batch = int(batch_size_bytes / estimated_row_size)

    # 5. Print a message indicating how many rows will be processed in each batch
    print(f"Processing in batches of ~{rows_per_batch:,} rows")
    
    # 6. Use pyarrow's batch reading capability
    # More efficient, as it is C++ under the hood, & doesn't load the entire file into memory
    training_file = pq.ParquetFile(file_path)
    batches = []
    
    # 7. Iterate through the training file, splitting it into 'rows_per_batch' sized batches
    for single_batch in training_file.iter_batches(batch_size=rows_per_batch):
        
        # Convert the single batch to pandas dataframe
        batch_df = single_batch.to_pandas()

        # Append each dataframe to the list 'batches'
        batches.append(batch_df)

        # Print the progress, for easy debugging
        print(f"Loaded batch: {len(batch_df):,} rows")
    
    # 8. Combine all batches
    print("Combining batches...")
    return pd.concat(batches, ignore_index=True) 

def load_training_data(file_path: Path = DEFAULT_INPUT_DIR, min_text_len: Optional[int] = MIN_TEXT_LENGTH, max_text_len: Optional[int] = MAX_TEXT_LENGTH) -> Dict[Tuple[str, str], pd.DataFrame]:
    """Handle the incoming training data file"""

    # 1. Validate file exists using Pathlib
    # If the provided file_path is actually a file, then use it as it is
    if file_path.is_file():
        actual_file_path = file_path
    # Else if, the provided file_path is a folder, then look into it
    elif file_path.is_dir():
        # Find files with the given filename prefix and add to a list (to handle when multiple files are found)
        training_files = list(file_path.glob(f"{INPUT_FILE_PREFIX}_*.parquet"))
        # If no files are found, raise error
        if not training_files:
            raise FileNotFoundError(f"No {INPUT_FILE_PREFIX}_*.parquet files found in {file_path}")
        # Use the first file as input
        actual_file_path = training_files[0]
        # If more than one file found, inform that we are using the first file, and how many files we found
        if len(training_files) > 1:
            print(f"Using {actual_file_path.name} (found {len(training_files)} files)")
    # If the provided file_path is neither a file or folder, raise an error
    else:
        raise FileNotFoundError(f"No supported file or folder found: {file_path}")
    
    # 2. Use Path.stat and st_size to get file size in bytes
    file_size_bytes = actual_file_path.stat().st_size

    # 3. Convert the file size from bytes to MB
    file_size_mb = file_size_bytes / (1024**2)

    # 4. If the file is above the limit, split it into smaller batches
    # In both cases, we get a dataframe, stored in 'df_main'
    if file_size_mb > MAX_TRAINING_FILE_SIZE:
        print(f"File size exceeds {MAX_TRAINING_FILE_SIZE}MB limit. Loading in batches...")
        df_main = split_training_data(actual_file_path, MAX_TRAINING_FILE_SIZE)
    else:
        print("File size is within limits. Loading the entire file into memory...")
        df_main = pd.read_parquet(actual_file_path)

    # 5. Check if the dataframe is empty
    if df_main.empty:
        raise ValueError("Training data file is empty")
    
    # 6. Print information about rows & columns
    print(f"Loaded Dataframe Successfully with {df_main.shape[0]:,} rows and {df_main.shape[1]} columns")

    # 7. Validate column structure
    # Find which columns are missing
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df_main.columns]

    # Raise an error if any required columns are missing and also show found columns
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}. Found columns: {list(df_main.columns)}")
    
    # 8. Remove rows with null, empty text or less then 3 characters (enough for one trigram)
    text_column = REQUIRED_COLUMNS[0] # Using the first element of the list, which will be manually assured by devs to be input text (name agnostic)
    initial_row_count = df_main.shape[0] # Use pandas method to get no of rows (faster)

    # Get the length of the text data, after striping whitespace on both ends and converting null to NaN
    text_data_length = df_main[text_column].str.strip().str.len()

    # Use pandas 'between' method to remove entries that are outside the range
    df_main = df_main[text_data_length.between(min_text_len, max_text_len, inclusive='both')]

    # Report the number of rows dropped
    if df_main.shape[0] < initial_row_count:
        dropped_count = initial_row_count - df_main.shape[0] # Get no of dropped rows by substracting current count from initial count
        print(f"Removed {dropped_count:,} rows with invalid {text_column} (null, empty, or outside {min_text_len}-{max_text_len} char range). Remaining: {df_main.shape[0]:,} rows")

    # 9. Ensure we still have data after filtering
    if df_main.empty:
        raise ValueError(f"No valid training data remaining after filtering for null, empty, too short and too long text")

    # 10. Use a single 'groupby' operation to get both stats and separated dataframes
    # First group by script and language (unique together)
    grouped_data = df_main.groupby(['script', 'language'])

    # Use grouped_data to get stats. Get count and average for the text column, then round it to 2 decimal places
    combo_stats = grouped_data.agg({
        text_column: ['count', lambda x: x.str.len().mean()]
    }).round(2)

    separated_df = {key: group for key, group in grouped_data}

    # Rename columns in combo_stats for clarity
    combo_stats.columns = ['count', 'avg_length']

    # Sort further for nicer presentation
    combo_stats = combo_stats.sort_values('count', ascending=False)

    # Get total no of script-language combinations
    total_combinations = len(combo_stats)
    print(f"Found {total_combinations} unique script-language combinations:")

    # Display breakdown by iterating through combo_stats (each row) using 'iterrows' method
    for (script, lang), row in combo_stats.iterrows():
        # Notice the two spaces, that is for indent in presentation
        print(f"  {script}-{lang}: {row['count']:,} rows (avg length: {row['avg_length']:.2f} chars)")

    # 11. Display text length statistics for the filtered dataset using describe method
    text_stats = df_main[text_column].str.len().describe()
    print(f"\nText length statistics:")
    print(f"  Min: {text_stats['min']:.0f} chars")
    print(f"  Max: {text_stats['max']:.0f} chars") 
    print(f"  Mean: {text_stats['mean']:.2f} chars")
    print(f"  Median: {text_stats['50%']:.2f} chars")
    
    # 12. Return the cleaned and validated DataFrame
    print(f"\nFinal dataset ready: {df_main.shape[0]:,} rows for trigram generation")
    return separated_df

def generate_trigrams(file_path: Path = DEFAULT_INPUT_DIR, min_text_len: Optional[int] = MIN_TEXT_LENGTH, max_text_len: Optional[int] = MAX_TEXT_LENGTH) -> Dict[Tuple[str, str], Dict[str, int]]:
    """ Process the separated dataframes from previous function & generate trigrams for each group """

    # 1. Load and group the training data
    separated_df = load_training_data(file_path, min_text_len, max_text_len)

    # 2. Initialize a dictionary for holding the group level frequency maps
    all_frequency_maps = {}
    
    # 3. Loop over the separated_df dictionary
    for (script, language), single_df in separated_df.items():

        # Create a dictionary for each group
        frequency_map_per_group = {} # This is the frequency map that contains all trigrams per group

        # Loop over each text entry in the single_df
        for text in single_df[REQUIRED_COLUMNS[0]]:
            frequency_map_per_entry = generate_trigrams_frequency_map(text)

            # Loop over each frequency map immediately
            for trigram, count in frequency_map_per_entry.items():
                # If the single trigram doesn't exist, then include it with its count
                if trigram not in frequency_map_per_group:
                    frequency_map_per_group[trigram] = count
                # If the single trigram already exists, then add to its count
                else:
                    frequency_map_per_group[trigram] += count

        # Store the frequency map for the current group
        all_frequency_maps[(script, language)] = frequency_map_per_group

    # 4. Return the combined dictionary
    return all_frequency_maps

def select_trigrams(file_path: Path = DEFAULT_INPUT_DIR, min_text_len: Optional[int] = MIN_TEXT_LENGTH, max_text_len: Optional[int] = MAX_TEXT_LENGTH, top_count: Optional[int] = SELECTED_TRIGRAMS_COUNT) -> Dict[Tuple[str, str], Dict[str, int]]:
    """ Select and return the most frequent trigrams for each group """

    # 1. Generate trigrams frequency maps for each group
    all_frequency_maps = generate_trigrams(file_path, min_text_len, max_text_len)

    # 2. Initialize a dictionary for holding the group level frequency maps but with selected and sorted trigrams only
    selected_trigrams = {}

    # 3. Loop over the frequency maps for each group, and sort and select the most frequent trigrams
    for (script, language), single_fq_map in all_frequency_maps.items():
        
        # One line code to sort by frequency (thus item[1]), with most frequent first (thus 'reverse=True'), and slicing the 'top_count' items
        top_trigrams = dict(sorted(single_fq_map.items(), key=lambda item: item[1], reverse=True)[:top_count])

        # Store the selected trigrams for the current group into a dictionary
        selected_trigrams[(script, language)] = top_trigrams

    # 4. Return the dictionary of selected trigrams
    return selected_trigrams

def generate_final_file(selected_trigrams: Dict[Tuple[str, str], Dict[str, int]], output_dir: Path = DEFAULT_OUTPUT_DIR, filename_prefix: str = OUTPUT_FILE_PREFIX) -> Path:
    """ Generate the final python file with the same format as default_trigrams.py """

    # 1. Ensure the output directory exists, otherwise create it
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Check if there are previous output files already in output folder, to determine next file name number
    output_file_pattern = str(output_dir/f"{filename_prefix}_*.py")
    existing_files = glob.glob(output_file_pattern) # Returns a list for matching pattern

    # 3. Extract file numbering from existing files using pathlib
    existing_numbers = set() # Declare a set
    for single_file in existing_files:
        one_stem = Path(single_file).stem
        if one_stem.startswith(f'{filename_prefix}_'):
            try:
                num_str = one_stem.replace(f'{filename_prefix}_', '')
                existing_numbers.add(int(num_str))
            except ValueError:
                continue

    # Find the first available slot starting from 1
    next_num = 1
    while next_num in existing_numbers:
        next_num += 1

    # Add the new number to filename
    output_filename = f"{filename_prefix}_{next_num:04d}.py"
    output_path = output_dir / output_filename

    # 4. Organize data by script (grouping multiple languages under same script)
    script_data = {}
    total_languages = 0
    total_trigrams = 0

    for (script, language), trigrams in selected_trigrams.items():
        if script not in script_data:
            script_data[script] = {}

        # Convert frequency counts to indices (like in default_trigrams.py)
        indexed_trigrams = {trigram: idx for idx, (trigram, freq) in enumerate(
            sorted(trigrams.items(), key=lambda x: x[1], reverse=True)
        )}

        script_data[script][language] = indexed_trigrams
        total_languages += 1
        total_trigrams += len(indexed_trigrams)

    # 5. Generate file content
    with open(output_path, 'w', encoding='utf-8') as f:
        # File header
        f.write('"""\n')
        f.write('Generated trigrams data for SomeLang\n')
        f.write(f'Total languages processed: {total_languages}\n')
        f.write(f'Total trigrams: {total_trigrams}\n')
        f.write('"""\n\n')

        # Core python imports (matching default_trigrams.py structure)
        f.write('# Core python imports\n')
        f.write('from typing import Dict # for type hinting\n\n')

        # Main trigrams dictionary
        f.write('LANGUAGE_TRIGRAMS: Dict[str, Dict[str, Dict[str, int]]] = {\n')

        # Write each script and its languages
        for script_name in sorted(script_data.keys()):
            f.write(f"    '{script_name}': {{\n")

            # Write each language under this script
            for language_name in sorted(script_data[script_name].keys()):
                trigrams = script_data[script_name][language_name]

                # Write language on single line with all trigrams (like default_trigrams.py)
                f.write(f"        '{language_name}': {{")

                # Convert trigrams to single line format
                trigram_items = []
                for trigram, index in trigrams.items():
                    # Escape single quotes in trigrams
                    escaped_trigram = trigram.replace("'", "\\'")
                    trigram_items.append(f"'{escaped_trigram}': {index}")

                # Join all trigrams on one line
                f.write(', '.join(trigram_items))
                f.write('},\n')

            f.write('    },\n')

        f.write('}\n')

    # 6. Print completion message
    print(f"\n✅ Generated trigrams file: {output_path}")
    print(f"   📊 Scripts: {len(script_data)}")
    print(f"   🌍 Languages: {total_languages}")
    print(f"   📝 Total trigrams: {total_trigrams}")

    return output_path

def main():
    """Main function to run the trainer from command line"""
    parser = argparse.ArgumentParser(description='Generate trigram models from training data')
    parser.add_argument('--input', type=Path, default=DEFAULT_INPUT_DIR, 
                       help='Input training data file or directory')
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT_DIR,
                       help='Output directory for trigram files')
    parser.add_argument('--min-text-length', type=int, default=MIN_TEXT_LENGTH,
                       help='Minimum text length to process')
    parser.add_argument('--max-text-length', type=int, default=MAX_TEXT_LENGTH,
                       help='Maximum text length to process')
    parser.add_argument('--trigrams-count', type=int, default=SELECTED_TRIGRAMS_COUNT,
                       help='Number of trigrams to select per language')
    
    args = parser.parse_args()
    
    # Run the complete pipeline
    print("🚀 Starting SomeLang training pipeline...")
    
    # Step 1: Select trigrams from training data
    selected_trigrams = select_trigrams(args.input, args.min_text_length, args.max_text_length, args.trigrams_count)
    
    # Step 2: Generate final file with selected trigrams
    output_file = generate_final_file(selected_trigrams, args.output)
    
    print(f"🎉 Training completed! Generated: {output_file}")

if __name__ == "__main__":
    main()
