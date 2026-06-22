import pandas as pd

df = pd.read_csv("cleaned_claims.csv")

procedure_name_map = {
    "PROC1001": "Standard Office Visit",
    "PROC1002": "Basic Blood Work Panel",
    "PROC1003": "Chest X-Ray",
    "PROC2001": "CT Scan – Abdomen",
    "PROC2002": "MRI – Brain",
    "PROC3001": "Laparoscopic Appendectomy",
    "PROC9999": "Emergency Room Evaluation"
}

diagnosis_name_map = {
    "D001": "Type 2 Diabetes Mellitus",
    "D002": "Primary Hypertension",
    "D003": "Mild Persistent Asthma",
    "D004": "Closed Femur Fracture",
    "D099": "Diagnosis Not Otherwise Specified"
}

def proc_desc(code: str) -> str:
    return procedure_name_map.get(code, f"Unmapped procedure: {code}")

def diag_desc(code: str) -> str:
    return diagnosis_name_map.get(code, f"Unmapped diagnosis: {code}")

df["Procedure_Description"] = df["Procedure_Code"].apply(proc_desc)
df["Diagnosis_Description"]  = df["Diagnosis_Code"].apply(diag_desc)

df.to_csv("cleaned_claims_with_desc.csv", index=False)

print("✅ Added descriptions → cleaned_claims_with_desc.csv")
