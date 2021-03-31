# -*- coding: utf-8 -*-
"""
Tests code (standardize_by_group.py) to standardize dataframe based on groupby columns
Created on 3/30/2021
@author: Giovanni R Budi
"""

import unittest
import numpy as np
import pandas as pd
# import file with standardization function
import standardize_by_group as sbg

# intial test dataframe
df = pd.DataFrame(np.array([['A', 4, 7], ['A', 5, 8], ['B', 6, 9], ['B', 7, 10]]), columns=['a', 'b', 'c'])

# expected standardized dataframe output for standardizing columns b,c with groupings from column a and keep = false
df_standardized_by_a = pd.DataFrame(np.array([['A', -0.7071067811865475, -0.7071067811865475], ['A', 0.7071067811865475, 0.7071067811865475], ['B', -0.7071067811865475, -0.7071067811865475], ['B', 0.7071067811865475, 0.7071067811865475]]), columns=['a', 'b_standardized', 'c_standardized'])
sbg.make_columns_float(df_standardized_by_a, ['b_standardized', 'c_standardized'])

# expected standardized dataframe output for standardizing columns b,c with groupings from column a and keep = true
df_standardized_by_a_v2 = pd.DataFrame(np.array([['A', 4, 7, -0.7071067811865475, -0.7071067811865475], ['A', 5, 8, 0.7071067811865475, 0.7071067811865475], ['B', 6, 9, -0.7071067811865475, -0.7071067811865475], ['B', 7, 10, 0.7071067811865475, 0.7071067811865475]]), columns=['a', 'b', 'c', 'b_standardized', 'c_standardized'])
sbg.make_columns_float(df_standardized_by_a_v2, ['b', 'c', 'b_standardized', 'c_standardized'])

# expected standardized dataframe output for standardizing columns b (drop column c) with groupings from column a and keep = false
df_standardized_by_a_v3 = pd.DataFrame(np.array([['A', -0.7071067811865475], ['A', 0.7071067811865475], ['B', -0.7071067811865475], ['B', 0.7071067811865475]]), columns=['a', 'b_standardized'])
sbg.make_columns_float(df_standardized_by_a_v3, ['b_standardized'])

# expected standardized dataframe output for standardizing columns b (drop column c) with groupings from column a and keep = true
df_standardized_by_a_v4 = pd.DataFrame(np.array([['A', 4, -0.7071067811865475], ['A', 5, 0.7071067811865475], ['B', 6, -0.7071067811865475], ['B', 7, 0.7071067811865475]]), columns=['a', 'b', 'b_standardized'])
sbg.make_columns_float(df_standardized_by_a_v4, ['b', 'b_standardized'])

# expected standardized dataframe output for standardizing columns b (keep column c) with groupings from column a and keep = false
df_standardized_by_a_v5 = pd.DataFrame(np.array([['A', 7, -0.7071067811865475], ['A', 8, 0.7071067811865475], ['B', 9, -0.7071067811865475], ['B', 10, 0.7071067811865475]]), columns=['a', 'c', 'b_standardized'])
sbg.make_columns_float(df_standardized_by_a_v5, ['c', 'b_standardized'])

# expected standardized dataframe output for standardizing columns b (keep column c) with groupings from column a and keep = true
df_standardized_by_a_v6 = pd.DataFrame(np.array([['A', 4, 7, -0.7071067811865475], ['A', 5, 8, 0.7071067811865475], ['B', 6, 9, -0.7071067811865475], ['B', 7, 10, 0.7071067811865475]]), columns=['a', 'b', 'c', 'b_standardized'])
sbg.make_columns_float(df_standardized_by_a_v6, ['b', 'c', 'b_standardized'])

# tests the standardize by group function
class TestStandardizeByGroupMethod(unittest.TestCase):

    def test_basic_standardization(self):
        # Test standardizing columns b,c with groupings from column a and keep = false
        self.assertTrue(sbg.standardize_dataframe_by_group(df, ['a'], [], ['b','c'], False).equals(df_standardized_by_a))
        # Test standardizing columns b,c with groupings from column a and keep = false
        self.assertTrue(sbg.standardize_dataframe_by_group(df, ['a'], [], ['b','c'], True).equals(df_standardized_by_a_v2))

    def test_dropping_columns(self):
        # Test standardizing columns b (drop column c) with groupings from column a and keep = false
        self.assertTrue(sbg.standardize_dataframe_by_group(df, ['a'], ['c'], ['b'], False).equals(df_standardized_by_a_v3))
        # Test standardizing columns b (drop column c) with groupings from column a and keep = true
        self.assertTrue(sbg.standardize_dataframe_by_group(df, ['a'], ['c'], ['b'], True).equals(df_standardized_by_a_v4))
        
    def test_keeping_columns(self):
        # Test standardizing columns b (keep column c) with groupings from column a and keep = false
        self.assertTrue(sbg.standardize_dataframe_by_group(df, ['a'], [], ['b'], False).equals(df_standardized_by_a_v5))
        # Test standardizing columns b (keep column c) with groupings from column a and keep = true
        self.assertTrue(sbg.standardize_dataframe_by_group(df, ['a'], [], ['b'], True).equals(df_standardized_by_a_v6))

if __name__ == '__main__':
    unittest.main()

