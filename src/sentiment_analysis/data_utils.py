"""Utilities for loading and saving data."""

import pandas as pd
import json
import os
from pathlib import Path
from typing import Optional, Dict, Any


def get_data_path(filename: str, data_type: str = 'raw') -> Path:
    """
    Get the full path to a data file.
    
    Args:
        filename: Name of the file
        data_type: Type of data ('raw', 'processed', 'external')
        
    Returns:
        Path object
    """
    base_path = Path(__file__).parent.parent.parent / 'data' / data_type
    return base_path / filename


def load_csv(filename: str, data_type: str = 'raw', **kwargs) -> pd.DataFrame:
    """
    Load a CSV file from the data directory.
    
    Args:
        filename: Name of the CSV file
        data_type: Type of data directory
        **kwargs: Additional arguments for pd.read_csv
        
    Returns:
        DataFrame
    """
    filepath = get_data_path(filename, data_type)
    return pd.read_csv(filepath, **kwargs)


def save_csv(df: pd.DataFrame, filename: str, data_type: str = 'processed', **kwargs):
    """
    Save a DataFrame to CSV in the data directory.
    
    Args:
        df: DataFrame to save
        filename: Name of the CSV file
        data_type: Type of data directory
        **kwargs: Additional arguments for df.to_csv
    """
    filepath = get_data_path(filename, data_type)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, **kwargs)


def load_json(filename: str, data_type: str = 'raw') -> Dict[Any, Any]:
    """
    Load a JSON file from the data directory.
    
    Args:
        filename: Name of the JSON file
        data_type: Type of data directory
        
    Returns:
        Dictionary
    """
    filepath = get_data_path(filename, data_type)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data: Dict[Any, Any], filename: str, data_type: str = 'processed'):
    """
    Save data to JSON in the data directory.
    
    Args:
        data: Dictionary to save
        filename: Name of the JSON file
        data_type: Type of data directory
    """
    filepath = get_data_path(filename, data_type)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def create_sample_data() -> pd.DataFrame:
    """
    Create a sample dataset for testing.
    
    Returns:
        Sample DataFrame with song lyrics
    """
    data = {
        'song_title': [
            'Happy Song',
            'Sad Ballad',
            'Neutral Tune',
            'Love Song',
            'Angry Track'
        ],
        'artist': [
            'Artist A',
            'Artist B',
            'Artist C',
            'Artist A',
            'Artist D'
        ],
        'lyrics': [
            'I am so happy today, sunshine and joy everywhere',
            'My heart is broken, tears falling down, sadness all around',
            'Walking down the street, just another day',
            'You are my everything, love fills my heart completely',
            'I am so angry, furious at everything happening'
        ],
        'genre': [
            'Pop',
            'Ballad',
            'Folk',
            'Pop',
            'Rock'
        ],
        'year': [
            2020,
            2019,
            2021,
            2020,
            2022
        ]
    }
    
    return pd.DataFrame(data)
