#!/usr/bin/env python3
"""
Script to analyze sentiment of songs from a CSV file.

Usage:
    python analyze_songs.py --input data/raw/songs.csv --output data/processed/songs_sentiment.csv
"""

import sys
import os
import argparse

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.preprocessing import preprocess_lyrics_dataframe
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description='Analyze sentiment of songs')
    parser.add_argument('--input', '-i', required=True, help='Input CSV file path')
    parser.add_argument('--output', '-o', required=True, help='Output CSV file path')
    parser.add_argument('--text-column', default='lyrics', help='Name of the text column')
    parser.add_argument('--method', default='vader', choices=['vader', 'textblob', 'both'],
                       help='Sentiment analysis method')
    parser.add_argument('--preprocess', action='store_true', help='Preprocess text before analysis')
    
    args = parser.parse_args()
    
    print(f"Loading data from {args.input}...")
    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} songs")
    
    if args.preprocess:
        print("Preprocessing lyrics...")
        df = preprocess_lyrics_dataframe(df, text_column=args.text_column)
        text_column = 'cleaned_lyrics'
    else:
        text_column = args.text_column
    
    print(f"Analyzing sentiment using {args.method}...")
    analyzer = SentimentAnalyzer(method=args.method)
    df = analyzer.analyze_dataframe(df, text_column=text_column)
    
    print(f"Saving results to {args.output}...")
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df.to_csv(args.output, index=False)
    
    print("\n=== Analysis Complete ===")
    print(f"Total songs: {len(df)}")
    print("\nSentiment Distribution:")
    print(df['sentiment'].value_counts())
    print("\nResults saved successfully!")


if __name__ == '__main__':
    main()
