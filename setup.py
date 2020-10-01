# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:04:03 2020

@author: Afsar
"""

import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="Read-Excel",
 
    #version of the module
    version="0.0.1",
 
    #Name of Author
    author="Mohammad Afsar",
 
    #your Email address
    author_email="mohammadafsar415@gmail.com",
 
    #Small Description about module
    description="Read en excel file throgh google drive and plot it",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Pushkar-Singh-14/",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)