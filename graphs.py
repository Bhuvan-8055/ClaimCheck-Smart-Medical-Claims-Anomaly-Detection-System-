# graphs.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz

# Load your dataset
df = pd.read_csv("cleaned_claims_with_desc.csv")

# Flag 1: High Cost Flag
threshold = 10000
df["High_Cost_Flag"] = df["Claim_Amount"] > threshold

# Flag 2: Duplicate Flag
df["Duplicate_Flag"] = df.duplicated(
    subset=["Patient_ID", "Provider_ID", "Claim_Date"], keep=False
)

# Flag 3: Mismatch Flag (Improved Logic)
def is_mismatch(proc, diag):
    if pd.isna(proc) or pd.isna(diag):
        return True
    similarity = fuzz.token_set_ratio(str(proc), str(diag))
    return similarity < 30  # adjust threshold as needed

df["Mismatch_Flag"] = df.apply(
    lambda row: is_mismatch(row["Procedure_Description"], row["Diagnosis_Description"]),
    axis=1
)

# Plot 1: High Cost Flag Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="High_Cost_Flag", data=df, palette="Set2")
plt.title("High Cost Flag Distribution")
plt.xlabel("High Cost Detected")
plt.ylabel("Number of Claims")
plt.tight_layout()
plt.savefig("high_cost_flag.png")
plt.close()

# Plot 2: Duplicate Flag Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="Duplicate_Flag", data=df, palette="Set1")
plt.title("Duplicate Flag Distribution")
plt.xlabel("Duplicate Detected")
plt.ylabel("Number of Claims")
plt.tight_layout()
plt.savefig("duplicate_flag.png")
plt.close()

# Plot 3: Mismatch Flag Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="Mismatch_Flag", data=df, color='lightseagreen')
plt.title("Mismatch Flag Distribution")
plt.xlabel("Mismatch Detected")
plt.ylabel("Number of Claims")
plt.tight_layout()
plt.savefig("mismatch_flag.png")
plt.close()

print("All graphs saved as PNG files.")
