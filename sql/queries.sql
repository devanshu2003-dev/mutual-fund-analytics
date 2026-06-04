-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP Inflow YoY Growth
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows;

-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
WHERE expense_ratio_pct < 1;

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 10;

SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category
ORDER BY avg_return DESC;

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT
    city_tier,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY city_tier;

SELECT
    payment_mode,
    COUNT(*) AS transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_amount DESC;