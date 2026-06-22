import pandas as pd

# Load the Excel data
df = pd.read_excel("clean_medical_claims_sample.csv.xlsx")

# 1. Drop completely empty rows
df.dropna(how="all", inplace=True)

# 2. Strip spaces from column names and values
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 3. Convert date column to datetime format
df["Claim_Date"] = pd.to_datetime(df["Claim_Date"], errors="coerce")

# 4. Drop rows with invalid or missing dates
df.dropna(subset=["Claim_Date"], inplace=True)

# 5. Drop duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned data to a new file
df.to_csv("cleaned_claims.csv", index=False)

print("✅ Data cleaned and saved to cleaned_claims.csv")
