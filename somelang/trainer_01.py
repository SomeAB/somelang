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
MAX_TRAINING_FILE_SIZE = 4096 # Maximum file size for training data in MB
REQUIRED_COLUMNS = ['text', 'language', 'script'] # This is the list of expected columns in parquet file. Change these if using a different dataset. Keep first element as text
MIN_TEXT_LENGTH = 3 # Minimum length of the text inside each text column in each row
MAX_TEXT_LENGTH = 2048 # Maximum length of the text inside each text column in each row

def split_training_data(file_path: Path, max_size_mb: int) -> pd.DataFrame:
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

def load_training_data(file_path: str, text_len: Optional[int] = MAX_TEXT_LENGTH) -> pd.DataFrame:
    """Handle the incoming training data file"""

    # 1. Validate file exists using Pathlib
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Training data file not found: {file_path}")
    
    # 2. Use Path.stat and st_size to get file size in bytes
    file_size_bytes = file_path.stat().st_size

    # 3. Convert the file size from bytes to MB
    file_size_mb = file_size_bytes / (1024**2)

    # 4. If the file is above the limit, split it into smaller batches
    # In both cases, we get a dataframe, stored in 'df_main'
    if file_size_mb > MAX_TRAINING_FILE_SIZE:
        print(f"File size exceeds {MAX_TRAINING_FILE_SIZE}MB limit. Loading in batches...")
        df_main = split_training_data(file_path, MAX_TRAINING_FILE_SIZE)
    else:
        print("File size is within limits. Loading the entire file into memory...")
        df_main = pd.read_parquet(file_path)

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
    df_main = df_main[text_data_length.between(MIN_TEXT_LENGTH, text_len, inclusive='both')]

    # Report the number of rows dropped
    if df_main.shape[0] < initial_row_count:
        dropped_count = initial_row_count - df_main.shape[0] # Get no of dropped rows by substracting current count from initial count
        print(f"Removed {dropped_count:,} rows with invalid {text_column} (null, empty, or outside {MIN_TEXT_LENGTH}-{text_len} char range). Remaining: {df_main.shape[0]:,} rows")

    # 9. Ensure we still have data after filtering
    if df_main.empty:
        raise ValueError(f"No valid training data remaining after filtering for null, empty, too short and too long text")
    
    # 10. Display important stats
    # Group first, Get both count and average length for each group & round to 2 decimal places, all in a single operation
    combo_stats = df_main.groupby(['script', 'language']).agg({
        text_column: ['count', lambda x: x.str.len().mean()]
    }).round(2)

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
    return df_main





    

    

