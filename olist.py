
import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# OLIST E-COMMERCE DATA ANALYTICS PROJECT
# Tools: Python, Pandas, Matplotlib
# ==========================================

# Project folder
FOLDER = r"C:\Users\pbgvh\OneDrive\Desktop\Project"

# ==========================================
# 1. LOAD ORDER DATA
# ==========================================

orders_file = os.path.join(FOLDER, "olist_orders_analysis.csv")
df = pd.read_csv(orders_file)

print("\n========== DATA OVERVIEW ==========")
print(df.head())
print("Dataset Shape:", df.shape)

# Data quality checks
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"], errors="coerce"
)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ==========================================
# 2. MONTHLY ORDER ANALYSIS
# ==========================================

df["month"] = df["order_purchase_timestamp"].dt.to_period("M")

monthly_orders = (
    df.groupby("month")["order_id"]
    .nunique()
    .reset_index(name="total_orders")
)

monthly_orders["month"] = monthly_orders["month"].astype(str)

print("\n========== MONTHLY ORDERS ==========")
print(monthly_orders.to_string(index=False))

monthly_orders.to_csv(
    os.path.join(FOLDER, "python_monthly_orders.csv"),
    index=False
)

plt.figure(figsize=(12, 5))
plt.plot(
    monthly_orders["month"],
    monthly_orders["total_orders"],
    marker="o"
)
plt.title("Olist Monthly Order Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "monthly_orders.png"), dpi=300)
plt.show()

# ==========================================
# 3. MONTHLY REVENUE ANALYSIS
# ==========================================

revenue_file = os.path.join(FOLDER, "monthly_revenue.csv")
revenue_df = pd.read_csv(revenue_file)

revenue_df["revenue"] = pd.to_numeric(
    revenue_df["revenue"], errors="coerce"
)

revenue_df = revenue_df.sort_values("month")

print("\n========== REVENUE ANALYSIS ==========")
print(revenue_df.head().to_string(index=False))
print("Total Revenue (R$):", round(revenue_df["revenue"].sum(), 2))

revenue_df.to_csv(
    os.path.join(FOLDER, "python_monthly_revenue.csv"),
    index=False
)

plt.figure(figsize=(12, 5))
plt.plot(
    revenue_df["month"],
    revenue_df["revenue"],
    marker="o"
)
plt.title("Olist Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Payment Value (R$)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "monthly_revenue.png"), dpi=300)
plt.show()

# ==========================================
# 4. TOP 10 PRODUCT CATEGORIES
# ==========================================

categories_file = os.path.join(FOLDER, "top_categories.csv")
categories = pd.read_csv(categories_file)

categories["product_sales"] = pd.to_numeric(
    categories["product_sales"], errors="coerce"
)

categories = categories.sort_values(
    "product_sales", ascending=False
).head(10)

print("\n========== TOP PRODUCT CATEGORIES ==========")
print(categories.to_string(index=False))

categories.to_csv(
    os.path.join(FOLDER, "python_top_categories.csv"),
    index=False
)

plt.figure(figsize=(11, 6))
plt.barh(categories["category"], categories["product_sales"])
plt.title("Top 10 Product Categories by Sales")
plt.xlabel("Product Sales (R$)")
plt.ylabel("Category")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "top_categories.png"), dpi=300)
plt.show()

# ==========================================
# 5. REPEAT VS ONE-TIME CUSTOMERS
# ==========================================

customers_file = os.path.join(FOLDER, "customer_analysis.csv")
customers = pd.read_csv(customers_file)

print("\n========== CUSTOMER ANALYSIS ==========")
print(customers.to_string(index=False))

customers.to_csv(
    os.path.join(FOLDER, "python_customer_analysis.csv"),
    index=False
)

plt.figure(figsize=(7, 5))
plt.bar(
    customers["customer_type"],
    customers["total_customers"]
)
plt.title("Repeat vs One-Time Customers")
plt.xlabel("Customer Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "customer_analysis.png"), dpi=300)
plt.show()

# ==========================================
# 6. CUSTOMER REVIEW ANALYSIS
# ==========================================

reviews_file = os.path.join(FOLDER, "review_analysis.csv")
reviews = pd.read_csv(reviews_file)

reviews["review_score"] = pd.to_numeric(
    reviews["review_score"], errors="coerce"
)
reviews["total_reviews"] = pd.to_numeric(
    reviews["total_reviews"], errors="coerce"
)

reviews = reviews.sort_values("review_score")

print("\n========== REVIEW ANALYSIS ==========")
print(reviews.to_string(index=False))

reviews.to_csv(
    os.path.join(FOLDER, "python_review_analysis.csv"),
    index=False
)

plt.figure(figsize=(8, 5))
plt.bar(
    reviews["review_score"].astype(int).astype(str),
    reviews["total_reviews"]
)
plt.title("Customer Review Score Distribution")
plt.xlabel("Review Score (1 = Poor, 5 = Excellent)")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig(os.path.join(FOLDER, "review_analysis.png"), dpi=300)
plt.show()

# ==========================================
# 7. FINAL SUMMARY
# ==========================================

print("\n========== PROJECT COMPLETED ==========")
print("Order records:", len(df))
print("Unique orders:", df["order_id"].nunique())
print("Monthly periods:", len(monthly_orders))
print("Product categories analyzed:", len(categories))
print("\nCharts and processed CSV files saved in:")
print(FOLDER)
print("\nAll analyses completed successfully!")
