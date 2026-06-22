import pandas as pd

# Load flagged claims
df = pd.read_csv("flagged_claims.csv")

# Show only rows where any flag is True
alerts = df[(df["High_Cost_Flag"]) | (df["Duplicate_Flag"]) | (df["Mismatch_Flag"])]

# Display the suspicious claims
if not alerts.empty:
    print("🚨 Suspicious Claims Detected:\n")
    print(alerts[["Claim_ID", "Patient_ID", "Provider_ID", "Claim_Amount", "Diagnosis_Code", "Procedure_Code", "High_Cost_Flag", "Duplicate_Flag", "Mismatch_Flag"]])
else:
    print("✅ No suspicious claims found.")
