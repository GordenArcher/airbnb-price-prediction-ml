"""
Feature Engineering Module
Functions for creating engineered features
"""

import pandas as pd
import numpy as np

def create_engineered_features(df):
    """
    Create 10 new engineered features
    
    Args:
        df (pd.DataFrame): Input data
        
    Returns:
        pd.DataFrame: Data with engineered features
    """
    df_eng = df.copy()
    
    print("\nFeature Engineering:")
    
    # Feature 1: has_reviews
    df_eng['has_reviews'] = (df_eng['number_of_reviews'] > 0).astype(int)
    print(f"  ✓ Created: has_reviews")
    
    # Feature 2: days_since_review
    df_eng['last_review_date'] = pd.to_datetime(df_eng['last_review'], errors='coerce')
    reference_date = pd.Timestamp('2024-12-31')
    df_eng['days_since_review'] = (reference_date - df_eng['last_review_date']).dt.days
    df_eng['days_since_review'].fillna(-1, inplace=True)
    print(f"  ✓ Created: days_since_review")
    
    price_bins = [0, 50, 100, 200, 500, float('inf')]
    price_labels = ['Budget', 'Economy', 'Mid-Range', 'Premium', 'Luxury']
    df_eng['price_category'] = pd.cut(df_eng['price'], bins=price_bins, labels=price_labels, include_lowest=True)
    print(f"  ✓ Created: price_category")
    
    df_eng['availability_level'] = pd.cut(df_eng['availability_365'],
                                           bins=[0, 30, 100, 300, 365],
                                           labels=['Low', 'Medium-Low', 'Medium-High', 'High'],
                                           include_lowest=True)
    print(f"  ✓ Created: availability_level")
    
    df_eng['host_experience'] = pd.cut(df_eng['calculated_host_listings_count'],
                                        bins=[0, 1, 3, 10, float('inf')],
                                        labels=['New', 'Growing', 'Established', 'Power'],
                                        include_lowest=True)
    print(f"  ✓ Created: host_experience")
    
    df_eng['popularity_score'] = df_eng['number_of_reviews'] / (df_eng['calculated_host_listings_count'] + 1)
    print(f"  ✓ Created: popularity_score")
    
    # Feature 7: room_type_encoded
    room_type_map = {room: idx for idx, room in enumerate(sorted(df_eng['room_type'].unique()))}
    df_eng['room_type_encoded'] = df_eng['room_type'].map(room_type_map)
    print(f"  ✓ Created: room_type_encoded")
    
    df_eng['is_entire_home'] = (df_eng['room_type'] == 'Entire home/apt').astype(int)
    print(f"  ✓ Created: is_entire_home")
    
    df_eng['host_multi_listing'] = (df_eng['calculated_host_listings_count'] > 1).astype(int)
    print(f"  ✓ Created: host_multi_listing")
    
    neighbourhood_map = {ng: idx for idx, ng in enumerate(df_eng['neighbourhood_group'].unique())}
    df_eng['neighbourhood_encoded'] = df_eng['neighbourhood_group'].map(neighbourhood_map)
    print(f"  ✓ Created: neighbourhood_encoded")
    
    print(f"\n  Total features created: 10")
    print(f"  Original columns: {len(df)}")
    print(f"  New columns: {len(df_eng)}")
    
    return df_eng
