import os
from setuptools import setup, find_packages

requirements = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as f:
        requirements = [
            line.strip() for line in f if line.strip() and not line.startswith("#")
        ]

setup(
    name="ANIME-RECOMMENDER-COMBINED",
    version="1.0",
    author="Shrikant",
    packages=find_packages(),
    install_requires=requirements,
)
