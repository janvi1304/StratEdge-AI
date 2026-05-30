# StratEdge-AI

### AI-Powered Investment Banking Intelligence Platform

StratEdge AI is a full-stack financial intelligence platform designed to simulate institutional investment banking workflows using machine learning, financial analytics, and real-time market data integration.

The platform automates:

* Strategic M&A screening
* Bankruptcy and corporate distress prediction
* Comparable company valuation analysis
* Financial intelligence generation
* Strategic acquisition rationale modeling

Built using FastAPI, React, and machine learning infrastructure, the system combines quantitative finance methodologies with AI-driven analytics to create a modern fintech analytics platform.

---

# Core Features

## AI M&A Recommendation Engine

* Predicts strategic acquisition candidates
* Generates acquisition probability scoring
* Evaluates strategic and financial compatibility
* Performs sector and industry alignment analysis
* Produces AI-generated acquisition rationale

### Factors Analyzed

* Industry compatibility
* Sector overlap
* Relative market capitalization
* Liquidity and acquisition capacity
* Financial scale advantage

---

## Bankruptcy & Corporate Distress Prediction

The platform includes a machine learning-based distress analytics engine trained on structured financial datasets.

### Capabilities

* Bankruptcy probability prediction
* Risk classification (Low / Moderate / High)
* Financial distress analysis
* Liquidity stress evaluation
* Corporate survivability assessment

### Use Cases

* Distressed M&A screening
* Credit risk analytics
* Restructuring advisory simulations
* Turnaround evaluation

---

## Comparable Company Analysis (CCA)

Implements institutional relative valuation workflows including:

* EV/Revenue
* EV/EBITDA
* Price-to-Earnings (P/E)
* Enterprise Value analysis

The system dynamically identifies peer groups and performs valuation benchmarking using real company financial data.

---

## Real-Time Financial Data Integration

Integrated with:

* Finnhub API
* Yahoo Finance (yfinance)

The platform retrieves:

* Live stock prices
* Market capitalization
* Cash reserves
* Debt structure
* Revenue and EBITDA metrics
* Industry classifications

---

# Technical Architecture

## Frontend

* React.js
* Tailwind CSS
* Vite
* Institutional fintech dashboard UI
* Interactive probability visualizations

---

## Backend

* FastAPI
* RESTful API architecture
* Financial analytics engine
* Machine learning inference services
* Real-time market data integration

---

## Machine Learning Stack

* Scikit-learn
* Random Forest Classification
* Financial feature engineering
* Probability-based prediction systems
* Structured financial dataset modeling

---

# System Architecture

```txt
frontend/
│
├── React Dashboard
├── Financial Visualization
├── M&A Analytics UI
└── Risk Analytics Interface

backend/
│
├── FastAPI Server
├── ML Prediction Engine
├── Bankruptcy Analytics
├── Comparable Valuation Engine
├── Market Data Integrations
└── Financial Intelligence APIs
```

---

# Machine Learning Models

## M&A Prediction Model

The acquisition engine evaluates strategic acquisition feasibility using:

* Industry alignment
* Sector compatibility
* Relative financial scale
* Liquidity capacity

The model outputs acquisition probability scores between companies.

---

## Bankruptcy Prediction Model

The bankruptcy engine analyzes:

* Financial distress indicators
* Solvency deterioration
* Liquidity instability
* Corporate survivability metrics

Outputs include:

* Bankruptcy probability
* Risk classification
* Distress prediction

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/stratedge-ai.git
```

---

# Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app:app --reload
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# Environment Variables

Create `.env` inside backend directory:

```env
FINNHUB_API_KEY=your_api_key_here
```

---

# Screenshots

(Add application screenshots here)

---

# Future Enhancements

## Planned Features

* Adaptive DCF valuation engine
* Distress-aware valuation frameworks
* Real-time stock chart visualization
* Advanced acquisition prediction models
* AI analyst commentary generation
* Institutional valuation dashboards
* Probability-weighted survival modeling

---

# Strategic Objective

StratEdge AI was developed to replicate portions of institutional investment banking workflows through:

* AI-driven M&A intelligence
* Financial distress analytics
* Strategic acquisition screening
* Quantitative financial analysis
* Relative valuation methodologies

The project demonstrates the intersection of:

* Financial engineering
* Machine learning
* Quantitative analytics
* Full-stack software engineering
* Institutional finance systems

within a unified fintech analytics platform.

---

# Author

Jhanvi Gupta

---
