# Contributing to Song Sentiment Analysis Project

Thank you for your interest in contributing to this project! This guide will help you get started.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/02807-computational-data-science.git
   cd 02807-computational-data-science
   ```

3. **Set up the development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-dev.txt
   pip install -e .
   ```

## Project Structure

- `src/sentiment_analysis/`: Main source code
- `notebooks/`: Jupyter notebooks for analysis
- `scripts/`: Command-line scripts
- `tests/`: Unit tests
- `data/`: Data directories
- `config/`: Configuration files

## Development Workflow

1. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Run tests** to ensure nothing is broken:
   ```bash
   make test
   # or
   pytest tests/ -v
   ```

4. **Format your code**:
   ```bash
   make format
   # or
   black src/ tests/ scripts/
   ```

5. **Run linters**:
   ```bash
   make lint
   # or
   flake8 src/ tests/
   ```

6. **Commit your changes** with a clear message:
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** on GitHub

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Write clear comments for complex logic

## Testing

- Write tests for new features
- Ensure all tests pass before submitting a PR
- Aim for good test coverage
- Use pytest for testing

## Documentation

- Update README.md if adding new features
- Add docstrings to new functions/classes
- Update notebooks if changing API
- Include examples in docstrings

## Commit Messages

Write clear, concise commit messages:
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but brief
- Reference issues when applicable

Examples:
```
Add VADER sentiment analyzer
Fix bug in text preprocessing
Update documentation for data loading
```

## Pull Request Process

1. Update documentation as needed
2. Ensure all tests pass
3. Update CHANGELOG.md with your changes
4. Get review from maintainers
5. Address any feedback
6. Merge when approved

## Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Relevant error messages or logs

## Questions?

Feel free to open an issue for any questions or concerns!

Thank you for contributing! 🎉
