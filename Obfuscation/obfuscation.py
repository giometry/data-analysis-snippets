# -*- coding: utf-8 -*-
"""
Code to obfuscate dataframe
Created on 3/30/2021
@author: Giovanni R Budi
"""

from string import ascii_lowercase
import itertools

def obfuscate_numeric_values(dataframe, key):
    """
    Obfuscates specified numeric columns in dataframe

    Parameters
    ----------
    dataframe : pandas dataframe
        initial dataframe to obfuscate numeric values
    key : pandas dataframe
        dataframe that contains column names and key values to obfuscate initial dataframe values
    """
    for col in key:
        dataframe[col] = dataframe[col]/key[col].iloc[0]

def iter_all_strings():
    """
    Creates an iterable of letters (a, b, c, ..., aa, ab, ..., aaa, etc.)

    Yield
    ------
    iterable
        iterable of letters/strings
    """
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)

def obfuscate_column_names(dataframe):
    """
    Obfuscates column names in dataframe

    Parameters
    ----------
    dataframe : pandas dataframe
        initial dataframe to obfuscate column names
    """
    dataframe.columns = list(itertools.islice(iter_all_strings(), len(dataframe.columns)))
    

