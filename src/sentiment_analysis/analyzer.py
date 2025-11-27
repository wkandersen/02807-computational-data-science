"""Sentiment analysis models and utilities."""

import pandas as pd
from typing import Union, List, Dict
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    """Main sentiment analyzer class supporting multiple methods."""
    
    def __init__(self, method: str = 'vader'):
        """
        Initialize sentiment analyzer.
        
        Args:
            method: Sentiment analysis method ('vader', 'textblob', or 'both')
        """
        self.method = method.lower()
        
        if self.method in ['vader', 'both']:
            self.vader = SentimentIntensityAnalyzer()
        
    def analyze_vader(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner).
        
        Args:
            text: Input text
            
        Returns:
            Dictionary with sentiment scores
        """
        scores = self.vader.polarity_scores(text)
        return scores
    
    def analyze_textblob(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using TextBlob.
        
        Args:
            text: Input text
            
        Returns:
            Dictionary with sentiment scores
        """
        blob = TextBlob(text)
        return {
            'polarity': blob.sentiment.polarity,
            'subjectivity': blob.sentiment.subjectivity
        }
    
    def analyze(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using the configured method.
        
        Args:
            text: Input text
            
        Returns:
            Dictionary with sentiment scores
        """
        if self.method == 'vader':
            return self.analyze_vader(text)
        elif self.method == 'textblob':
            return self.analyze_textblob(text)
        elif self.method == 'both':
            vader_scores = self.analyze_vader(text)
            textblob_scores = self.analyze_textblob(text)
            return {**vader_scores, **textblob_scores}
        else:
            raise ValueError(f"Unknown method: {self.method}")
    
    def classify_sentiment(self, scores: Dict[str, float]) -> str:
        """
        Classify sentiment as positive, negative, or neutral.
        
        Args:
            scores: Sentiment scores dictionary
            
        Returns:
            Sentiment label
        """
        if self.method == 'vader' or self.method == 'both':
            compound = scores.get('compound', 0)
            if compound >= 0.05:
                return 'positive'
            elif compound <= -0.05:
                return 'negative'
            else:
                return 'neutral'
        elif self.method == 'textblob':
            polarity = scores.get('polarity', 0)
            if polarity > 0.1:
                return 'positive'
            elif polarity < -0.1:
                return 'negative'
            else:
                return 'neutral'
    
    def analyze_dataframe(self, df: pd.DataFrame, text_column: str = 'lyrics') -> pd.DataFrame:
        """
        Analyze sentiment for a dataframe of texts.
        
        Args:
            df: Input dataframe
            text_column: Name of the column containing text
            
        Returns:
            Dataframe with sentiment scores and labels
        """
        df = df.copy()
        
        # Analyze each text
        sentiment_results = df[text_column].apply(lambda x: self.analyze(str(x)))
        
        # Extract scores into separate columns
        if self.method == 'vader' or self.method == 'both':
            df['neg'] = sentiment_results.apply(lambda x: x.get('neg', 0))
            df['neu'] = sentiment_results.apply(lambda x: x.get('neu', 0))
            df['pos'] = sentiment_results.apply(lambda x: x.get('pos', 0))
            df['compound'] = sentiment_results.apply(lambda x: x.get('compound', 0))
        
        if self.method == 'textblob' or self.method == 'both':
            df['polarity'] = sentiment_results.apply(lambda x: x.get('polarity', 0))
            df['subjectivity'] = sentiment_results.apply(lambda x: x.get('subjectivity', 0))
        
        # Add sentiment label
        df['sentiment'] = sentiment_results.apply(lambda x: self.classify_sentiment(x))
        
        return df
