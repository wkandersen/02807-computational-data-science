.PHONY: help install install-dev test clean lint format notebooks sample-data

help:
	@echo "Available commands:"
	@echo "  make install       - Install production dependencies"
	@echo "  make install-dev   - Install development dependencies"
	@echo "  make test          - Run tests"
	@echo "  make clean         - Clean temporary files"
	@echo "  make lint          - Run linters"
	@echo "  make format        - Format code with black"
	@echo "  make notebooks     - Start Jupyter notebook server"
	@echo "  make sample-data   - Generate sample data"

install:
	pip install -r requirements.txt
	pip install -e .

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .

test:
	pytest tests/ -v --cov=src/sentiment_analysis

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ .coverage htmlcov/

lint:
	flake8 src/ tests/ --max-line-length=100
	pylint src/sentiment_analysis

format:
	black src/ tests/ scripts/

notebooks:
	jupyter notebook notebooks/

sample-data:
	python scripts/generate_sample_data.py
