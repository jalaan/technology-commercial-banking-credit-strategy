"""Generate synthetic data for the Transformative Technology Commercial Banking project."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
RAW.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)

PORTFOLIO = [
    ("AetherGrid Systems", "Cloud / AI Observability", 255, 17.0, 12.9, 7.5, 48, 80, 1.8, 112, 18, 1, 1.20, "Client"),
    ("CipherNorth Security", "Cybersecurity", 410, 21.0, 18.0, 14.0, 92, 105, 2.1, 118, 28, 0, 1.65, "Prospect"),
    ("LedgerSpring", "Fintech Infrastructure", 185, 29.0, 7.0, -2.0, 36, 70, 1.4, 121, 12, 2, 1.05, "Prospect"),
    ("VectorMesh AI", "AI Data Infrastructure", 132, 48.0, -6.0, -18.0, 74, 20, 3.2, 126, 9, 3, 0.82, "Prospect"),
    ("CoreTransit Software", "Vertical SaaS", 305, 11.0, 22.0, 17.0, 61, 45, 2.4, 108, 7, 0, 1.15, "Client"),
    ("HelioStack Cloud", "Cloud Services", 780, 15.0, 16.0, 10.0, 125, 260, 1.6, 111, 35, 1, 2.40, "Client"),
    ("NexaCommerce", "Commerce Enablement", 520, 9.0, 13.0, 8.0, 68, 155, 1.5, 104, 14, 2, 1.55, "Prospect"),
    ("QuantumRoute Networks", "Network Software", 940, 7.0, 20.0, 15.0, 170, 325, 1.9, 106, 42, 1, 2.75, "Client"),
    ("PrismOps", "DevOps / Automation", 225, 18.0, 10.0, 6.0, 44, 65, 1.7, 113, 20, 1, 0.95, "Prospect"),
    ("NovaHealthTech", "Healthcare Technology", 610, 13.0, 15.0, 9.0, 115, 190, 1.8, 109, 6, 1, 1.90, "Client"),
    ("SignalForge", "Data & Analytics", 72, 34.0, 2.0, -6.0, 29, 15, 2.5, 124, 10, 2, 0.48, "Prospect"),
    ("AtlasEdge Systems", "Edge Computing", 1180, 5.0, 24.0, 18.0, 210, 360, 2.0, 103, 46, 1, 3.10, "Client"),
]

headers = ["Company","Vertical","Revenue_mm","Revenue_Growth_pct","EBITDA_Margin_pct","FCF_Margin_pct",
           "Cash_mm","Debt_mm","Current_Ratio_x","NRR_pct","International_Revenue_pct","Risk_Flags",
           "Estimated_Wallet_mm","Status"]

with (RAW/"portfolio_companies.csv").open("w", newline="") as f:
    w=csv.writer(f); w.writerow(headers); w.writerows(PORTFOLIO)

print("Synthetic portfolio written to", RAW/"portfolio_companies.csv")
