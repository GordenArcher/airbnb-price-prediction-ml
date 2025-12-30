"""
Data Loading Module
Functions for loading and configuring data
"""

import pandas as pd
import yaml
import os

def load_data(filepath):
    """
    Load CSV data from file
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Data loaded successfully: {filepath}")
        print(f"  Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found - {filepath}")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {str(e)}")
        return None


def load_config(config_path='config/config.yaml'):
    """
    Load YAML configuration file
    
    Args:
        config_path (str): Path to config file
        
    Returns:
        dict: Configuration dictionary
    """
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        print(f"✓ Config loaded successfully: {config_path}")
        return config
    except FileNotFoundError:
        print(f"✗ Error: Config file not found - {config_path}")
        return None
    except Exception as e:
        print(f"✗ Error loading config: {str(e)}")
        return None


def save_data(df, filepath):
    """
    Save DataFrame to CSV
    
    Args:
        df (pd.DataFrame): Data to save
        filepath (str): Output file path
    """
    try:
        df.to_csv(filepath, index=False)
        print(f"✓ Data saved: {filepath}")
    except Exception as e:
        print(f"✗ Error saving data: {str(e)}")

