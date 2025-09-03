"""
SomeLang Cleaner - by SomeAB

This module handles data cleaning and standardization for training data.
Parses combined language codes (e.g., 'eng_Latn') into separate language and script columns.
Keeps script codes as 4-character ISO 15924 codes.
"""

import pandas as pd
import argparse
import os
import glob
from pathlib import Path
from typing import List, Tuple

# Note: No longer using script_codes.json as we keep script codes as-is


def parse_language_code(combined_code: str) -> Tuple[str, str]:
    """
    Parse combined language code into language and script components.
    
    Args:
        combined_code: Language code like 'eng_Latn' or 'eng'
        
    Returns:
        Tuple of (language_code, script_code)
        
    Examples:
        'eng_Latn' -> ('eng', 'Latn')
        'rus_Cyrl' -> ('rus', 'Cyrl') 
        'eng' -> ('eng', 'Unknown')
    """
    if '_' in combined_code:
        parts = combined_code.split('_', 1)
        language_code = parts[0]
        script_code = parts[1]
        
        # Keep script code as-is (4-character ISO 15924 code)
        return language_code, script_code
    else:
        # No script code provided
        return combined_code, 'Unknown'


def clean_data(input_files: List[str], output_dir: str = 'training_data') -> str:
    """
    Clean and standardize input parquet files.
    Parses combined language codes and creates separate language and script columns.
    Combines all input files into a single output file.
    
    Args:
        input_files: List of input parquet file paths
        output_dir: Directory to save cleaned files
        
    Returns:
        Output file path
    """
    processed_dataframes = []
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Find existing training_data files to determine starting counter
    existing_pattern = os.path.join(output_dir, "training_data_*.parquet")
    existing_files = glob.glob(existing_pattern)
    
    # Extract numbers from existing files and find the highest
    max_num = 0
    for existing_file in existing_files:
        basename = os.path.basename(existing_file)
        # Extract number from training_data_XXXX.parquet
        try:
            num_str = basename.replace('training_data_', '').replace('.parquet', '')
            num = int(num_str)
            max_num = max(max_num, num)
        except ValueError:
            continue
    
    # Use next available number for the combined output file
    output_counter = max_num + 1
    
    # Process each input file
    for i, input_file in enumerate(input_files, 1):
        print(f"Processing file {i}/{len(input_files)}: {input_file}")
        
        # Read input parquet file
        try:
            df = pd.read_parquet(input_file)
            print(f"  - Loaded {len(df):,} rows")
            print(f"  - Columns: {list(df.columns)}")
            
            # Process language column if it exists
            if 'language' in df.columns:
                print(f"  - Processing language codes...")
                
                # Parse language codes and create new columns
                language_script_pairs = df['language'].apply(parse_language_code)
                
                # Extract language and script into separate columns
                df['language'] = language_script_pairs.apply(lambda x: x[0])
                df['script'] = language_script_pairs.apply(lambda x: x[1])
                
                # Show sample of transformations
                sample_original = df.iloc[0]
                print(f"  - Sample transformation:")
                print(f"    Original: language='{sample_original.get('language', 'N/A')}'")
                print(f"    New: language='{sample_original['language']}', script='{sample_original['script']}'")
                
                # Show unique script types found
                unique_scripts = df['script'].unique()
                print(f"  - Found {len(unique_scripts)} unique script codes: {list(unique_scripts)[:5]}{'...' if len(unique_scripts) > 5 else ''}")
            else:
                print(f"  - No 'language' column found, keeping original structure")
            
            # Add processed DataFrame to list
            processed_dataframes.append(df)
            print(f"  - Added to combined dataset")
            
        except Exception as e:
            print(f"  - Error processing {input_file}: {e}")
            continue
    
    # Combine all processed DataFrames
    if not processed_dataframes:
        print("Error: No files were successfully processed.")
        return None
    
    print(f"\nCombining {len(processed_dataframes)} processed datasets...")
    combined_df = pd.concat(processed_dataframes, ignore_index=True)
    
    # Generate output filename
    output_filename = f"training_data_{output_counter:04d}.parquet"
    output_path = os.path.join(output_dir, output_filename)
    
    # Save combined dataset
    combined_df.to_parquet(output_path, index=False)
    
    print(f"Combined dataset statistics:")
    print(f"  - Total rows: {len(combined_df):,}")
    print(f"  - Final columns: {list(combined_df.columns)}")
    print(f"  - Languages: {sorted(combined_df['language'].unique()) if 'language' in combined_df.columns else 'N/A'}")
    print(f"  - Scripts: {sorted(combined_df['script'].unique()) if 'script' in combined_df.columns else 'N/A'}")
    print(f"  - Saved to: {output_path}")
    
    print(f"\nCompleted processing successfully.")
    return output_path


def main():
    """Command line interface for the cleaner."""
    parser = argparse.ArgumentParser(description='Clean and standardize training data files')
    parser.add_argument('input_files', nargs='+', help='Input parquet files to process')
    parser.add_argument('--output-dir', '-o', default='training_data', help='Output directory (default: training_data)')
    
    args = parser.parse_args()
    
    # Validate input files exist
    valid_files = []
    for file_path in args.input_files:
        if os.path.exists(file_path):
            valid_files.append(file_path)
        else:
            print(f"Warning: File not found: {file_path}")
    
    if not valid_files:
        print("Error: No valid input files found.")
        return
    
    print(f"SomeLang Cleaner")
    print(f"Input files: {len(valid_files)}")
    print(f"Output directory: {args.output_dir}")
    print("-" * 50)
    
    # Process files
    output_file = clean_data(valid_files, args.output_dir)
    
    print("-" * 50)
    if output_file:
        print(f"Generated combined cleaned file:")
        print(f"  - {output_file}")
    else:
        print("Error: No output file was generated.")


if __name__ == "__main__":
    main()
