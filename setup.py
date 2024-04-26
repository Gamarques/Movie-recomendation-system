from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'gamarques'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author_email = 'gabrielgamarques1@gmail.com',
    description = 'A package for movies recommendation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS

)