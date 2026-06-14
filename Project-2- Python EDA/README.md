# E-commerce Sales Analysis

## Overview
This repository contains an exploratory data analysis of an e-commerce sales dataset (1200 orders, 14 columns). The analysis inspects order value distribution, outliers, product and channel performance, and relationships between numeric variables.

## Problem Statement
Understand customer purchase behavior and order value drivers to inform inventory, marketing, and checkout optimizations. Identify outliers and high-value orders for further investigation.

## Objectives
- Compute key order-value metrics (mean, median, min, max).
- Detect and inspect outliers in TotalPrice.
- Identify top-performing products, payment methods, and referral sources.
- Analyze correlations between numeric variables.
- Provide actionable recommendations based on findings.

## Dataset
- Source file used in analysis: `Dataset for Data Analytics.xlsx`
- Rows: 1200
- Columns: 14
- Missing CouponCode values were filled with `"NO COUPON"`.

## Tools & Libraries
- Python (pandas, numpy)
- Visualization: matplotlib, seaborn
- Environment: Jupyter Notebook

## Methodology
1. Load dataset into a pandas DataFrame.
2. Basic data quality checks and missing-value handling.
3. Descriptive statistics and distribution plots for TotalPrice.
4. Outlier detection using the IQR method.
5. Categorical counts and bar charts for product, payment method, and referral source.
6. Correlation analysis for numeric features.

## Key Metrics
- Average Order Value: $1053.97
- Median Order Value: $823.62
- Minimum Order Value: $11.39
- Maximum Order Value: $3456.4

## Outlier Analysis (IQR method)
- Q1 = 410.52
- Q3 = 1578.47
- IQR = 1167.95
- Lower bound = -1341.41
- Upper bound = 3330.41
- Number of TotalPrice outliers detected: 8

## Top Categories & Channels
- Most popular product category: Printer
- Top 5 product categories: Printer, Tablet, Chair, Laptop, Desk
- Most popular payment method: Online
- Most common referral source: Instagram

## Correlation Highlights (with TotalPrice)
- UnitPrice: 0.717
- Quantity: 0.615
- ItemsInCart: 0.393

## Key Findings
- Order value distribution is right-skewed with several high-value outliers.
- TotalPrice is most strongly correlated with UnitPrice and Quantity.
- Printers, Tablets, Chairs, Laptops, and Desks are the top-selling product categories.
- Online payments and Instagram referrals are important channels.

## Recommendations
1. Prioritize inventory and restocking for the highest-selling product categories.
2. Optimize the online payment flow to reduce friction and improve conversions.
3. Use targeted couponing for customers without coupon usage to increase average order value.
4. Investigate high-value outliers to confirm validity (special orders, promotions, or data issues).
5. Focus marketing on top referral channels (e.g., Instagram) and track campaign performance.

## Repository Structure
- Notebook with analysis (Jupyter): contains data loading, cleaning, EDA, visualizations.
- `Dataset for Data Analytics.xlsx` — source data (not committed).
- `EXECUTIVE_SUMMARY.md` — executive summary (if present).
- `README.md` — this file.

## How to Reproduce
1. Open the Jupyter notebook.
2. Ensure `Dataset for Data Analytics.xlsx` is available in the working directory.
3. Run cells top-to-bottom to reproduce the analysis and figures.

## Contact
Analyst: Lawrence Ngukusuk

