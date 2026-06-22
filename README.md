
# ClaimCheck – Smart Medical Claims Anomaly Detection System

## Overview

ClaimCheck is a rule-based healthcare analytics project designed to identify anomalies in medical claims data. The system automatically flags suspicious claims such as duplicate submissions, unusually high-cost procedures, and diagnosis–procedure mismatches. The objective is to reduce manual review effort, improve claim validation, and support fraud prevention in healthcare workflows.

---

## Problem Statement

Healthcare organizations process thousands of claims every day. Manual verification of these claims is time-consuming and prone to errors. Common issues include:

* Duplicate claim submissions
* Overbilling and unusually expensive procedures
* Incorrect diagnosis–procedure combinations
* Data entry and coding errors

ClaimCheck addresses these challenges through automated anomaly detection and interactive visualization.

---

## Dataset Description

A synthetic healthcare claims dataset was used to simulate real-world medical billing records.

### Dataset Attributes

| Column                | Description                          |
| --------------------- | ------------------------------------ |
| Claim_ID              | Unique claim identifier              |
| Patient_ID            | Unique patient identifier            |
| Provider_ID           | Healthcare provider identifier       |
| Procedure_Code        | Medical procedure code               |
| Procedure_Cost        | Cost of the procedure                |
| Diagnosis_Code        | Diagnosis identifier                 |
| Claim_Date            | Date of claim submission             |
| Claim_Amount          | Total claim amount                   |
| Procedure_Description | Human-readable procedure description |
| Diagnosis_Description | Human-readable diagnosis description |

---

## Methodology

### 1. Data Preprocessing

* Loaded claim records using Pandas
* Removed invalid or missing entries
* Standardized date formats
* Added descriptive mappings for diagnosis and procedure codes

### 2. High-Cost Claim Detection

Claims with amounts above the 90th percentile were flagged as potential overbilling cases.

**Logic:**

```python
threshold = df["Claim_Amount"].quantile(0.90)
df["High_Cost_Flag"] = df["Claim_Amount"] > threshold
```

### 3. Duplicate Claim Detection

Claims with identical:

* Patient_ID
* Provider_ID
* Claim_Date

were marked as duplicates.

**Logic:**

```python
df["Duplicate_Flag"] = df.duplicated(
    subset=["Patient_ID","Provider_ID","Claim_Date"],
    keep=False
)
```

### 4. Diagnosis–Procedure Mismatch Detection

Claims were checked for inconsistencies between diagnosis descriptions and procedure descriptions using rule-based validation.

Potential mismatches indicate coding errors or suspicious billing activity.

---

## System Architecture

```text
Medical Claims Dataset
          │
          ▼
Data Cleaning & Validation
          │
          ▼
Anomaly Detection Engine
 ├── High Cost Detection
 ├── Duplicate Detection
 └── Diagnosis-Procedure Validation
          │
          ▼
Flagged Claims Dataset
          │
          ▼
Streamlit Dashboard
```

---

## Implementation

### Technologies Used

* Python
* Pandas
* Streamlit
* Matplotlib
* Seaborn

### Key Features

* Automated anomaly detection
* Interactive claim review dashboard
* Human-readable diagnosis and procedure descriptions
* Visual analytics for anomaly patterns
* Exportable flagged claims dataset

---

## Results

The system successfully identified suspicious claims across three anomaly categories:

### High-Cost Claims

* Detected claims significantly above normal cost thresholds.
* Helps identify potential overbilling scenarios.

### Duplicate Claims

* Identified repeated claim submissions.
* Reduces duplicate reimbursements and processing errors.

### Diagnosis–Procedure Mismatches

* Flagged claims containing potentially inconsistent medical coding.
* Supports claim validation and audit workflows.

Approximately **12% of claims** were flagged as potentially suspicious during testing.

---

## Dashboard Features

The Streamlit dashboard provides:

* Claim-level anomaly review
* Filtering by anomaly type
* Procedure and diagnosis descriptions
* Summary statistics
* Interactive data exploration

---

## Future Enhancements

* Integration with PostgreSQL for large-scale claim storage
* Machine Learning–based anomaly detection using Isolation Forest
* Real ICD-10 and CPT code integration
* Real-time claim monitoring
* Fraud risk scoring system

---

## Conclusion

ClaimCheck demonstrates how rule-based anomaly detection can improve healthcare claim validation. By automatically identifying duplicate claims, overbilling patterns, and coding inconsistencies, the system reduces manual review effort and provides a foundation for future intelligent healthcare analytics solutions.
