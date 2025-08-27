import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))


from lib.cli import cli

if __name__ == '__main__':
    cli()