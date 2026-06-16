import joblib
import pandas as pd
import os


print("CUSTOMER BEHAVIOR ANALYTICS SYSTEM INTERFACE")
print("Task ID: ML-INT-1 | Intern Ref ID: TC-INT-18991230-816")


base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, 'best_rf_model.pkl')
features_path = os.path.join(base_dir, 'model_features.pkl')

if not os.path.exists(model_path):
    print(" Error: Run your notebooks/churn_analysis.ipynb file first to export model components!")
    exit()

model = joblib.load(model_path)
model_features = joblib.load(features_path)
print(" Light Predictive Engine Assets Synced Successfully!\n")

while True:
    print("--- Run a Live Customer Simulation ---")
    try:
        tenure = float(input("Enter Customer Tenure in Months (e.g., 12): "))
        monthly_charges = float(input("Enter Monthly Charges in $ (e.g., 65.5): "))
        support_count = float(input("Enter Tech Support Add-ons Count (0 to 4): "))
        is_auto = input("Is payment automatic? (yes/no): ").strip().lower()
        
        # Build evaluation vector matching model structure precisely
        input_row = pd.DataFrame(0, index=[0], columns=model_features)
        if 'tenure' in input_row.columns: input_row['tenure'] = tenure
        if 'MonthlyCharges' in input_row.columns: input_row['MonthlyCharges'] = monthly_charges
        if 'SupportInteractionCount' in input_row.columns: input_row['SupportInteractionCount'] = support_count
        if 'IsAutomaticPayment' in input_row.columns: input_row['IsAutomaticPayment'] = 1 if is_auto == 'yes' else 0
        
        prob = model.predict_proba(input_row)[0][1]
        category = "Low Risk Profile" if prob < 0.30 else "Medium Risk Profile" if prob < 0.65 else "High Risk Profile"
            
        print(f"\n Prediction Result:")
        print(f"-> Predicted Churn Risk Probability: {prob*100:.2f}%")
        print(f"-> Operational Risk Designation: {category}\n")
    except ValueError:
        print(" Invalid entry numerical format. Please retry.")
        
    cont = input("Simulate another customer? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("\nExiting interface system. Good luck with your task submission!")
        break