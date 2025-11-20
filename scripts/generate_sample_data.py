#!/usr/bin/env python3
"""
Script to generate sample data for testing.

Usage:
    python generate_sample_data.py --output data/raw/sample_songs.csv
"""

import sys
import os
import argparse

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sentiment_analysis.data_utils import create_sample_data


def main():
    parser = argparse.ArgumentParser(description='Generate sample song data')
    parser.add_argument('--output', '-o', default='data/raw/sample_songs.csv',
                       help='Output CSV file path')
    
    args = parser.parse_args()
    
    print("Generating sample data...")
    df = create_sample_data()
    
    print(f"Created {len(df)} sample songs")
    print(f"\nSaving to {args.output}...")
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df.to_csv(args.output, index=False)
    
    print("Sample data generated successfully!")
    print("\nPreview:")
    print(df.head())


if __name__ == '__main__':
    main()
