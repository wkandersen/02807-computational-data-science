# Data Directory

This directory contains all data used in the sentiment analysis project.

## Structure

- **raw/**: Original, unprocessed data files
  - Place your raw song lyrics CSV files here
  - Example format: songs.csv with columns: song_title, artist, lyrics, genre, year

- **processed/**: Cleaned and processed data
  - Output from preprocessing scripts
  - Data ready for analysis and modeling

- **external/**: External datasets and references
  - Third-party data sources
  - Reference datasets

## Data Format

Expected CSV format for song lyrics:

```csv
song_title,artist,lyrics,genre,year
"Song Name","Artist Name","Lyrics text here...","Pop",2020
```

## Getting Started

1. Place your raw data files in the `raw/` directory
2. Use the preprocessing scripts or notebooks to clean the data
3. Processed data will be saved in the `processed/` directory

## Sample Data

To generate sample data for testing:

```bash
python scripts/generate_sample_data.py --output data/raw/sample_songs.csv
```
