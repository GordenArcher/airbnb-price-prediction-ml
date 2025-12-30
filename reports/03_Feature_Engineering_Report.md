
# Feature Engineering Report

**Project:** Airbnb Dataset Analysis  
**Date:** December 30, 2025 
**Author:** Gorden Archer

---

## Executive Summary

10 new features were engineered to improve model performance and provide business insights. Features were derived from existing data to capture domain knowledge and create meaningful representations.

---

## Features Created

### 1. has_reviews (Binary)

**Purpose:** Indicator of listing activity and popularity  
**Type:** Binary (0/1)  
**Distribution:**
- 0 (No Reviews): Multiple listings
- 1 (Has Reviews): Most listings active

**Business Use:** Identifies active vs. inactive listings

---

### 2. days_since_review (Numeric)

**Purpose:** Measure recency of engagement  
**Type:** Integer (days)  
**Statistics:**
- Captures time since last guest interaction
- -1 for listings with no reviews

**Business Use:** Recent reviews indicate active, well-managed listings

---

### 3. price_category (Categorical)

**Purpose:** Segment market into meaningful price tiers  
**Type:** Categorical (5 levels)  
**Bins:**
- Budget: $0-50
- Economy: $50-100
- Mid-Range: $100-200
- Premium: $200-500
- Luxury: $500+

**Business Use:** Enables segment-specific analysis and strategies

---

### 4. availability_level (Categorical)

**Purpose:** Classify listing availability patterns  
**Type:** Categorical (4 levels)  
**Bins:**
- Low: 0-30 days
- Medium-Low: 30-100 days
- Medium-High: 100-300 days
- High: 300-365 days

**Business Use:** Low availability may indicate high demand/premium positioning

---

### 5. host_experience (Categorical)

**Purpose:** Classify host expertise level based on portfolio size  
**Type:** Categorical (4 levels)  
**Bins:**
- New: 1 listing
- Growing: 2-3 listings
- Established: 4-10 listings
- Power: 10+ listings

**Business Use:** Experienced hosts may command better prices or quality

---

### 6. popularity_score (Numeric)

**Purpose:** Measure individual listing popularity relative to host portfolio  
**Type:** Float  
**Calculation:** reviews / (host_listings + 1)

**Business Use:** Popular listings within host portfolio command attention

---

### 7. room_type_encoded (Numeric)

**Purpose:** Numeric encoding of categorical room type for models  
**Type:** Integer  
**Mapping:**
- Entire home/apt: 0
- Hotel room: 1
- Private room: 2
- Shared room: 3

**Business Use:** Enables room type in numeric models

---

### 8. is_entire_home (Binary)

**Purpose:** Key differentiator for price predictions  
**Type:** Binary (0/1)  

**Impact:** Entire homes are primary price driver

**Business Use:** Strongest single predictor of price

---

### 9. host_multi_listing (Binary)

**Purpose:** Identify hosts with multiple properties  
**Type:** Binary (0/1)  

**Business Use:** Portfolio hosts may have economies of scale

---

### 10. neighbourhood_encoded (Numeric)

**Purpose:** Numeric encoding of geography for models  
**Type:** Integer  

**Business Use:** Enables location in numeric models

---

## Summary

**Original Columns:** 16  
**New Columns:** 27 (16 original + 10 engineered)  
**Features Ready for Modeling:** ✓ Yes

---

## Conclusion

10 engineered features have been created to enhance the dataset for analysis and modeling. Ready for use in predictive modeling and clustering analysis.

**Engineered Data Location:** `data/processed/data_engineered.csv`  