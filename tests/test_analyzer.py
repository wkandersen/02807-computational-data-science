"""Tests for sentiment analyzer module."""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import pandas as pd
from sentiment_analysis.analyzer import SentimentAnalyzer


def test_vader_analyzer():
    """Test VADER sentiment analyzer."""
    analyzer = SentimentAnalyzer(method='vader')
    
    # Positive text
    positive_text = "I love this song, it's amazing and wonderful!"
    result = analyzer.analyze(positive_text)
    assert 'compound' in result
    assert result['compound'] > 0
    
    # Negative text
    negative_text = "This is terrible, awful, and horrible."
    result = analyzer.analyze(negative_text)
    assert result['compound'] < 0


def test_textblob_analyzer():
    """Test TextBlob sentiment analyzer."""
    analyzer = SentimentAnalyzer(method='textblob')
    
    positive_text = "I love this wonderful song"
    result = analyzer.analyze(positive_text)
    assert 'polarity' in result
    assert 'subjectivity' in result
    assert result['polarity'] > 0


def test_classify_sentiment():
    """Test sentiment classification."""
    analyzer = SentimentAnalyzer(method='vader')
    
    # Positive
    scores = {'compound': 0.5}
    assert analyzer.classify_sentiment(scores) == 'positive'
    
    # Negative
    scores = {'compound': -0.5}
    assert analyzer.classify_sentiment(scores) == 'negative'
    
    # Neutral
    scores = {'compound': 0.02}
    assert analyzer.classify_sentiment(scores) == 'neutral'


def test_analyze_dataframe():
    """Test dataframe analysis."""
    analyzer = SentimentAnalyzer(method='vader')
    
    df = pd.DataFrame({
        'lyrics': [
            'I love this song',
            'This is sad and depressing',
            'Just another day'
        ]
    })
    
    result = analyzer.analyze_dataframe(df, text_column='lyrics')
    
    assert 'sentiment' in result.columns
    assert 'compound' in result.columns
    assert len(result) == 3
    assert result['sentiment'].iloc[0] == 'positive'
    assert result['sentiment'].iloc[1] == 'negative'


def test_invalid_method():
    """Test handling of invalid method."""
    analyzer = SentimentAnalyzer(method='invalid')
    with pytest.raises(ValueError):
        analyzer.analyze("test text")
