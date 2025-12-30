"""
Data Cleaning Module
Functions for data validation and cleaning
"""

import pandas as pd
import numpy as np

def validate_data(df):
    """
    Validate data quality
    
    Args:
        df (pd.DataFrame): Input data
        
    Returns:
        dict: Quality metrics
    """
    metrics = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().sum(),
        'duplicate_rows': df.duplicated().sum(),
        'duplicate_ids': df['id'].duplicated().sum() if 'id' in df.columns else 0,
        'invalid_prices': (df['price'] <= 0).sum() if 'price' in df.columns else 0,
        'negative_min_nights': (df['minimum_nights'] < 0).sum() if 'minimum_nights' in df.columns else 0
    }
    
    print("\nData Quality Report:")
    print(f"  Total rows: {metrics['total_rows']:,}")
    print(f"  Total columns: {metrics['total_columns']}")
    print(f"  Missing values: {metrics['missing_values']}")
    print(f"  Duplicate rows: {metrics['duplicate_rows']}")
    print(f"  Duplicate IDs: {metrics['duplicate_ids']}")
    print(f"  Invalid prices: {metrics['invalid_prices']}")
    print(f"  Negative min nights: {metrics['negative_min_nights']}")
    
    return metrics


def clean_data(df):
    """
    Clean data by removing invalid records and handling missing values
    
    Args:
        df (pd.DataFrame): Input data
        
    Returns:
        pd.DataFrame: Cleaned data
    """
    df_clean = df.copy()
    initial_rows = len(df_clean)
    
    print("\nData Cleaning Process:")
    
    df_clean = df_clean[df_clean['price'] > 0]
    removed_price = initial_rows - len(df_clean)
    print(f"  ✓ Removed {removed_price} rows with invalid prices")
    
    initial_rows = len(df_clean)
    df_clean = df_clean[df_clean['minimum_nights'] >= 0]
    removed_min_nights = initial_rows - len(df_clean)
    print(f"  ✓ Removed {removed_min_nights} rows with negative minimum nights")
    
    if 'reviews_per_month' in df_clean.columns:
        median_rpm = df_clean['reviews_per_month'].median()
        df_clean['reviews_per_month'].fillna(median_rpm, inplace=True)
        print(f"  ✓ Filled missing reviews_per_month with median: {median_rpm:.2f}")
    
    if 'last_review' in df_clean.columns:
        df_clean['last_review'].fillna('No Review', inplace=True)
        print(f"  ✓ Filled missing last_review with 'No Review'")
    
    print(f"\n  Cleaning Summary:")
    print(f"    Original: {len(df):,} rows")
    print(f"    Cleaned: {len(df_clean):,} rows")
    print(f"    Removed: {len(df) - len(df_clean):,} rows")
    
    return df_clean
