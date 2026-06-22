import pandas as pd

# Load the enriched data with descriptions
df = pd.read_csv("cleaned_claims_with_desc.csv")

# 1. Flag high-cost procedures (above 90th percentile)
cost_threshold = df["Claim_Amount"].quantile(0.90)
df["High_Cost_Flag"] = df["Claim_Amount"] > cost_threshold

# 2. Detect duplicate claims (same patient, provider, and date)
df["Duplicate_Flag"] = df.duplicated(
    subset=["Patient_ID", "Provider_ID", "Claim_Date"],
    keep=False
)

# 3. Diagnosis-procedure mismatch logic
mismatch_conditions = (
    ((df["Diagnosis_Code"] == "D001") & (df["Procedure_Code"] != "PROC1001")) |
    ((df["Diagnosis_Code"] == "D002") & (df["Procedure_Code"] != "PROC1002")) |
    ((df["Diagnosis_Code"] == "D003") & (df["Procedure_Code"] != "PROC1003")) |
    ((df["Diagnosis_Code"] == "D004") & (df["Procedure_Code"] != "PROC2001")) |
    ((df["Diagnosis_Code"] == "D099") & (df["Procedure_Code"] != "PROC9999"))
)
df["Mismatch_Flag"] = mismatch_conditions

# Save the updated dataset with flags and descriptions
df.to_csv("flagged_claims.csv", index=False)

print("✅ Anomalies flagged and saved to flagged_claims.csv")

