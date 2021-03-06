# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(  
    name='hoboreader', 
    version='0.0.2',  
    author='Steven K Firth',  # Optional
    author_email='s.k.firth@lboro.ac.uk',  # Optional
    description='Python package for reading Onset Hobo sensor csv files',  # Required
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/building-energy/hoboreader',  # Optional
    packages=find_packages(), # Required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )
