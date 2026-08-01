"""
Alex AI Configuration
"""

import os


# Alex Settings

ALEX_NAME = "Alex"


# Project paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


MEMORY_FILE = os.path.join(
    BASE_DIR,
    "data",
    "memory.json"
)


# Version

VERSION = "1.0"