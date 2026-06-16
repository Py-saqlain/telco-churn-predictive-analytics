# Telco Customer Churn Analytics System

A comprehensive machine learning pipeline and interactive command-line interface (CLI) built to predict telecom subscriber churn risks and estimate financial revenue impact using a Random Forest ensemble model.

## 🛠️ Tech Stack
* **Core Language & Runtime:** Python 3.13 (Isolated local Virtual Environment `venv`)
* **Data Processing & Engineering:** pandas, numpy
* **Machine Learning Engine:** scikit-learn (Random Forest Classifier, Logistic Regression)
* **Data Visualization:** seaborn, matplotlib
* **Model Serialization:** joblib

## 📁 Project Structure
```text
telco-customer-churn-analytics/
├── app/
│   ├── best_rf_model.pkl         # Serialized Random Forest model binary
│   ├── model_features.pkl        # Serialized tracking features list
│   └── insights_viewer.py        # Interactive CLI customer simulation engine
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn teyzix.csv  # Cleansed baseline dataset
├── notebooks/
│   └── churn_analysis.ipynb      # Main Jupyter notebook processing pipeline
├── README.md                     # Documentation file
└── requirements.txt              # Project environment dependencies
Execution Guide
1. Setup Environment Dependencies
