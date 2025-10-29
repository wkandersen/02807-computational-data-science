"""Setup script for sentiment analysis project."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sentiment-analysis",
    version="0.1.0",
    author="Your Name",
    description="A project for analyzing sentiment in songs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wkandersen/02807-computational-data-science",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "scikit-learn>=1.3.0",
        "nltk>=3.8.0",
        "textblob>=0.17.0",
        "vaderSentiment>=3.3.2",
    ],
)
