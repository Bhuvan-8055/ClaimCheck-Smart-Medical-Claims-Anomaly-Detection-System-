import pandas as pd

# Step 1: Load the medical claims data from Excel
df = pd.read_excel("clean_medical_claims_sample.csv.xlsx")

# Show the first 5 rows
print("✅ Data Loaded Successfully!")
print(df.head())
