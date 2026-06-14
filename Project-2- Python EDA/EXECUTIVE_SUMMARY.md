# Executive Summary

**Dataset:** E-commerce Sales Data  
**Analyst:** Lawrence Ngukusuk  
**Date:** June 2026  

## Overview
This analysis covers the e-commerce sales dataset with 1200 orders and 14 columns. Missing values in `CouponCode` were handled by replacing them with `"NO COUPON"`.

## Key Metrics
- Average Order Value: $1053.97
- Median Order Value: $823.62
- Minimum Order Value: $11.39
- Maximum Order Value: $3456.40

## Outlier Analysis
- Lower bound for outliers: $-1341.41
- Upper bound for outliers: $3330.41
- Number of TotalPrice outliers detected: 8

## Top Categories and Channels
- Most popular product category: Printer
- Most popular payment method: Online
- Most common referral source: Instagram

## Key Findings
- The distribution of order values is right-skewed, with a handful of high-value orders acting as outliers.
- Higher quantities and higher unit prices are strongly associated with higher total prices.
- The most popular product category and payment channel should be prioritized for inventory and checkout optimization.

## Recommendations
1. Increase marketing efforts on the top referral channel to capture more customers.
2. Optimize the online payment experience since online payments are the most popular.
3. Maintain stock levels for the highest-selling products to avoid missed sales.
4. Use targeted coupon offers for customers without coupon usage to encourage purchases.
5. Investigate high-value outliers to determine if they are special orders, promotions, or data issues.

