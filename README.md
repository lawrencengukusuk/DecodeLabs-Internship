DATA CLEANING REPORT
Tools Used:
python
pandas
openPyXL

STEPS PERFORMED:
(1) Loaded the Excel dataset into python using panddas:
import pandas as pd
df=pd.read_excel("dataset for Data Analytics (2).xlsx")
(2) Inspected the data structure Using:
print(df.head())
print(df.info())
print(df.shape())
(3) Checked for missing values using:
print(df.isnull().sum())
Results: CouponCode 309
Interpretation: the CouponCode contained 309 missing values,Which were replaced with "No coupon"

(4) Handled missing values where necessary
(5) Checked for duplicates rows using:
print(df.duplicates().sum())
(6) Remove duplicates rows using:
print(df.drop_duplicates())
(7) Verified data formats and converted date columns where necessary
(8)Comfirmed there were no duplicates IDs
(9)Saved the cleaned dataset as Cleaned_dataset.xlsx

OUTCOME:
The dataset was successfully cleaned by handling missing values,Removing duplicates, and verifying data formats.


