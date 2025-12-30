"""
Modeling Module
Functions for building and evaluating models
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

def prepare_modeling_data(df, feature_cols, target_col='price', test_size=0.2, random_state=42):
    """
    Prepare data for modeling
    
    Args:
        df (pd.DataFrame): Input data
        feature_cols (list): Feature column names
        target_col (str): Target column name
        test_size (float): Test set ratio
        random_state (int): Random seed
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test, scaler)
    """
    df_model = df[feature_cols + [target_col]].dropna()
    
    X = df_model[feature_cols]
    y = df_model[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\nData Prepared for Modeling:")
    print(f"  Training set: {X_train.shape[0]:,} samples")
    print(f"  Test set: {X_test.shape[0]:,} samples")
    print(f"  Features: {X_train.shape[1]}")
    
    return X_train, X_test, X_train_scaled, X_test_scaled, y_train, y_test, scaler


def build_models(X_train, X_test, X_train_scaled, X_test_scaled, y_train, y_test):
    """
    Build and evaluate multiple models
    
    Args:
        X_train, X_test: Feature data
        X_train_scaled, X_test_scaled: Scaled feature data
        y_train, y_test: Target data
        
    Returns:
        dict: Model results
    """
    model_results = {}
    
    print("\nBuilding Models:")
    
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    y_pred_lr = lr_model.predict(X_test_scaled)
    r2_lr = r2_score(y_test, y_pred_lr)
    
    model_results['Linear Regression'] = {
        'model': lr_model,
        'predictions': y_pred_lr,
        'r2': r2_lr,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_lr)),
        'mae': mean_absolute_error(y_test, y_pred_lr)
    }
    print(f"  ✓ Linear Regression - R²: {r2_lr:.4f}")
    
    rf_model = RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    r2_rf = r2_score(y_test, y_pred_rf)
    
    model_results['Random Forest'] = {
        'model': rf_model,
        'predictions': y_pred_rf,
        'r2': r2_rf,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_rf)),
        'mae': mean_absolute_error(y_test, y_pred_rf),
        'feature_importance': rf_model.feature_importances_
    }
    print(f"  ✓ Random Forest - R²: {r2_rf:.4f}")
    

    gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
    gb_model.fit(X_train, y_train)
    y_pred_gb = gb_model.predict(X_test)
    r2_gb = r2_score(y_test, y_pred_gb)
    
    model_results['Gradient Boosting'] = {
        'model': gb_model,
        'predictions': y_pred_gb,
        'r2': r2_gb,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_gb)),
        'mae': mean_absolute_error(y_test, y_pred_gb),
        'feature_importance': gb_model.feature_importances_
    }
    print(f"  ✓ Gradient Boosting - R²: {r2_gb:.4f}")
    
    return model_results


def evaluate_models(model_results):
    """
    Evaluate and compare models
    
    Args:
        model_results (dict): Model results dictionary
        
    Returns:
        str: Best model name
    """
    print("\nModel Comparison:")
    print(f"{'Model':<20} {'R² Score':<12} {'RMSE':<12} {'MAE':<12}")
    print("-" * 56)
    
    best_model = None
    best_r2 = -1
    
    for name, results in model_results.items():
        print(f"{name:<20} {results['r2']:<12.4f} ${results['rmse']:<11.2f} ${results['mae']:<11.2f}")
        if results['r2'] > best_r2:
            best_r2 = results['r2']
            best_model = name
    
    print(f"\n✓ Best Model: {best_model} (R²: {best_r2:.4f})")
    return best_model


def save_models(model_results, best_model_name, output_dir='models'):
    """
    Save trained models to pickle files
    
    Args:
        model_results (dict): Model results
        best_model_name (str): Name of best model
        output_dir (str): Output directory
    """
    print(f"\nSaving Models:")
    
    for name, results in model_results.items():
        model = results['model']
        filename = f"{output_dir}/{name.lower().replace(' ', '_')}_model.pkl"
        with open(filename, 'wb') as f:
            pickle.dump(model, f)
        print(f"  ✓ Saved: {filename}")

