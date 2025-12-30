"""
Clustering Module
Functions for clustering and market segmentation
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

def perform_clustering(df, features, max_k=10, random_state=42):
    """
    Perform K-means clustering with optimal K selection
    
    Args:
        df (pd.DataFrame): Input data
        features (list): Feature columns for clustering
        max_k (int): Maximum K to test
        random_state (int): Random seed
        
    Returns:
        tuple: (cluster_labels, optimal_k, scaler)
    """
    cluster_data = df[features].dropna()
    
    scaler = StandardScaler()
    cluster_scaled = scaler.fit_transform(cluster_data)
    
    print("\nPerforming Clustering:")
    print(f"  Features: {features}")
    print(f"  Samples: {len(cluster_data):,}")
    

    silhouette_scores = []
    inertias = []
    
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        labels = kmeans.fit_predict(cluster_scaled)
        silhouette_scores.append(silhouette_score(cluster_scaled, labels))
        inertias.append(kmeans.inertia_)
    
    optimal_k = 2 + np.argmax(silhouette_scores)
    print(f"  ✓ Optimal K: {optimal_k}")
    
    kmeans_final = KMeans(n_clusters=optimal_k, random_state=random_state, n_init=10)
    cluster_labels = kmeans_final.fit_predict(cluster_scaled)
    
    return cluster_labels, optimal_k, scaler


def analyze_clusters(df, features, cluster_labels, optimal_k):
    """
    Analyze cluster characteristics
    
    Args:
        df (pd.DataFrame): Input data
        features (list): Feature columns
        cluster_labels (array): Cluster assignments
        optimal_k (int): Number of clusters
    """
    cluster_data = df[features].dropna().copy()
    cluster_data['Cluster'] = cluster_labels
    
    print(f"\nCluster Analysis:")
    print(f"\nCluster Distribution:")
    
    for cluster_id in range(optimal_k):
        cluster_mask = cluster_data['Cluster'] == cluster_id
        count = cluster_mask.sum()
        pct = (count / len(cluster_data)) * 100
        print(f"  Cluster {cluster_id}: {count:,} listings ({pct:.1f}%)")
    
    print(f"\nCluster Characteristics:")
    for cluster_id in range(optimal_k):
        cluster_mask = cluster_data['Cluster'] == cluster_id
        print(f"\n  Cluster {cluster_id}:")
        for feature in features:
            mean_val = cluster_data[cluster_mask][feature].mean()
            print(f"    {feature}: {mean_val:.2f}")
