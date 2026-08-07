-- Technology Coverage Portfolio: example analytical queries
-- Uses data/processed/portfolio_metrics.csv loaded into a SQL engine of your choice.

-- 1. Highest-priority coverage opportunities
SELECT
    Company,
    Vertical,
    Status,
    Revenue_mm,
    Credit_Score,
    Opportunity_Score,
    Coverage_Priority_Score,
    Priority_Tier
FROM portfolio_metrics
ORDER BY Coverage_Priority_Score DESC;

-- 2. Prospects with good credit screens but underpenetrated relationship opportunity
SELECT
    Company,
    Vertical,
    Revenue_mm,
    Credit_Score,
    Opportunity_Score,
    Estimated_Wallet_mm
FROM portfolio_metrics
WHERE Status = 'Prospect'
  AND Credit_Score >= 70
ORDER BY Credit_Score DESC, Opportunity_Score DESC;

-- 3. International / FX opportunity screen
SELECT
    Company,
    Vertical,
    International_Revenue_pct,
    Estimated_Wallet_mm,
    Credit_Score
FROM portfolio_metrics
WHERE International_Revenue_pct >= 20
ORDER BY International_Revenue_pct DESC;

-- 4. Credit watch list
SELECT
    Company,
    Vertical,
    Net_Leverage_x,
    FCF_Margin_pct,
    Risk_Flags,
    Credit_Score
FROM portfolio_metrics
WHERE Credit_Score < 60
   OR FCF_Margin_pct < 0
   OR Risk_Flags >= 2
ORDER BY Credit_Score ASC;
