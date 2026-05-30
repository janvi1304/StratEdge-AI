import yfinance as yf
import pandas as pd


# =========================
# COMPANY LIST
# =========================

tickers = [

    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "NVDA",
    "META",
    "NFLX",
    "TSLA",
    "SPOT",
    "AMD"

]


# =========================
# STORE DATA
# =========================

rows = []


# =========================
# FETCH REAL DATA
# =========================

for ticker in tickers:

    try:

        company = yf.Ticker(ticker)

        info = company.info

        rows.append({

            "name": info.get("shortName"),

            "ticker": ticker,

            "industry": info.get("industry"),

            "sector": info.get("sector"),

            "market_cap": round(
                info.get("marketCap", 0) / 1e9,
                2
            ),

            "cash": round(
                info.get("totalCash", 0) / 1e9,
                2
            ),

            "debt": round(
                info.get("totalDebt", 0) / 1e9,
                2
            ),

            "revenue": round(
                info.get("totalRevenue", 0) / 1e9,
                2
            ),

            "ebitda": round(
                info.get("ebitda", 0) / 1e9,
                2
            ),

            "profit_margin": info.get(
                "profitMargins", 0
            ),

            "current_ratio": info.get(
                "currentRatio", 0
            ),

            "debt_to_equity": info.get(
                "debtToEquity", 0
            )

        })

        print(f"Loaded: {ticker}")

    except:

        print(f"Failed: {ticker}")


# =========================
# CREATE DATAFRAME
# =========================

df = pd.DataFrame(rows)


# =========================
# SAVE CSV
# =========================

df.to_csv(
    "real_companies.csv",
    index=False
)

print("\nReal company dataset created.")
print(df.head())