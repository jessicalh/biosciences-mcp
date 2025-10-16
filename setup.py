#!/usr/bin/env python3
"""
Setup script for Biosciences MCP Server
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="biosciences-mcp",
    version="0.1.0a1",
    author="Jessica H",
    author_email="ke7gad@gmail.com",
    description="Alpha version bioinformatics MCP server built with FastMCP and Biopython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jessicalh/biosciences-mcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "biosciences-mcp=server.main:main",
        ],
    },
    keywords="bioinformatics genomics proteomics mcp claude biopython",
    project_urls={
        "Bug Reports": "https://github.com/jessicalh/biosciences-mcp/issues",
        "Source": "https://github.com/jessicalh/biosciences-mcp",
    },
)
