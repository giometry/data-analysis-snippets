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

# expected basic standardization with keep = true
df_basic_standardize = pd.DataFrame(np.array([[4, -1.161895], [5, -0.387298], [6, 0.387298], [7, 1.161895]]), columns=['b', 'b_standardized'])
sbg.make_columns_float(df_basic_standardize, ['b', 'b_standardized'])

# expected basic standardization with keep = false
df_basic_standardize_v2 = pd.DataFrame(np.array([[-1.161895], [-0.387298], [0.387298], [1.161895]]), columns=['b_standardized'])
sbg.make_columns_float(df_basic_standardize_v2, ['b_standardized'])

# tests the basic standardization function
class TestStandardizeMethod(unittest.TestCase):
    
    def test_basic_standardization(self):
        # Test standardizing columns b, dropping column a,c and keep = false
        pd.testing.assert_frame_equal(df_basic_standardize, sbg.standardize_dataframe(df, ['a', 'c'], ['b'], True))
        # Test standardizing columns b, dropping column a,c and keep = true
        pd.testing.assert_frame_equal(df_basic_standardize_v2, sbg.standardize_dataframe(df, ['a', 'c'], ['b'], False))
        
# tests the standardize by group function
class TestStandardizeByGroupMethod(unittest.TestCase):

    def test_basic_standardization(self):
        # Test standardizing columns b,c with groupings from column a and keep = false
        pd.testing.assert_frame_equal(df_standardized_by_a, sbg.standardize_dataframe_by_group(df, ['a'], [], ['b','c'], False))
        # Test standardizing columns b,c with groupings from column a and keep = true
        pd.testing.assert_frame_equal(df_standardized_by_a_v2, sbg.standardize_dataframe_by_group(df, ['a'], [], ['b','c'], True))

    def test_dropping_columns(self):
        # Test standardizing columns b (drop column c) with groupings from column a and keep = false
        pd.testing.assert_frame_equal(df_standardized_by_a_v3, sbg.standardize_dataframe_by_group(df, ['a'], ['c'], ['b'], False))
        # Test standardizing columns b (drop column c) with groupings from column a and keep = true
        pd.testing.assert_frame_equal(df_standardized_by_a_v4, sbg.standardize_dataframe_by_group(df, ['a'], ['c'], ['b'], True))
        
    def test_keeping_columns(self):
        # Test standardizing columns b (keep column c) with groupings from column a and keep = false
        pd.testing.assert_frame_equal(df_standardized_by_a_v5, sbg.standardize_dataframe_by_group(df, ['a'], [], ['b'], False))
        # Test standardizing columns b (keep column c) with groupings from column a and keep = true
        pd.testing.assert_frame_equal(df_standardized_by_a_v6, sbg.standardize_dataframe_by_group(df, ['a'], [], ['b'], True))

if __name__ == '__main__':
    unittest.main()

