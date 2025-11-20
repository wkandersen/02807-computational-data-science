"""Tests for preprocessing module."""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from sentiment_analysis.preprocessing import clean_text, extract_features


def test_clean_text():
    """Test basic text cleaning."""
    text = "Hello World! This is a TEST."
    cleaned = clean_text(text)
    assert cleaned == "hello world this is a test"
    
    # Test with empty string
    assert clean_text("") == ""
    
    # Test with special characters
    text_special = "Hello@#$ 123 World!!!"
    cleaned_special = clean_text(text_special)
    assert cleaned_special == "hello world"


def test_clean_text_with_stopwords():
    """Test text cleaning with stopword removal."""
    text = "This is a test of the system"
    cleaned = clean_text(text, remove_stopwords=True)
    # Should remove common stopwords like 'is', 'a', 'the', 'of'
    assert len(cleaned.split()) < len(text.split())


def test_extract_features():
    """Test feature extraction."""
    text = "hello world test"
    features = extract_features(text)
    
    assert features['word_count'] == 3
    assert features['unique_word_count'] == 3
    assert features['char_count'] == len(text)
    assert features['avg_word_length'] > 0
    
    # Test with empty string
    empty_features = extract_features("")
    assert empty_features['word_count'] == 0
    assert empty_features['avg_word_length'] == 0


def test_clean_text_non_string():
    """Test handling of non-string input."""
    assert clean_text(None) == ""
    assert clean_text(123) == ""
