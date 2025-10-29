# Quick Start Guide

Get started with sentiment analysis in just a few minutes!

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/wkandersen/02807-computational-data-science.git
cd 02807-computational-data-science
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
pip install -e .
```

## Quick Example

### Using Python Script

Generate sample data and analyze it:
```bash
# Generate sample data
python scripts/generate_sample_data.py

# Analyze sentiment
python scripts/analyze_songs.py \
  --input data/raw/sample_songs.csv \
  --output data/processed/sentiment_results.csv \
  --method vader
```

### Using Python Code

```python
from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.data_utils import create_sample_data
import pandas as pd

# Create sample data
df = create_sample_data()

# Initialize analyzer
analyzer = SentimentAnalyzer(method='vader')

# Analyze sentiment
results = analyzer.analyze_dataframe(df, text_column='lyrics')

# View results
print(results[['song_title', 'sentiment', 'compound']].head())
```

### Using Jupyter Notebooks

```bash
jupyter notebook
```

Then open `notebooks/01_introduction.ipynb` and run the cells!

## What's Next?

- **Explore notebooks**: Check out the example notebooks in `notebooks/`
- **Add your data**: Place your song lyrics CSV in `data/raw/`
- **Customize analysis**: Edit `config/config.yaml` for your needs
- **Build models**: Create machine learning models in new notebooks

## Common Tasks

### Analyze Your Own Data

Your CSV should have at least these columns:
- A text column (e.g., 'lyrics')
- Optional: 'song_title', 'artist', 'genre', 'year'

```python
df = pd.read_csv('your_songs.csv')
analyzer = SentimentAnalyzer()
results = analyzer.analyze_dataframe(df, text_column='lyrics')
results.to_csv('results.csv', index=False)
```

### Visualize Results

```python
from sentiment_analysis.visualization import plot_sentiment_distribution

fig = plot_sentiment_distribution(results)
plt.show()
```

### Compare Methods

```python
# VADER
vader_analyzer = SentimentAnalyzer(method='vader')
vader_results = vader_analyzer.analyze_dataframe(df, text_column='lyrics')

# TextBlob
textblob_analyzer = SentimentAnalyzer(method='textblob')
textblob_results = textblob_analyzer.analyze_dataframe(df, text_column='lyrics')
```

## Troubleshooting

**Import errors?**
- Make sure you ran `pip install -r requirements.txt`
- Check that your virtual environment is activated

**NLTK data not found?**
- Run: `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`

**Jupyter kernel issues?**
- Install jupyter in your venv: `pip install jupyter`
- Add kernel: `python -m ipykernel install --user --name=venv`

## Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review example notebooks in `notebooks/`
- Open an issue on GitHub

Happy analyzing! 🎵📊
