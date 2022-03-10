#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:46:17 2021

@author: junaid
"""

"""
Install in virtual environment: activate virtual environment then
    pyqt5 designer is a tool to create gui app by drag abd drop,
    You can just design using tool, but working part you have
    to still write code
    install pyqt designer by
    pip install PyQt5Designer
    Use pip freeze to see list of qt installation to verify designer 
    is installed or not
Install in anaconda: Most of the time, designer is installed
    So, Open terminal in anaconda base directory(environment) and type designer
    to open Pyqt designer. or some time you may need to type 
    dsigner.exe(windows)/designer.sh(linux)
    If it is not installed then you may proceed following
    open anaconda, select any environment you want to install
    Click on the triangle pointing in the environment of your choice to 
    open terminal then just use regular pip
    Type pip freeze to check all pyqt list
    Open terminal in anaconda base directory(environment) and type designer
    to open Pyqt designer
To convert ui file into python: for use
    pyuic5 -x source_file_name(along with directory).ui -o object_file_name.py
"""