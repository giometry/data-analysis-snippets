# -*- coding: utf-8 -*-
"""
Code to standardize dataframe based on groupby columns
Created on 3/30/2021
@author: Giovanni R Budi
"""

import pandas as pd

def make_columns_float(dataframe, cols):
    """
    Change specified columns in dataframe to data type float
    
    Parameters
    ----------
    dataframe : pandas dataframe
        initial dataframe
    cols : list of column names (strings)
        list of columns to change data type into float
    """
    for i in cols:
        dataframe[i] = dataframe[i].astype('float64')
    
def get_summary_data(dataframe, groupcolumns, summarycolumns):
    """
    Generates a dataframe with summary statistics (mean and standard deviation) of columns based on the grouped columns

    Parameters
    dataframe : pandas dataframe
        intial dataframe
    groupcolumns : list of column names (strings)
        list of columns to group by
    summarycolumns: list of column names (strings)
        list of columns to gather summary statistics for

    Returns
    -------
    df_summary : pandas dataframe
        dataframe with summary statistics
    """
    df_summary = dataframe.groupby(groupcolumns)[summarycolumns].agg(['mean', 'std'])
    df_summary.columns = ['_'.join(x) for x in df_summary.columns.ravel()]
    df_summary.reset_index(inplace=True)
    return df_summary

# This is the main function
def standardize_dataframe_by_group(dataframe, groupcolumns, dropcolumns, standardizecolumns, keep):
    """
    Generates standardized dataframe based on groupby columns

    Parameters
    ----------
    dataframe : pandas dataframe
        initial dataframe to be standardized
    groupcolumns : list of column names (strings)
        list of columns to group by
    dropcolumns : list of column names (strings)
        columns to drop in initial dataframe
    standardizecolumns : list of column names (strings)
        columns to standardize in initial dataframe
    keep: boolean
        option to keep original columns for list of standardized columns

    Returns
    -------
    df_standardized : pandas dataframe
        standardized dataframe
    """
    make_columns_float(dataframe, standardizecolumns)
    df_summary = get_summary_data(dataframe, groupcolumns, standardizecolumns)
    df_standardized = pd.merge(dataframe, df_summary, on=groupcolumns, how='left')
    for col in standardizecolumns:
        df_standardized[col + '_standardized'] = (df_standardized[col] - df_standardized[col + '_mean'])/df_standardized[col + '_std']
        df_standardized.drop(columns = [col + '_mean', col + '_std'], inplace=True)
    df_standardized.drop(columns = dropcolumns, inplace=True)
    if keep == False:
        df_standardized.drop(columns = standardizecolumns, inplace=True)
    return df_standardized




