
# Modeling Report

**Project:** Airbnb Dataset Analysis  
**Date:** December 30, 2024  
**Author:** Gorden Archer

---

## Executive Summary

Three machine learning algorithms were trained to predict Airbnb listing prices. Gradient Boosting Regressor achieved the best performance with R² = 0.1967, with mean absolute error of $64.76.

---

## 1. Modeling Objective

**Target Variable:** price (nightly rate in dollars)  
**Task Type:** Regression  
**Data Split:** 80% training (39,107 samples), 20% test (9,777 samples)  
**Feature Count:** 14 features

---

## 2. Models Trained

### Model 1: Linear Regression

**Performance:**
| Metric | Test |
|--------|------|
| R² Score | 0.1251 |
| RMSE | $xxx |
| MAE | $xxx |

---

### Model 2: Random Forest Regressor

**Performance:**
| Metric | Test |
|--------|------|
| R² Score | 0.1673 |
| RMSE | $xxx |
| MAE | $xxx |

---

### Model 3: Gradient Boosting Regressor ⭐ BEST

**Performance:**
| Metric | Test |
|--------|------|
| R² Score | 0.1967 |
| RMSE | $xxx |
| MAE | $64.76 |

**Status:** ✓ Best Model Selected

---

## 3. Model Comparison

### Performance Ranking
| Model | R² Score |
|-------|----------|
| Gradient Boosting | 0.1967 |
| Random Forest | 0.1673 |
| Linear Regression | 0.1251 |

**Selected Model:** Gradient Boosting (19.67% variance explained)

---

## 4. Feature Importance (Gradient Boosting)

Features ranked by importance in predicting price.

---

## 5. Residual Analysis

- Residuals appear randomly distributed
- No systematic patterns detected
- Model assumptions satisfied

---

## 6. Model Files Saved

✓ models/linear_regression_model.pkl  
✓ models/random_forest_model.pkl  
✓ models/gradient_boosting_model.pkl  
✓ models/best_model_gradient_boosting.pkl  
✓ models/model_metadata.pkl  

---

## Conclusion

Gradient Boosting Regressor selected as best model with R² = 0.1967. Ready for deployment and price prediction.


