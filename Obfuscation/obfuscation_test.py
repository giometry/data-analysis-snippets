# -*- coding: utf-8 -*-
"""
Tests code (obfuscate.py) to obfuscate dataframe

Created on 4/3/2021
@author: Giovanni R Budi
"""

import unittest
import numpy as np
import pandas as pd
import obfuscation as obf

# Tests the obfuscation functions
class TestObfuscationMethod(unittest.TestCase):
    
    # Test obfuscating column names
    def test_obfuscate_columns(self):
        # initial dataframe
        df = pd.DataFrame(np.array([[1, 1, 0], [3, 0, 0], [0, 1, 2]]), columns=['cat', 'dog', 'bird'])
        expected_obfuscated_columns = pd.DataFrame(np.array([[1, 1, 0], [3, 0, 0], [0, 1, 2]]), columns=['a', 'b', 'c'])
        obf.obfuscate_column_names(df)
        self.assertTrue(df.equals(expected_obfuscated_columns))
        # expected result of column obfuscation
        expected_obfuscated_column = pd.DataFrame(np.array([[1, 1, 0], [3, 0, 0], [0, 1, 2]]), columns=['a', 'b', 'c'])
        # obfuscates intial dataframe column names
        obf.obfuscate_column_names(df)
        # tests expected vs actual of column name obfuscation
        pd.testing.assert_frame_equal(expected_obfuscated_column, df)
        
    # Test obfuscating values in numeric columns with key dataframe
    def test_obfuscate_number(self):
        # initial dataframe
        df = pd.DataFrame(np.array([[1, 1, 0], [3, 0, 0], [0, 1, 2]]), columns=['cat', 'dog', 'bird'])
        # key dataframe 
        key = pd.DataFrame(np.array([[3, 2, 1]]), columns=['cat', 'dog', 'bird'])
        # expected result of numeric column obfuscation
        expected_obfuscated_numeric = pd.DataFrame(np.array([[1/3, 1/2, 0], [1, 0, 0], [0, 1/2, 2]]), columns=['cat', 'dog', 'bird'])
        # obfuscates initial dataframe numeric values
        obf.obfuscate_numeric_values(df, key)
        # test expected vs actual of numeric column obfuscation
        pd.testing.assert_frame_equal(expected_obfuscated_numeric, df)
        
    # Test both obfuscation methods
    def test_obfuscation(self):
        # initial dataframe
        df = pd.DataFrame(np.array([[1, 1, 0], [3, 0, 0], [0, 1, 2]]), columns=['cat', 'dog', 'bird'])
        # key dataframe
        key = pd.DataFrame(np.array([[3, 2, 1]]), columns=['cat', 'dog', 'bird'])
        # expected result of obfuscation
        expected_obfuscation = pd.DataFrame(np.array([[1/3, 1/2, 0], [1, 0, 0], [0, 1/2, 2]]), columns=['a', 'b', 'c'])
        # obfuscates initial dataframe numeric values
        obf.obfuscate_numeric_values(df, key)
        # obfuscates initial dataframe column names
        obf.obfuscate_column_names(df)
        # tests expected vs actual of obfuscation
        pd.testing.assert_frame_equal(expected_obfuscation, df)

if __name__ == '__main__':
    unittest.main()

