
import sys
import os


sys.path.insert(0, os.path.dirname(__file__))

try:
    from lib.cli import cli
    print("🎵 Music App CLI Starting... 🎵")
    if __name__ == '__main__':
        cli()
except ImportError as e:
    print(f"Import Error: {e}")
    print("Make sure you're running from the project root directory")
    print("and that all dependencies are installed: pipenv install")
except Exception as e:
    print(f"Error: {e}")