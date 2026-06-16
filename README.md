# Project Submission: Telco Customer Churn Analytics System
# Task ID: ML-INT-1 | Intern Ref ID: TC-INT-18991230-816

---

## 1. Executive Summary & Tech Stack

### Task Description
Developed an end-to-end customer churn analytics pipeline using a Random Forest ensemble model to predict churn risks and estimate financial revenue impact. This implementation includes high-speed data engineering, exploratory visual analysis, and an interactive command-line interface (CLI) for real-time customer profile simulations.

### Tech Stack
* **Core Language & Runtime:** Python 3.13 (Isolated local Virtual Environment `venv`)
* **Data Processing & Engineering:** pandas, numpy
* **Machine Learning Engine:** scikit-learn (Random Forest Classifier, Logistic Regression)
* **Data Visualization:** seaborn, matplotlib
* **Model Serialization:** joblib
* **Operating System Environment:** Windows 10

---

## 2. Project Directory Structure

Ensure your local root folder is organized exactly as follows before generating your final submission archive:

```text
telco-customer-churn-analytics/
│
├── app/
│   ├── best_rf_model.pkl         # Trained Random Forest model binary (Serialized)
│   ├── model_features.pkl        # Serialized tracking features list (Binary)
│   └── insights_viewer.py        # Interactive CLI customer simulation engine
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn teyzix.csv  # Cleansed baseline dataset
│
├── notebooks/
│   └── churn_analysis.ipynb      # Main Jupyter notebook processing pipeline
│
├── README.md                     # Comprehensive system documentation
└── requirements.txt              # Project environment dependencies
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
