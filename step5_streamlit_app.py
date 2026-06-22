import streamlit as st
import pandas as pd

st.set_page_config(page_title="ClaimCheck Dashboard", layout="wide")

# Load the flagged claims data
df = pd.read_csv("flagged_claims.csv")

st.title("📊 ClaimCheck – Medical Billing Anomaly Detector")

# Show basic stats
st.markdown("### 📌 Summary")
st.write(f"Total Claims: {len(df)}")
st.write(f"High Cost Flags (Claims whose billed amount is far higher than normal): {df['High_Cost_Flag'].sum()}")
st.write(f"Duplicate Flags (Claim that repeats another with the same patient, provider, date): {df['Duplicate_Flag'].sum()}")
st.write(f"Mismatch Flags (Claim where diagnosis code and procedure code don't belong together): {df['Mismatch_Flag'].sum()}")

# Sidebar filter
st.sidebar.header("🔍 Filter Flags")
selected_flags = st.sidebar.multiselect(
    "Select Flag Types",
    ["High_Cost_Flag", "Duplicate_Flag", "Mismatch_Flag"],
    default=["High_Cost_Flag", "Duplicate_Flag", "Mismatch_Flag"]
)

# Filter by selected flags
if selected_flags:
    filtered_df = df[df[selected_flags].any(axis=1)]
else:
    filtered_df = df.copy()

st.markdown("### 🧾 Flagged Claims Table")

# Display with description columns
columns_to_show = [
    "Claim_ID", "Patient_ID", "Provider_ID", "Claim_Date",
    "Diagnosis_Code", "Diagnosis_Description",
    "Procedure_Code", "Procedure_Description",
    "Claim_Amount", "High_Cost_Flag", "Duplicate_Flag", "Mismatch_Flag"
]

st.dataframe(filtered_df[columns_to_show])
