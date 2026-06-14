import pandas as pd
#load Excel File
df = pd.read_excel("Dataset for Data Analytics (2).xlsx")

#show first 5 rows
print(df.head()) 

#check Dataset information
print(df.info())

#check columns and rows
print(df.shape)

#checking missing values
print(df.isnull().sum())
#checking duplicates
duplicates=df.duplicated().sum()
print("duplicated Rows:", duplicates)
#Remove duplicates
df.drop_duplicates(inplace=True)
print(duplicates, "duplicates removed")

#checking missing values after filling
df["CouponCode"]=df["CouponCode"].fillna("NO_COUPON")
print(df.isnull().sum())
#check Duplicates order IDs
print(df["OrderID"].duplicated().sum())
#verify Date Format
print(df["Date"].dtype)
#date conversion
df["Date"]=pd.to_datetime(df["Date"], errors="coerce"
)
#check for invalid Dates
print(df["Date"].isnull().sum())
#check Numeric columnns
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].describe())
#Detect  Outliers
Q1=df["TotalPrice"].quantile(0.25)
Q3=df["TotalPrice"].quantile(0.75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=df[(df["TotalPrice"]<lower_bound) | (df["TotalPrice"]>upper_bound)]
print("Number of Outliers in TotalPrice:", outliers.shape[0])
#checking text consistency
print(df["PaymentMethod"].unique())
print(df["OrderStatus"].unique())
print(df["ReferralSource"].unique())
print(df["Product"].unique())
#standardize text Fields
df["PaymentMethod"]=df["PaymentMethod"].str.lower()
df["OrderStatus"]=df["OrderStatus"].str.lower()
df["ReferralSource"]=df["ReferralSource"].str.lower()
df["Product"]=df["Product"].str.lower()
#verify Total Price
calculated_total=(df["Quantity"]*df["UnitPrice"])
difference=(df["TotalPrice"]-calculated_total)
print(difference.head())
# Final Validation
print('missing values after cleaning:\n', df.isnull().sum())
print('duplicates after cleaning:\n', df.duplicated().sum())
print('data types after cleaning:\n', df.dtypes)
print('final dataset shape after cleaning:\n', df.shape)
print('final dataset preview after cleaning:\n', df.head())
print('final dataset description after cleaning:\n', df.describe())
print('final dataset unique values after cleaning:\n', df.nunique())
print('final dataset info after cleaning:\n', df.info())
print('final dataset columns after cleaning:\n', df.columns)
print('final dataset outliers in TotalPrice after cleaning:\n', df[(df["TotalPrice"]<lower_bound) | (df["TotalPrice"]>upper_bound)].shape[0])
print('final dataset unique Payment Methods after cleaning:\n', df["PaymentMethod"].unique())
print('final dataset unique Order Statuses after cleaning:\n', df["OrderStatus"].unique())
print('final dataset null dates after cleaning:\n', df["Date"].isnull().sum())
# Save cleaned dataset to a new Excel file
df.to_excel("Cleaned_Dataset.xlsx", index=False)