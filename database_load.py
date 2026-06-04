import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine(
    r"sqlite:///D:/Bluestock/mutual-fund-analytics/bluestock_mf.db"
)

# Read all cleaned CSVs
fund_master = pd.read_csv("data/processed/clean_fund_master.csv")
aum_history = pd.read_csv("data/processed/clean_aum_by_fund_house.csv")
monthly_sip_inflows = pd.read_csv("data/processed/clean_monthly_sip_inflows.csv")
category_inflows = pd.read_csv("data/processed/clean_category_inflows.csv")
industry_folio_counts = pd.read_csv("data/processed/clean_industry_folio_count.csv")
portfolio_holdings = pd.read_csv("data/processed/clean_portfolio_holdings.csv")
benchmark_indices = pd.read_csv("data/processed/clean_benchmark_indices.csv")
nav_history = pd.read_csv("data/processed/clean_nav.csv")
investor_transc = pd.read_csv("data/processed/clean_investor_transactions.csv")
scheme_performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

# Rename date column for consistency with schema
nav_history.rename(columns={"date": "nav_date"}, inplace=True)

# Load into SQLite tables
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

investor_transc.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

scheme_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum_history.to_sql(
    "aum_by_fund_house",
    engine,
    if_exists="replace",
    index=False
)

monthly_sip_inflows.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

category_inflows.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

industry_folio_counts.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

portfolio_holdings.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark_indices.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print("All 10 datasets loaded successfully into SQLite!")

# from sqlalchemy import create_engine
# import sqlite3
# import os
# engine = create_engine(
#     r"sqlite:///D:/Bluestock/mutual-fund-analytics/bluestock_mf.db"
# )

# with engine.connect() as conn:
#     pass

# print("Database created successfully")



# engine = create_engine(
#     r"sqlite:///D:/Bluestock/mutual-fund-analytics/bluestock_mf.db"
# )

# conn = sqlite3.connect(
#     r"D:\Bluestock\mutual-fund-analytics\bluestock_mf.db"
# )

# cursor = conn.cursor()

# with open(
#     r"D:\Bluestock\mutual-fund-analytics\sql\schema.sql",
#     "r"
# ) as file:

#     schema = file.read()

# cursor.executescript(schema)

# conn.commit()

# print("Tables created successfully")
