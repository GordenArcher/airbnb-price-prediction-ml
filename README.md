

![Python](https://img.shields.io/badge/Python-3.13-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/airbnb-price-prediction-ml?style=social)](https://github.com/yourusername/airbnb-price-prediction-ml)


# Airbnb Dataset - Comprehensive Machine Learning Analysis

## Project Overview

This project performs a complete exploratory data analysis (EDA), data cleaning, feature engineering, and predictive modeling on the Airbnb dataset. The analysis includes multiple machine learning approaches to predict listing prices, identify market patterns, and segment listings into distinct clusters.

### Key Objectives
✓ Exploratory Data Analysis (EDA) with summary statistics and visualizations
✓ Data Quality Assessment and Cleaning
✓ Feature Engineering (10 new features created)
✓ Predictive Modeling using 3 different algorithms
✓ Model Evaluation and Comparison
✓ Unsupervised Learning (K-means Clustering for market segmentation)
✓ Clear documentation of assumptions and methodological choices

## Project Structure

```
Airbnb_Analysis_Project/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore file
├── venv/                              # Environment variable
├── notebooks/
│   └── Airbnb_Complete_Analysis.ipynb # Main Jupyter notebook with all analysis
│
├── data/
│   ├── raw/
│   │   └── MinoAI dataset.csv         # Original dataset (DO NOT MODIFY)
│   └── processed/
│       ├── data_cleaned.csv           # Cleaned dataset
│       └── data_engineered.csv        # Dataset with engineered features
│
├── src/                               # (Optional) Modularized code
│   ├── __init__.py
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   ├── clustering.py
│   └── utils.py
│
├── models/                            # Trained models (pkl files)
│   ├── linear_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── gradient_boosting_model.pkl
│   ├── best_model_gradient_boosting.pkl
│   └── model_metadata.pkl
│
├── visualizations/                    # Generated charts and plots
│   ├── eda/
│   │   ├── 01_missing_values.png
│   │   ├── 02_univariate_analysis.png
│   │   ├── 03_bivariate_analysis.png
│   │   └── 04_correlation_heatmap.png
│   ├── modeling/
│   │   ├── 01_model_comparison.png
│   │   ├── 02_predictions_vs_actual.png
│   │   └── 03_feature_importance.png
│   └── clustering/
│       ├── 01_elbow_and_silhouette.png
│       └── 02_cluster_distributions.png
│
└── reports/            
    ├── 01_EDA_Report.md
    ├── 02_Data_Quality_Report.md
    ├── 03_Feature_Engineering_Report.md
    ├── 04_Modeling_Report.md
    └── 05_Clustering_Report.md
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- pip (Python package manager)

### Step 1: Clone or Download Project
```bash
cd Airbnb_Analysis_Project
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Place Dataset
- Place `MinoAI dataset.csv` in the `data/raw/` folder

### Step 5: Run Analysis
```bash
jupyter notebook
# Open: notebooks/Airbnb_Complete_Analysis.ipynb
# Run all cells sequentially
```

## Key Findings

### Dataset Characteristics
- **Total Listings:** 48,895
- **Features Analyzed:** 16 original + 10 engineered = 26 total
- **Data Quality:** 99.5% complete after cleaning

### Price Analysis
- **Mean Price:** $152.72
- **Median Price:** $107.00
- **Price Range:** $1 - $10,000+
- **Distribution:** Right-skewed (premium properties pull average up)

### Best Predictive Model
- **Algorithm:** Gradient Boosting Regressor
- **Test R² Score:** ~0.70 (explains 70% of price variance)
- **Prediction Error (MAE):** ~$45
- **Top 3 Features:** Room Type, Neighbourhood, Host Listings Count

### Market Segmentation
- **Natural Clusters:** 3 distinct market segments
- **Cluster 1:** Budget listings (high availability, low reviews)
- **Cluster 2:** Popular/mid-range (moderate reviews, varied prices)
- **Cluster 3:** Premium/exclusive (high price, low availability)

## Analysis Phases

### Phase 1: Exploratory Data Analysis (EDA)
- Summary statistics for all variables
- Distribution analysis (univariate & bivariate)
- Correlation analysis
- Missing value assessment
- Visual exploration with 9+ charts

### Phase 2: Data Quality Assessment
- Identified 9+ data quality issues
- Documented cleaning decisions
- Removed invalid records (price ≤ 0)
- Imputed missing values appropriately

### Phase 3: Feature Engineering
10 new features created:
1. `has_reviews` - Binary indicator of listing activity
2. `days_since_review` - Time-based engagement metric
3. `price_category` - Market segment classification
4. `availability_level` - Availability tier
5. `host_experience` - Host expertise level
6. `popularity_score` - Reviews per host listing
7. `room_type_encoded` - Numeric room type
8. `is_entire_home` - Entire property indicator
9. `host_multi_listing` - Host portfolio indicator
10. `neighbourhood_encoded` - Geographic encoding

### Phase 4: Predictive Modeling
**Three Algorithms Tested:**
1. **Linear Regression** - R² = 0.62 (baseline)
2. **Random Forest** - R² = 0.68 (robust, handles non-linearity)
3. **Gradient Boosting** - R² = 0.70 (best performer)

**Model Comparison:**
- Best model selected by R² score
- All models saved for future predictions
- Feature importance analysis provided

### Phase 5: Clustering & Market Segmentation
- Optimal K selection using elbow method & silhouette score
- K=3 identified as optimal
- Cluster characteristics analyzed
- Market segments profiled

## How to Use the Models

### Load and Make Predictions
```python
import pickle
import pandas as pd

# Load best model
with open('models/best_model_gradient_boosting.pkl', 'rb') as f:
    best_model = pickle.load(f)

# Load metadata
with open('models/model_metadata.pkl', 'rb') as f:
    metadata = pickle.load(f)

# Load scaler for feature scaling
scaler = metadata['scaler']
feature_names = metadata['feature_names']

# Prepare new data (must have all required features)
new_data = pd.DataFrame({...})  # Your new listing data
new_data_scaled = scaler.transform(new_data[feature_names])

# Make prediction
predicted_price = best_model.predict(new_data_scaled)
print(f"Predicted Price: ${predicted_price[0]:.2f}")
```

## Key Assumptions & Limitations

### Assumptions Made
✓ Price > $0 assumed valid (removed invalid records)
✓ Missing `reviews_per_month` imputed with median
✓ Reference date assumed: 2024-12-31
✓ Train-test split random_state=42 for reproducibility
✓ Outliers retained (represent market diversity)
✓ Linear relationships acceptable for initial modeling

### Limitations
⚠ Model R² = 0.70 (30% variance unexplained - other factors exist)
⚠ Temporal patterns not analyzed (seasonality, trends)
⚠ External factors not included (events, competition, reviews text)
⚠ Geographic precision limited to neighbourhood groups
⚠ Does not capture host reputation/review quality
⚠ Static analysis (snapshot in time)

## Further Analysis Opportunities

→ **Temporal Analysis:** Seasonality patterns, trend analysis
→ **Text Analysis:** Review sentiment analysis for quality assessment
→ **Host Performance:** Churn prediction, growth modeling
→ **Price Optimization:** Dynamic pricing recommendations
→ **Anomaly Detection:** Unusual listing identification
→ **Advanced Modeling:** Neural networks, ensemble stacking

## Technologies Used

- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Statistical Analysis:** SciPy
- **Notebook:** Jupyter/JupyterLab

## Model Performance Metrics

| Model | Train R² | Test R² | RMSE | MAE |
|-------|----------|---------|------|-----|
| Linear Regression | 0.62 | 0.62 | $89 | $52 |
| Random Forest | 0.95 | 0.68 | $78 | $48 |
| Gradient Boosting | 0.73 | 0.70 | $75 | $45 |

**Best Model:** Gradient Boosting (best test R², good generalization)

## File Descriptions

- `notebooks/Airbnb_Complete_Analysis.ipynb` - Complete analysis in 17 cells
- `data/raw/MinoAI dataset.csv` - Original untouched dataset
- `data/processed/data_cleaned.csv` - After cleaning (removed invalid records)
- `data/processed/data_engineered.csv` - With engineered features
- `models/*.pkl` - Trained model files for predictions
- `visualizations/eda/` - Exploratory data analysis charts
- `visualizations/modeling/` - Model evaluation visualizations
- `visualizations/clustering/` - Clustering analysis plots

## Author
[Your Name]

## Date
[Project Date]

## License
This project is for educational purposes.

## Questions or Feedback?
For questions about the analysis, refer to the detailed comments in the Jupyter notebook or review the generated visualizations in the `visualizations/` folder.

---

### Generated Files Count
- **Processed Data Files:** 2
- **Trained Models:** 5
- **Visualizations:** 9
- **Total Outputs:** 16+

All files automatically generated upon running the notebook.
```

---

