# Clustering & Market Segmentation Report

**Project:** Airbnb Dataset Analysis  
**Date:** December 30, 2025 
**Author:** Student

---

## Executive Summary

K-means clustering identified **3 natural market segments** in the Airbnb data. The segments represent distinct listing types with different pricing, availability, and review patterns.

---

## 1. Clustering Objective

**Method:** K-means Clustering  
**Features Used:** price, minimum_nights, number_of_reviews, availability_365, reviews_per_month  
**Optimal K:** 3 clusters ✓  
**Sample Size:** Entire dataset

---

## 2. Optimal K Selection

### Silhouette Score Analysis
**K=3 selected as optimal** based on:
- Elbow method indicates diminishing returns after K=3
- Silhouette score peaks at K=3
- Good cluster separation and cohesion

---

## 3. Cluster Profiles

### Cluster 0: Budget High-Volume
**Size:** Significant portion of market

**Characteristics:**
- Low to moderate pricing
- High availability and reviews
- Volume-focused strategy

**Business Strategy:** Price competitively, maintain availability, encourage reviews

---

### Cluster 1: Popular Mid-Range
**Size:** Main market segment

**Characteristics:**
- Mid-range pricing
- Balanced availability and reviews
- Quality-focused approach

**Business Strategy:** Maintain quality, consistent marketing, competitive pricing

---

### Cluster 2: Premium Exclusive
**Size:** Smaller premium segment

**Characteristics:**
- High pricing
- Selective availability
- Fewer but high-value bookings

**Business Strategy:** Premium positioning, selective screening, quality service

---

## 4. Market Insights

### Key Findings
- **Market Segmentation:** Three distinct strategies identified
- **Price-Review Relationship:** Inverse relationship between price and review volume
- **Availability Strategy:** Premium listings maintain lower availability
- **Volume vs. Value:** Budget segment prioritizes volume; premium prioritizes price

---

## 5. Cluster Validation

**Silhouette Score:** Positive (clusters well-separated)  
**Davies-Bouldin Index:** Reasonable (clusters distinct)  
**Assessment:** Clusters are valid and interpretable ✓

---

## 6. Recommendations

### For Hosts
1. Identify your cluster position
2. Optimize strategy for your cluster
3. Consider property upgrades to move up tiers

### For Platform
1. Provide segment-specific tools
2. Cluster-based recommendations
3. Targeted marketing strategies

### For Investors
1. Diversify across clusters
2. Analyze cluster economics
3. Strategic positioning

---

## Conclusion

Three distinct market segments identified through clustering analysis. Each segment represents different hosting strategies and business models. Actionable insights for all stakeholders.