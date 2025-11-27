# Song Sentiment Analysis Project

A comprehensive project for analyzing sentiment in song lyrics using natural language processing and machine learning techniques.

## 📋 Project Overview

This project provides tools and notebooks for performing sentiment analysis on song lyrics. It includes:

- Data preprocessing utilities
- Multiple sentiment analysis methods (VADER, TextBlob)
- Visualization tools
- Jupyter notebooks for interactive analysis
- Command-line scripts for batch processing

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or conda for package management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/wkandersen/02807-computational-data-science.git
cd 02807-computational-data-science
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## 📁 Project Structure

```
.
├── config/                 # Configuration files
│   └── config.yaml        # Main configuration
├── data/                  # Data directory
│   ├── raw/              # Raw, unprocessed data
│   ├── processed/        # Cleaned and processed data
│   └── external/         # External datasets
├── notebooks/            # Jupyter notebooks
│   ├── 01_introduction.ipynb
│   ├── 02_data_exploration.ipynb
│   └── 03_advanced_analysis.ipynb
├── scripts/              # Command-line scripts
│   ├── analyze_songs.py
│   └── generate_sample_data.py
├── src/                  # Source code
│   └── sentiment_analysis/
│       ├── __init__.py
│       ├── analyzer.py          # Sentiment analysis models
│       ├── preprocessing.py     # Data preprocessing
│       ├── visualization.py     # Visualization utilities
│       └── data_utils.py        # Data loading/saving
├── tests/                # Unit tests
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
└── README.md            # This file
```

## 📊 Usage

### Interactive Analysis (Jupyter Notebooks)

Start Jupyter:
```bash
jupyter notebook
```

Then open the notebooks in the `notebooks/` directory:

1. **01_introduction.ipynb**: Get started with basic sentiment analysis
2. **02_data_exploration.ipynb**: Explore and visualize your data
3. **03_advanced_analysis.ipynb**: Advanced techniques and model comparison

### Command-Line Scripts

Generate sample data:
```bash
python scripts/generate_sample_data.py --output data/raw/sample_songs.csv
```

Analyze sentiment:
```bash
python scripts/analyze_songs.py --input data/raw/songs.csv --output data/processed/songs_sentiment.csv
```

### Python API

```python
from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.preprocessing import clean_text
import pandas as pd

# Load your data
df = pd.read_csv('data/raw/songs.csv')

# Initialize analyzer
analyzer = SentimentAnalyzer(method='vader')

# Analyze sentiment
df = analyzer.analyze_dataframe(df, text_column='lyrics')

# View results
print(df[['song_title', 'sentiment', 'compound']].head())
```

## 🔧 Features

### Sentiment Analysis Methods

- **VADER**: Optimized for social media and short texts
- **TextBlob**: Simple polarity and subjectivity analysis
- **Combined**: Use both methods for comparison

### Preprocessing

- Text cleaning and normalization
- Stopword removal
- Feature extraction (word count, unique words, etc.)

### Visualization

- Sentiment distribution plots
- Score histograms
- Word clouds
- Genre/artist comparisons
- Time series analysis

## 📈 Example Results

The project can analyze various aspects of song sentiment:

- Overall sentiment distribution (positive, negative, neutral)
- Sentiment scores and trends
- Artist and genre comparisons
- Word frequency and patterns

## 🧪 Testing

Run tests:
```bash
pytest tests/
```

## 📝 Configuration

Edit `config/config.yaml` to customize:

- Data paths
- Preprocessing settings
- Sentiment analysis thresholds
- Visualization preferences

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- VADER Sentiment Analysis
- TextBlob
- NLTK
- scikit-learn

## 📧 Contact

For questions or feedback, please open an issue on GitHub.