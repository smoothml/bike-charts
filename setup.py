import re
from pathlib import Path
from setuptools import find_packages, setup

NAME = "bike-charts"
DESCRIPTION = "Bike charts."
REQUIRES_PYTHON = ">=3.7.0"
AUTHOR = "Paul Harrison"

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / "bike_charts"

# Get package version
VERSION = "0.0.1"  # Default version
version_pattern = re.compile("(?<=__version__\s=\s[''])\d\.\d\.?\d?")
with open(PACKAGE_DIR / "__init__.py") as f:
    for line in f:
        res = version_pattern.search(line.strip())
        if res is not None:
            VERSION = res.group(0)

REQUIREMENTS = [
    "databases[postgresql]~=0.2",
    "python-dotenv~=0.12",
    "fastapi~=0.54",
    "sqlalchemy~=1.3",
    "uvicorn~=0.11",
]

setup(
    name=NAME,
    packages=find_packages(exclude=["tests"]),
    version=VERSION,
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    author=AUTHOR,
)
