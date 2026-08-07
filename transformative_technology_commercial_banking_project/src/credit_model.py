"""Transparent credit-metric functions used in the project."""
def net_leverage(debt, cash, ebitda):
    return max(debt-cash, 0) / ebitda if ebitda > 0 else None

def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities if current_liabilities else None

def cash_available_for_debt_service(ebitda, capex, cash_taxes):
    return ebitda - capex - cash_taxes

def dscr(ebitda, capex, cash_taxes, interest, scheduled_principal):
    debt_service = interest + scheduled_principal
    if debt_service <= 0:
        return None
    return cash_available_for_debt_service(ebitda, capex, cash_taxes) / debt_service

if __name__ == "__main__":
    print("2026E base-case DSCR:",
          round(dscr(45.0, 15.0, 6.2, 4.7, 5.0), 2))
