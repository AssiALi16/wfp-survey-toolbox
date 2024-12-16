from typing import List

import pandas as pd


def check_columns_exist(
    df: pd.DataFrame, required_columns: List[str]
) -> tuple[bool, List[str]]:
    """Check if all required columns exist in dataframe"""
    missing_cols = [col for col in required_columns if col not in df.columns]
    return len(missing_cols) == 0, missing_cols


def check_missing_values(
    df: pd.DataFrame, columns: List[str]
) -> tuple[bool, List[str]]:
    """Check if specified columns have no missing values"""
    cols_with_missing = [col for col in columns if df[col].isna().any()]
    return len(cols_with_missing) == 0, cols_with_missing


def check_numeric_columns(
    df: pd.DataFrame, columns: List[str]
) -> tuple[bool, List[str]]:
    """Check if columns are numeric type"""
    non_numeric_cols = [
        col for col in columns if not pd.api.types.is_numeric_dtype(df[col])
    ]
    return len(non_numeric_cols) == 0, non_numeric_cols


def check_value_ranges(
    df: pd.DataFrame, columns: List[str], min_val: float = 0, max_val: float = 7
) -> tuple[bool, List[str]]:
    """Check if values fall within expected range"""
    out_of_range_cols = [
        col
        for col in columns
        if not ((df[col] >= min_val) & (df[col] <= max_val)).all()
    ]
    return len(out_of_range_cols) == 0, out_of_range_cols
