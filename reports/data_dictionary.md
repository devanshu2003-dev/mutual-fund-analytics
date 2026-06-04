# Data Dictionary

## dim_fund

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Unique fund identifier |
| scheme_name | TEXT | Name of mutual fund |
| fund_house | TEXT | AMC name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |

## fact_nav

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Fund identifier |
| nav_date | DATE | NAV date |
| nav | REAL | Net Asset Value |
| daily_return | REAL | Daily NAV return |

## fact_transactions

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| investor_id        | TEXT      | Unique investor identifier    |
| transaction_date   | DATE      | Date of transaction           |
| amfi_code          | TEXT      | Mutual fund scheme code       |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption   |
| amount_inr         | REAL      | Transaction amount in INR     |
| state              | TEXT      | Investor state                |
| city               | TEXT      | Investor city                 |
| city_tier          | TEXT      | City classification (T30/B30) |
| age_group          | TEXT      | Investor age bracket          |
| gender             | TEXT      | Investor gender               |
| annual_income_lakh | REAL      | Annual income in lakhs        |
| payment_mode       | TEXT      | Mode of payment               |
| kyc_status         | TEXT      | KYC verification status       |

## fact_performance

| Column             | Data Type | Description                       |
| ------------------ | --------- | --------------------------------- |
| amfi_code          | TEXT      | Mutual fund scheme code           |
| return_1yr_pct     | REAL      | 1-year return percentage          |
| return_3yr_pct     | REAL      | 3-year return percentage          |
| return_5yr_pct     | REAL      | 5-year return percentage          |
| benchmark_3yr_pct  | REAL      | 3-year benchmark return           |
| alpha              | REAL      | Excess return over benchmark      |
| beta               | REAL      | Measure of market risk            |
| sharpe_ratio       | REAL      | Risk-adjusted return metric       |
| sortino_ratio      | REAL      | Downside risk-adjusted return     |
| std_dev_ann_pct    | REAL      | Annualized volatility             |
| max_drawdown_pct   | REAL      | Maximum decline from peak         |
| aum_crore          | REAL      | Assets Under Management (Crore ₹) |
| expense_ratio_pct  | REAL      | Annual expense ratio              |
| morningstar_rating | INTEGER   | Morningstar fund rating           |
| risk_grade         | TEXT      | Fund risk category                |

## aum_by_fund_house

| Column | Data Type | Description |
|----------|----------|----------|
| date | DATE | Reporting date |
| fund_house | TEXT | Asset Management Company (AMC) |
| aum_lakh_crore | REAL | AUM in lakh crores |
| aum_crore | REAL | Assets Under Management in crores |
| num_schemes | INTEGER | Number of schemes managed |

## monthly_sip_inflows

| Column | Data Type | Description |
|----------|----------|----------|
| month | TEXT | Reporting month |
| sip_inflow_crore | REAL | Monthly SIP inflow in crores |
| active_sip_accounts_crore | REAL | Active SIP accounts in crores |
| new_sip_accounts_lakh | REAL | New SIP accounts opened (lakh) |
| sip_aum_lakh_crore | REAL | SIP AUM in lakh crores |
| yoy_growth_pct | REAL | Year-over-Year growth percentage |

## category_inflows

| Column | Data Type | Description |
|----------|----------|----------|
| month | TEXT | Reporting month |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net inflow/outflow in crores |

## industry_folio_count

| Column | Data Type | Description |
|----------|----------|----------|
| month | TEXT | Reporting month |
| total_folios_crore | REAL | Total investor folios |
| equity_folios_crore | REAL | Equity fund folios |
| debt_folios_crore | REAL | Debt fund folios |
| hybrid_folios_crore | REAL | Hybrid fund folios |
| others_folios_crore | REAL | Other category folios |

## portfolio_holdings

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Mutual fund scheme code |
| stock_symbol | TEXT | Stock ticker symbol |
| stock_name | TEXT | Company/stock name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio weight (%) |
| market_value_cr | REAL | Market value in crores |
| current_price_inr | REAL | Current stock price in INR |
| portfolio_date | DATE | Portfolio disclosure date |

## benchmark_indices

| Column | Data Type | Description |
|----------|----------|----------|
| date | DATE | Index date |
| index_name | TEXT | Benchmark index name |
| close_value | REAL | Closing value of the benchmark index |