# Data Analysis of an E-commerce Dataset

## Project Overview
This project analyzes sales transactions from the `Orders` SQLite database to uncover product performance, customer behavior, payment trends, referral effectiveness, and revenue patterns. The notebook combines SQL queries with Python `pandas` analysis to deliver actionable business insights.

## Author
- Lawrence Ngukusuk
## Date: 
- june,2026

## Objectives
- Identify top-performing products by revenue and average order value
- Determine the payment methods generating the highest revenue
- Find the top customers by spend
- Track monthly revenue trends and seasonality
- Analyze coupon usage impact on average order value
- Evaluate referral source performance and revenue share
- Identify high-value products and revenue concentration
- Review cancelled and returned orders
- Measure customer retention and returning customer revenue contribution

## Key Findings
- Top revenue-generating products:
    - Chair, Printer, Laptop, Tablet, Monitor, Desk, Phone
- Highest revenue payment method:
    - Credit Card, closely followed by Online, Cash, Gift Card, and Debit Card
- Top 10 customers by spend are dominated by single or low-count purchases with high average order values
- Monthly revenue shows strong variation, with peaks in May 2023, June 2024, and June 2025, and lower revenue months in April and May
- Coupon impact:
    - Coupon-used orders generated the majority of revenue and a slightly higher average order value compared to no-coupon orders
- Referral source performance:
    - Instagram, Email, Google, Facebook, and Referral are the top channels, with Instagram contributing the largest revenue share
- High-value products:
    - All major products exceeded $50,000 in revenue, indicating strong product concentration
- Cancellation/return review:
    - Detailed cancelled/returned order history is available for trend and root-cause analysis
- Customer retention:
    - Total customers: 1,189
    - Returning customers: 11
    - Returning rate: 0.93%
    - Revenue share from returning customers: 1.54%
    - One-time customers have a higher average order value than returning customers

## Tools and Technologies
- SQLite
- Python
- pandas
- Jupyter Notebook
- SQL for querying transactional data
- matplotlib / pandas plotting for visual trend analysis

## Recommendations
- Prioritize marketing and inventory for top revenue products such as Chair, Printer, Laptop, and Tablet
- Improve customer retention programs, as returning customers are currently a very small share of orders and revenue
- Continue investing in strong referral channels like Instagram and Email
- Investigate causes of cancellations and returns to reduce churn and recover lost revenue
- Leverage coupon strategies carefully, since coupon orders still maintain strong average order values
- Review payment processing preferences to optimize checkout experience across Credit Card, Online, Cash, Gift Card, and Debit Card

## Best Questions Answered
- Which products generate the most revenue?
- What is the average order value by product?
- Which payment methods drive the highest revenue?
- Who are the top spending customers?
- How does revenue trend month over month?
- What is the impact of coupon usage on revenue and average order value?
- Which referral sources contribute the most revenue?
- What are the details of cancelled and returned orders?
- How healthy is customer retention and what share of revenue comes from repeat buyers?

## Notes
This analysis is intended to provide a clear business view of sales performance and customer behavior in the Orders dataset. The findings can be used to guide strategic product focus, marketing spend, customer loyalty initiatives, and operational improvements.