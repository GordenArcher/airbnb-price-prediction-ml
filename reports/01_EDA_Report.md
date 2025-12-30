# Exploratory Data Analysis Report

**Project:** Airbnb Dataset Analysis  
**Date:** December 30, 2025 
**Author:** Gorden Archer

---

## Executive Summary

This report documents the exploratory data analysis (EDA) performed on the Airbnb dataset. The analysis includes data overview, distribution analysis, correlation analysis, and pattern discovery.

---

## 1. Dataset Overview

### Dimensions
- **Total Records:** 48,895 listings
- **Total Features:** 16 variables
- **Data Types:** 10 numeric, 6 categorical
- **Memory Usage:** ~3.85 MB

### Feature Descriptions

| Feature | Type | Description |
|---------|------|-------------|
| id | Integer | Unique listing identifier |
| name | String | Listing name |
| host_id | Integer | Host identifier |
| host_name | String | Host name |
| neighbourhood_group | String | Neighbourhood group |
| neighbourhood | String | Specific neighbourhood |
| latitude | Float | Geographic latitude |
| longitude | Float | Geographic longitude |
| room_type | String | Type of room (Entire/Private/Shared) |
| price | Integer | Nightly price in dollars |
| minimum_nights | Integer | Minimum stay requirement |
| number_of_reviews | Integer | Total reviews received |
| last_review | String | Date of most recent review |
| reviews_per_month | Float | Average monthly reviews |
| calculated_host_listings_count | Integer | Number of listings by host |
| availability_365 | Integer | Days available per year |

---

## 2. Missing Values Analysis

### Summary
- **Total Missing Values:** 20,104
- **Percentage of Dataset:** 2.71%
- **Most Affected Column:** reviews_per_month (20.56%)

### Missing Value Details

| Column | Missing Count | Missing % | Treatment |
|--------|---------------|-----------|-----------|
| reviews_per_month | 10,052 | 20.56% | Impute with median |
| last_review | 10,052 | 20.56% | Impute with 'No Review' |
| host_name | 21 | 0.04% | Keep as is |
| name | 16 | 0.03% | Keep as is |

### Rationale
- **reviews_per_month:** Missing values indicate zero reviews. Median imputation preserves distribution.
- **last_review:** Missing indicates no reviews. Created indicator for missing pattern.
- **host_name & name:** Minimal missing; negligible impact on analysis.

---

## 3. Descriptive Statistics

### Numeric Variables

#### Price
```
Count:    48,895
Mean:     $152.72
Median:   $106.00
Std Dev:  $240.15
Min:      $0.00
Max:      $10,000.00
Q1:       $69.00
Q3:       $175.00
```

**Observations:**
- Highly right-skewed distribution (mean > median)
- Mean > Median indicates premium outliers pulling average up
- Wide range ($0-$10,000) suggests diverse market segments
- Standard deviation ($240.15) nearly 1.5x mean indicates high variability

#### Minimum Nights
```
Count:    48,895
Mean:     7.03 days
Median:   3.00 days
Std Dev:  20.51 days
Min:      1 day
Max:      1,250 days
```

**Observations:**
- Most listings flexible (median = 3 days)
- Long-term rentals present (max = 1,250 days / 3+ years)
- High standard deviation indicates varied host strategies

#### Number of Reviews
```
Count:    48,895
Mean:     23.27 reviews
Median:   5.00 reviews
Std Dev:  44.55 reviews
Min:      0 reviews
Max:      629 reviews
```

**Observations:**
- Many new/inactive listings (median = 5, mean = 23.27 suggests right-skew)
- Popular listings with 600+ reviews exist
- Highly variable engagement levels

#### Availability (365 days)
```
Count:    48,895
Mean:     112.78 days
Median:   45.00 days
Std Dev:  108.35 days
Min:      0 days
Max:      365 days
```

**Observations:**
- High variance indicates diverse host availability strategies
- Some fully booked listings (0 days available)
- Some always available (365 days)
- Bimodal distribution (either always available or selectively available)

### Categorical Variables

#### Room Type Distribution
| Room Type | Observation |
|-----------|------------|
| Entire home/apt | Most common type |
| Private room | Second most common |
| Shared room | Less common |
| Hotel room | Rare |

**Key Finding:** Entire homes dominate the market, representing the majority of listings

#### Neighbourhood Group Distribution
Multiple neighbourhoods with significant geographic spread across New York City area

**Key Finding:** Geographic clustering evident; certain neighborhoods command premium pricing

---

## 4. Distribution Analysis

### Price Distribution
- **Shape:** Right-skewed
- **Skewness:** Positive (tail extends to right)
- **Outliers:** Top 5% priced above $550

**Insight:** Most listings cluster in budget-to-mid-range ($69-$175 IQR); luxury outliers pull distribution right.

### Reviews Distribution
- **Shape:** Right-skewed
- **Concentration:** 50% of listings have 1-24 reviews
- **Top performers:** Some listings have 600+ reviews

**Insight:** Few listings generate majority of reviews (Pareto principle evident).

### Availability Distribution
- **Shape:** Bimodal (two peaks)
- **Peak 1:** Near 0 (fully booked)
- **Peak 2:** Near 365 (always available)

**Insight:** Hosts use two distinct strategies: either selective (low availability) or volume-focused (high availability).

---

## 5. Correlation Analysis

### Correlation with Price

| Feature | Correlation |
|---------|-------------|
| minimum_nights | Positive |
| calculated_host_listings_count | Positive |
| availability_365 | Negative |
| number_of_reviews | Negative |
| reviews_per_month | Negative |

**Key Findings:**
- **Positive Correlation:** Minimum nights & host experience correlate with higher prices
- **Negative Correlation:** Higher reviews/availability suggest lower prices (popular budget options)
- **Interpretation:** Premium/exclusive listings have fewer reviews; budget listings driven by volume

### Multi-collinearity Check
- No high correlation (>0.9) between features
- Safe to use all features in modeling
- Features provide independent information

---

## 6. Bivariate Analysis

### Price by Room Type
- Entire homes command significant premium
- Clear price differentiation across room types
- Room type is major price driver

### Price by Neighbourhood
- Significant geographic variation
- Premium neighborhoods show 2-3x price premium
- Location is critical pricing factor

### Price vs Reviews
- **Correlation:** Negative
- **Interpretation:** Premium listings have fewer reviews; high-volume listings are cheaper
- **Business Implication:** Different market segments (premium vs. budget)

---

## 7. Key Patterns & Insights

### Market Segmentation
1. **Premium/Exclusive:** High price, low availability, few reviews
2. **Popular/Budget:** Lower price, high reviews, high availability
3. **Emerging:** New listings with few reviews, variable prices

### Availability Strategies
- Bimodal distribution reveals two distinct host philosophies
- Some hosts maximize occupancy; others maintain selectivity

---

## 8. Data Quality Summary

| Issue | Count | Impact |
|-------|-------|--------|
| Missing values | 20,104 | Low (will impute) |
| Duplicate records | 0 | None |
| Invalid prices | 11 | Will remove |
| Outliers (IQR) | ~10,000 | Retain for diversity |

---

## 9. Recommendations

### For Data Cleaning
- ✓ Remove invalid prices (≤ $0) → 11 records
- ✓ Impute missing reviews_per_month with median
- ✓ Impute last_review with 'No Review'
- ✓ Retain outliers for market representation

### For Feature Engineering
- ✓ Create binary: has_reviews
- ✓ Create categorical: price_range
- ✓ Create: days_since_review
- ✓ Create: host_experience_level

### For Modeling
- Focus on room_type and neighbourhood as key predictors
- Consider market segmentation (premium vs. budget)
- Explore non-linear models for price prediction

---

## 10. Conclusion

The Airbnb dataset shows a diverse market with clear segmentation by room type and geography. Price is driven primarily by property characteristics (entire vs. private) and location. The market contains both high-volume budget listings and premium exclusive properties, suggesting different host strategies and target audiences.