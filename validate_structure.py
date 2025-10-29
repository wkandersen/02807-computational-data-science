#!/usr/bin/env python3
"""
Validate project structure without requiring dependencies.
This script checks that all necessary files and directories exist.
"""

import os
import sys
from pathlib import Path


def validate_structure():
    """Validate project structure."""
    root = Path(__file__).parent
    
    # Required directories
    required_dirs = [
        'config',
        'data/raw',
        'data/processed',
        'data/external',
        'notebooks',
        'scripts',
        'src/sentiment_analysis',
        'tests',
    ]
    
    # Required files
    required_files = [
        'README.md',
        'requirements.txt',
        'setup.py',
        'config/config.yaml',
        'data/README.md',
        'src/sentiment_analysis/__init__.py',
        'src/sentiment_analysis/analyzer.py',
        'src/sentiment_analysis/preprocessing.py',
        'src/sentiment_analysis/visualization.py',
        'src/sentiment_analysis/data_utils.py',
        'notebooks/01_introduction.ipynb',
        'notebooks/02_data_exploration.ipynb',
        'notebooks/03_advanced_analysis.ipynb',
        'scripts/analyze_songs.py',
        'scripts/generate_sample_data.py',
        'tests/__init__.py',
        'tests/test_analyzer.py',
        'tests/test_preprocessing.py',
    ]
    
    print("=" * 60)
    print("PROJECT STRUCTURE VALIDATION")
    print("=" * 60)
    
    errors = []
    
    # Check directories
    print("\nChecking directories...")
    for dir_path in required_dirs:
        full_path = root / dir_path
        if full_path.exists() and full_path.is_dir():
            print(f"  ✓ {dir_path}")
        else:
            print(f"  ✗ {dir_path} - MISSING")
            errors.append(f"Missing directory: {dir_path}")
    
    # Check files
    print("\nChecking files...")
    for file_path in required_files:
        full_path = root / file_path
        if full_path.exists() and full_path.is_file():
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path} - MISSING")
            errors.append(f"Missing file: {file_path}")
    
    # Summary
    print("\n" + "=" * 60)
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} errors found")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("VALIDATION SUCCESSFUL: All required files and directories exist!")
        print("\nNext steps:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Install package: pip install -e .")
        print("  3. Generate sample data: python scripts/generate_sample_data.py")
        print("  4. Start Jupyter: jupyter notebook")
        return True


if __name__ == '__main__':
    success = validate_structure()
    sys.exit(0 if success else 1)
