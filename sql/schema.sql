CREATE TABLE IF NOT EXISTS dim_fund(
    amfi_code TEXT PRIMARY KEY,
    fund_house VARCHAR ,
    scheme_name VARCHAR,
    category VARCHAR,
    sub_category VARCHAR,
    plan VARCHAR,
    launch_date DATE,
    benchmark VARCHAR, 
    expense_ratio_pct FLOAT,
    exit_load_pct FLOAT, 
    min_sip_amount INT,
    min_lumpsum_amount INT,
    fund_manager VARCHAR,
    risk_category VARCHAR,
    sebi_category_code VARCHAR
);


CREATE TABLE IF NOT EXISTS
fact_nav (amfi_code TEXT FK,
nav_date DATE, 
nav REAL,
daily_return REAL);

CREATE TABLE IF NOT EXISTS fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code TEXT,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,

    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,

    aum_crore REAL,
    expense_ratio_pct REAL,

    morningstar_rating INTEGER,
    risk_grade TEXT,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);