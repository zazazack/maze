"""App settings."""
import os
import sys
import logging

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

version = f'Python version: {sys.version}'
workdir = f'Working directory: {os.path.abspath(os.curdir)}'
logging.debug(version)
logging.debug(workdir)
