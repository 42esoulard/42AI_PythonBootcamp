#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools


setuptools.setup(
    name="ai42", # Replace with your own username
    version="1.0.0",
    user="esoulard",
    author="ai42",
    author_email="esoulard@student.42.fr",
    description="42ai Python bootcamp",
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)