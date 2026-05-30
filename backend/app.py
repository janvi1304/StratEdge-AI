id="cleanapp01"
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

import pandas as pd
import requests
import os
import pickle


# ============================================
# LOAD ENV VARIABLES
# ============================================

load_dotenv()

API_KEY = os.getenv("FINNHUB_API_KEY")


# ============================================
# CREATE FASTAPI APP
# ============================================

app = FastAPI()


# ============================================
# ENABLE CORS
# ============================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================
# LOAD COMPANY DATA
# ============================================

companies = pd.read_csv("real_companies.csv")

# Clean missing values
companies = companies.fillna(0)

# Convert numeric columns
numeric_cols = [

    "market_cap",
    "cash",
    "debt",
    "revenue",
    "ebitda"

]

for col in numeric_cols:

    companies[col] = pd.to_numeric(
        companies[col],
        errors="coerce"
    ).fillna(0)


# ============================================
# LOAD MODELS
# ============================================

with open("mna_model.pkl", "rb") as file:

    model = pickle.load(file)

with open("bankruptcy_model.pkl", "rb") as file:

    bankruptcy_model = pickle.load(file)


# ============================================
# HOME ROUTE
# ============================================

@app.get("/")
def home():

    return {

        "message": "AI Investment Banking Platform Running"

    }


# ============================================
# LIVE STOCK DATA
# ============================================

@app.get("/stock/{ticker}")
def get_stock(ticker: str):

    try:

        url = (

            f"https://finnhub.io/api/v1/quote"

            f"?symbol={ticker}"

            f"&token={API_KEY}"

        )

        response = requests.get(url)

        return response.json()

    except Exception as e:

        return {

            "error": str(e)

        }


# ============================================
# COMPANY SEARCH
# ============================================

@app.get("/company/{name}")
def get_company_data(name: str):

    try:

        search_url = (

            f"https://finnhub.io/api/v1/search"

            f"?q={name}"

            f"&token={API_KEY}"

        )

        response = requests.get(search_url)

        data = response.json()

        if not data["result"]:

            return {

                "error": "Company not found"

            }

        company = data["result"][0]

        ticker = company["symbol"]

        description = company["description"]

        stock_url = (

            f"https://finnhub.io/api/v1/quote"

            f"?symbol={ticker}"

            f"&token={API_KEY}"

        )

        stock_response = requests.get(stock_url)

        stock_data = stock_response.json()

        return {

            "company_name": description,

            "ticker": ticker,

            "stock_data": {

                "current_price": stock_data.get("c"),

                "change": stock_data.get("d"),

                "percent_change": stock_data.get("dp"),

                "high": stock_data.get("h"),

                "low": stock_data.get("l"),

                "open": stock_data.get("o"),

                "previous_close": stock_data.get("pc")

            }

        }

    except Exception as e:

        return {

            "error": str(e)

        }


# ============================================
# COMPARABLE COMPANIES
# ============================================

@app.get("/comps/{company_name}")
def get_comps(company_name: str):

    try:

        target = companies[

            companies["name"]
            .astype(str)
            .str.lower()
            .str.contains(company_name.lower())

        ]

        if target.empty:

            return {

                "error": "Company not found"

            }

        target = target.iloc[0]

        peers = companies[
            companies["industry"]
            == target["industry"]
        ]

        results = []

        for _, row in peers.iterrows():

            if row["name"] == target["name"]:
                continue

            ev = (

                float(row["market_cap"])

                + float(row["debt"])

                - float(row["cash"])

            )

            ebitda = max(
                float(row["ebitda"]),
                1
            )

            revenue = max(
                float(row["revenue"]),
                1
            )

            earnings = max(
                float(row["market_cap"]) * 0.08,
                1
            )

            ev_ebitda = round(
                ev / ebitda,
                2
            )

            pe_ratio = round(
                float(row["market_cap"]) / earnings,
                2
            )

            ev_revenue = round(
                ev / revenue,
                2
            )

            results.append({

                "company": row["name"],

                "industry": row["industry"],

                "EV": round(ev, 2),

                "EV/EBITDA": ev_ebitda,

                "P/E": pe_ratio,

                "EV/Revenue": ev_revenue

            })

        return {

            "target_company": target["name"],

            "peer_group": results

        }

    except Exception as e:

        return {

            "error": str(e)

        }


# ============================================
# AI M&A ENGINE
# ============================================

@app.get("/mna/{company_name}")
def mna_recommendation(company_name: str):

    try:

        target = companies[

            companies["name"]
            .astype(str)
            .str.lower()
            .str.contains(company_name.lower())

        ]

        if target.empty:

            return {

                "error": "Company not found"

            }

        target = target.iloc[0]

        recommendations = []

        for _, company in companies.iterrows():

            if company["name"] == target["name"]:
                continue

            # ============================================
            # FEATURE ENGINEERING
            # ============================================

            industry_match = int(

                company["industry"]
                == target["industry"]

            )

            sector_match = int(

                company["sector"]
                == target["sector"]

            )

            market_cap_ratio = round(

                float(company["market_cap"])

                /
                max(float(target["market_cap"]), 1),

                2

            )

            cash_ratio = round(

                float(company["cash"])

                /
                max(float(target["cash"]), 1),

                2

            )

            # ============================================
            # MODEL FEATURES
            # ============================================

            features = [[

                industry_match,

                sector_match,

                market_cap_ratio,

                cash_ratio

            ]]

            # ============================================
            # PREDICT ACQUISITION PROBABILITY
            # ============================================

            probability = model.predict_proba(
                features
            )[0][1]

            probability = round(
                probability * 100,
                2
            )

            # ============================================
            # SMART STRATEGIC RATIONALE
            # ============================================

            if industry_match == 1:

                rationale = (

                    f"{company['name']} could consolidate "

                    f"its position within the "

                    f"{target['industry']} industry "

                    f"through acquisition of "

                    f"{target['name']}."

                )

            elif sector_match == 1:

                rationale = (

                    f"{company['name']} could expand "

                    f"its presence in the "

                    f"{target['sector']} sector "

                    f"and unlock operational synergies."

                )

            elif market_cap_ratio > 2:

                rationale = (

                    f"{company['name']} has significant "

                    f"financial scale advantage over "

                    f"{target['name']}, enabling a "

                    f"potential strategic acquisition."

                )

            elif cash_ratio > 1.5:

                rationale = (

                    f"{company['name']} maintains a strong "

                    f"cash position which could support "

                    f"acquisition financing and expansion."

                )

            else:

                rationale = (

                    f"{company['name']} could pursue "

                    f"{target['name']} to diversify "

                    f"business operations and strengthen "

                    f"competitive positioning."

                )

            # ============================================
            # SPECIAL INDUSTRY LOGIC
            # ============================================

            if "AI" in str(target["sector"]):

                rationale += (

                    " The acquisition could accelerate "

                    "AI capabilities and platform expansion."

                )

            elif "Cloud" in str(target["sector"]):

                rationale += (

                    " Cloud infrastructure integration "

                    "could generate long-term enterprise synergies."

                )

            elif "Streaming" in str(target["sector"]):

                rationale += (

                    " The deal could strengthen digital "

                    "content and subscription ecosystems."

                )

            elif "Semiconductor" in str(target["industry"]):

                rationale += (

                    " Semiconductor supply chain and "

                    "compute synergies could create value."

                )

            recommendations.append({

                "acquirer": company["name"],

                "industry": company["industry"],

                "sector": company["sector"],

                "market_cap": round(
                    float(company["market_cap"]),
                    2
                ),

                "acquisition_probability": probability,

                "rationale": rationale

            })

        # ============================================
        # SORT RESULTS
        # ============================================

        recommendations = sorted(

            recommendations,

            key=lambda x:
            x["acquisition_probability"],

            reverse=True

        )

        top_results = recommendations[:5]

        return {

            "target_company": target["name"],

            "target_sector": target["sector"],

            "recommended_acquirers": top_results

        }

    except Exception as e:

        return {

            "error": str(e)

        }


# ============================================
# BANKRUPTCY RISK API
# ============================================

@app.get("/bankruptcy-risk")
def bankruptcy_risk():

    try:

        sample_company = [[

            500,
            200,
            100,
            150,
            300,
            400,
            250,
            180,
            220,
            190,
            130,
            170,
            90,
            75,
            60,
            500,
            450,
            550

        ]]

        prediction = bankruptcy_model.predict(
            sample_company
        )[0]

        probability = bankruptcy_model.predict_proba(
            sample_company
        )[0][1]

        probability = round(
            probability * 100,
            2
        )

        risk_level = "Low"

        if probability > 70:

            risk_level = "High"

        elif probability > 40:

            risk_level = "Moderate"

        return {

            "bankruptcy_probability": probability,

            "risk_level": risk_level,

            "prediction": int(prediction)

        }

    except Exception as e:

        return {

            "error": str(e)

        }

