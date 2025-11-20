"""Data preprocessing utilities for song lyrics."""

import re
import string
import pandas as pd
from typing import List, Optional
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def download_nltk_resources():
    """Download required NLTK resources."""
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
    except Exception as e:
        print(f"Error downloading NLTK resources: {e}")


def clean_text(text: str, remove_stopwords: bool = False) -> str:
    """
    Clean and preprocess text data.
    
    Args:
        text: Input text to clean
        remove_stopwords: Whether to remove stopwords
        
    Returns:
        Cleaned text
    """
    if not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    if remove_stopwords:
        download_nltk_resources()
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        text = ' '.join([word for word in tokens if word not in stop_words])
    
    return text


def preprocess_lyrics_dataframe(df: pd.DataFrame, text_column: str = 'lyrics') -> pd.DataFrame:
    """
    Preprocess a dataframe containing song lyrics.
    
    Args:
        df: Input dataframe
        text_column: Name of the column containing lyrics
        
    Returns:
        Dataframe with cleaned lyrics
    """
    df = df.copy()
    
    # Add cleaned text column
    df['cleaned_lyrics'] = df[text_column].apply(lambda x: clean_text(x))
    
    # Add word count
    df['word_count'] = df['cleaned_lyrics'].apply(lambda x: len(x.split()))
    
    return df


def extract_features(text: str) -> dict:
    """
    Extract basic text features from lyrics.
    
    Args:
        text: Input text
        
    Returns:
        Dictionary of features
    """
    features = {}
    
    # Word count
    words = text.split()
    features['word_count'] = len(words)
    
    # Character count
    features['char_count'] = len(text)
    
    # Average word length
    if words:
        features['avg_word_length'] = sum(len(word) for word in words) / len(words)
    else:
        features['avg_word_length'] = 0
    
    # Unique word count
    features['unique_word_count'] = len(set(words))
    
    return features
