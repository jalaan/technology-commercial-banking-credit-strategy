"""Coverage-priority model. This is a project screening score, not a bank risk rating."""
def clamp(x):
    return max(0, min(100, x))

def score_company(revenue, growth, ebitda_margin, fcf_margin, cash, debt,
                  current_ratio, nrr, international_revenue_pct, risk_flags, estimated_wallet_mm):
    ebitda = revenue * ebitda_margin / 100
    net_debt = max(debt-cash, 0)
    net_leverage = net_debt/ebitda if ebitda > 0 else 9.9

    growth_score = clamp(growth*3.0)
    margin_score = clamp(50 + ebitda_margin*2.5)
    fcf_score = clamp(50 + fcf_margin*2.5)
    leverage_score = clamp(100 - net_leverage*22)
    liquidity_score = clamp(current_ratio*40)
    nrr_score = clamp((nrr-90)*2.5)
    risk_score = clamp(100-risk_flags*22)

    credit_score = (
        0.12*growth_score + 0.18*margin_score + 0.18*fcf_score +
        0.22*leverage_score + 0.14*liquidity_score +
        0.08*nrr_score + 0.08*risk_score
    )
    opportunity_score = clamp(estimated_wallet_mm/3.2*100)*0.7 + clamp(international_revenue_pct*2)*0.3
    coverage_priority = 0.65*credit_score + 0.35*opportunity_score
    return round(credit_score,1), round(opportunity_score,1), round(coverage_priority,1)

if __name__ == "__main__":
    print(score_company(255,17,12.9,7.5,48,80,1.8,112,18,1,1.20))
