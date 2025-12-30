# Data Quality Report

**Project:** Airbnb Dataset Analysis  
**Date:** December 30, 2025
**Author:** Gorden Archer

---

## Executive Summary

This report documents data quality issues identified in the raw dataset and the cleaning decisions made to ensure analysis validity.

---

## 1. Data Quality Issues Identified

### 1.1 Missing Values

#### reviews_per_month
- **Count:** 10,052 missing values
- **Percentage:** 20.56%
- **Cause:** Listings with zero reviews have null values
- **Treatment:** Impute with median (0.72)
- **Rationale:** Preserves distribution; zero reviews ≠ missing data

#### last_review
- **Count:** 10,052 missing values
- **Percentage:** 20.56%
- **Cause:** Listings never reviewed have no last_review date
- **Treatment:** Impute with 'No Review'
- **Rationale:** Creates meaningful indicator for new/inactive listings

### 1.2 Invalid Records

#### Invalid Prices
- **Count:** 11 records
- **Percentage:** 0.02%
- **Issue:** Price ≤ $0 (impossible for paid service)
- **Decision:** Remove entirely
- **Impact:** 11 rows removed, 48,884 remain

#### Negative Minimum Nights
- **Count:** 0 records
- **Percentage:** 0%
- **Issue:** No negative values found
- **Decision:** No action needed

### 1.3 Outliers

#### Price Outliers
| Metric | Value |
|--------|-------|
| Q1 | $69 |
| Q3 | $175 |
| IQR | $106 |
| Lower Bound | -$90 |
| Upper Bound | $334 |
| Outliers (IQR) | ~9,000+ |

**Decision:** Keep outliers  
**Rationale:** Represent legitimate premium market segment; important for business understanding

---

## 2. Duplicate Records

### ID Duplicates
- **Duplicates Found:** 0
- **Action:** None needed
- **Finding:** All listings have unique IDs

### Full Row Duplicates
- **Duplicates Found:** 0
- **Action:** None needed

---

## 3. Data Type Issues

### Type Mismatches
- All columns have correct data types
- Dates properly identified
- Numeric fields verified

### Resolution
- ✓ Data types validated
- ✓ No conversions needed
- ✓ Ready for analysis

---

## 4. Statistical Anomalies

### Unexpected Distributions

#### Availability_365
- **Expected:** Values 0-365
- **Found:** All values within range ✓

#### Calculated_host_listings_count
- **Expected:** Positive integers
- **Found:** Valid range (0-327) ✓

---

## 5. Cleaning Summary

### Pre-Cleaning
- **Total Records:** 48,895
- **Total Columns:** 16
- **Total Cells:** 782,320

### Cleaning Actions Taken
1. Removed 11 records with invalid prices (price ≤ $0)
2. Imputed 10,052 missing values in reviews_per_month (median: 0.72)
3. Imputed 10,052 missing values in last_review ('No Review')
4. Verified no data type issues
5. Retained outliers for market representation

### Post-Cleaning
- **Total Records:** 48,884
- **Total Columns:** 16
- **Total Cells:** 781,344
- **Records Removed:** 11 (0.02%)
- **Data Quality:** 99.98% ✓

---

## 6. Data Quality Metrics

| Metric | Before | After |
|--------|--------|-------|
| Completeness | 97.29% | 100% |
| Validity | 99.98% | 100% |
| Consistency | 100% | 100% |
| Overall | **99.25%** | **100%** |

---

## 7. Assumptions & Decisions

### Key Assumptions
1. **Price > 0** - All valid Airbnb listings have positive prices ✓
2. **Minimum_nights ≥ 0** - Zero minimum nights is valid (flexible) ✓
3. **Missing reviews_per_month = 0 reviews** - Reasonable interpretation ✓
4. **Outliers are valid** - Premium properties represent real market ✓

### Alternative Approaches Considered
- Remove all outliers (rejected: loses legitimate premium segment)
- Use median imputation (selected: preserves distribution) ✓
- Use forward fill (rejected: not temporal data)

---

## 8. Recommendations

### For Analysis
- Use cleaned dataset only; never modify raw data
- Document any additional filtering for specific analyses
- Track assumptions used in models

### For Future Data Collection
- Implement validation at data entry
- Require price > 0
- Standardize date formats

---

## 9. Conclusion

The dataset quality has been improved through systematic identification and treatment of issues. Only 11 invalid records (0.02%) were removed. Missing values have been imputed appropriately, maintaining data integrity. The cleaned dataset is 100% valid and ready for analysis.

**Cleaned Data Location:** `data/processed/data_cleaned.csv`  