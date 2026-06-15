# Data Cleaning Report

## Overview
This repository contains the data cleaning steps performed on the dataset "dataset for Data Analytics (2).xlsx". The cleaning process standardized formats, handled missing values and duplicates, and produced a cleaned output suitable for downstream analysis.

## Tools
- Python
- pandas
- openpyxl

## Dataset
- Source file: dataset for Data Analytics (2).xlsx
- Cleaned output: Cleaned_dataset.xlsx

## Cleaning Steps
1. Load dataset
    ```python
    df = pd.read_excel("dataset for Data Analytics (2).xlsx")
    ```
2. Inspect structure and sample records
    ```python
    df.head()
    df.info()
    df.shape
    ```
3. Identify missing values
    ```python
    df.isnull().sum()
    ```
    - Observation: `CouponCode` contained 309 missing values. These were standardized to "No coupon".
4. Handle missing values where appropriate (e.g., fill, impute, or drop based on context).
5. Detect duplicate rows
    ```python
    df.duplicated().sum()
    ```
6. Remove duplicate rows
    ```python
    df = df.drop_duplicates()
    ```
7. Verify and convert data types (for example, parse date columns to datetime)
    ```python
    df['Date'] = pd.to_datetime(df['Date'])
    ```
8. Confirm unique identifiers (no duplicate IDs remain).
9. Save the cleaned dataset
    ```python
    df.to_excel("Cleaned_dataset.xlsx", index=False, engine="openpyxl")
    ```

## Outcome
The dataset was successfully cleaned: missing values were addressed, duplicate records removed, and data types standardized. The cleaned file `Cleaned_dataset.xlsx` is ready for analysis.

## Recommendations
- Document any assumptions or imputations applied to missing data.
- Retain a backup of the raw dataset.
- Add basic validation checks (value ranges, referential integrity) as part of the ETL pipeline.
