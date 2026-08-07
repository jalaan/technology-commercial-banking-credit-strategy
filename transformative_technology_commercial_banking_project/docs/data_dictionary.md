# Data Dictionary

## portfolio_companies.csv
| Field | Definition |
|---|---|
| Company | Fictional company name |
| Vertical | Technology sub-sector |
| Revenue_mm | Latest annual revenue in $MM |
| Revenue_Growth_pct | Latest annual revenue growth |
| EBITDA_Margin_pct | EBITDA / revenue |
| FCF_Margin_pct | Free cash flow / revenue |
| Cash_mm | Cash balance |
| Debt_mm | Gross debt |
| Current_Ratio_x | Current assets / current liabilities |
| NRR_pct | Net revenue retention |
| International_Revenue_pct | International share of revenue |
| Risk_Flags | Count of synthetic qualitative watch items |
| Estimated_Wallet_mm | Synthetic annual relationship wallet estimate |
| Status | Client or prospect |

## portfolio_metrics.csv
Adds:
- Net_Leverage_x
- Credit_Score
- Opportunity_Score
- Coverage_Priority_Score
- Priority_Tier

## aethergrid_financials.csv
Historical and forecast financial statements plus operating KPIs for the flagship client.

## aethergrid_treasury_activity.csv
Synthetic monthly customer collections, vendor payments, wires, ACH, FX notional, and operating cash.

## aethergrid_scenarios.csv
Base, downside, and upside scenario outputs including revenue, EBITDA, interest, debt service, DSCR, and net leverage.
