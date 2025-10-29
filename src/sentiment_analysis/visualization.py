"""Visualization utilities for sentiment analysis."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from typing import Optional
import numpy as np


def set_style():
    """Set default plotting style."""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10


def plot_sentiment_distribution(df: pd.DataFrame, sentiment_column: str = 'sentiment', 
                                title: str = 'Sentiment Distribution'):
    """
    Plot the distribution of sentiments.
    
    Args:
        df: Dataframe with sentiment labels
        sentiment_column: Name of the sentiment column
        title: Plot title
    """
    set_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sentiment_counts = df[sentiment_column].value_counts()
    colors = {'positive': 'green', 'neutral': 'gray', 'negative': 'red'}
    
    bars = ax.bar(sentiment_counts.index, sentiment_counts.values)
    
    # Color bars
    for bar, label in zip(bars, sentiment_counts.index):
        bar.set_color(colors.get(label, 'blue'))
    
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_title(title)
    
    # Add count labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom')
    
    plt.tight_layout()
    return fig


def plot_sentiment_scores(df: pd.DataFrame, score_column: str = 'compound',
                          title: str = 'Sentiment Score Distribution'):
    """
    Plot distribution of sentiment scores.
    
    Args:
        df: Dataframe with sentiment scores
        score_column: Name of the score column
        title: Plot title
    """
    set_style()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(df[score_column], bins=50, edgecolor='black', alpha=0.7)
    ax.axvline(x=0, color='red', linestyle='--', label='Neutral')
    ax.set_xlabel('Sentiment Score')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    ax.legend()
    
    plt.tight_layout()
    return fig


def plot_sentiment_comparison(df: pd.DataFrame, group_column: str,
                              sentiment_column: str = 'sentiment',
                              title: str = 'Sentiment Comparison'):
    """
    Compare sentiment across different groups.
    
    Args:
        df: Dataframe with sentiment labels
        group_column: Column to group by (e.g., 'artist', 'genre')
        sentiment_column: Name of the sentiment column
        title: Plot title
    """
    set_style()
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create crosstab
    ct = pd.crosstab(df[group_column], df[sentiment_column], normalize='index') * 100
    
    ct.plot(kind='bar', stacked=True, ax=ax,
            color=['red', 'gray', 'green'])
    
    ax.set_xlabel(group_column.capitalize())
    ax.set_ylabel('Percentage (%)')
    ax.set_title(title)
    ax.legend(title='Sentiment')
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    return fig


def generate_wordcloud(text: str, title: str = 'Word Cloud',
                       max_words: int = 100,
                       background_color: str = 'white'):
    """
    Generate a word cloud from text.
    
    Args:
        text: Input text
        title: Plot title
        max_words: Maximum number of words
        background_color: Background color
    """
    set_style()
    fig, ax = plt.subplots(figsize=(12, 8))
    
    wordcloud = WordCloud(width=800, height=400,
                         max_words=max_words,
                         background_color=background_color,
                         colormap='viridis').generate(text)
    
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(title, fontsize=16)
    
    plt.tight_layout()
    return fig


def plot_sentiment_over_time(df: pd.DataFrame, date_column: str,
                             score_column: str = 'compound',
                             title: str = 'Sentiment Over Time'):
    """
    Plot sentiment trends over time.
    
    Args:
        df: Dataframe with sentiment scores and dates
        date_column: Name of the date column
        score_column: Name of the score column
        title: Plot title
    """
    set_style()
    fig, ax = plt.subplots(figsize=(12, 6))
    
    df_sorted = df.sort_values(date_column)
    
    ax.plot(df_sorted[date_column], df_sorted[score_column], marker='o', alpha=0.6)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Neutral')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sentiment Score')
    ax.set_title(title)
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    return fig


def plot_correlation_matrix(df: pd.DataFrame, features: list,
                           title: str = 'Feature Correlation Matrix'):
    """
    Plot correlation matrix for selected features.
    
    Args:
        df: Dataframe with features
        features: List of feature names
        title: Plot title
    """
    set_style()
    fig, ax = plt.subplots(figsize=(10, 8))
    
    corr = df[features].corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, ax=ax, square=True)
    
    ax.set_title(title)
    
    plt.tight_layout()
    return fig
