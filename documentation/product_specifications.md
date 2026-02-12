# Product Specifications - MarketByte (The Financial Co-Pilot)

**Version:** 1.0 (Hackathon MVP)
**Status:** Draft
**Last Updated:** 2026-02-13

---

## 1. Introduction

**MarketByte** (Code Name: _PSX-Brief_) is an AI-driven "Financial Co-Pilot" integrated into WhatsApp. It aims to democratize financial literacy for retail investors in Pakistan by transforming complex market data into personalized, actionable insights.

### 1.1 Vision

To transition retail investors from "blind" panic-selling to data-driven confidence by providing a frictionless bridge between abstract financial indices and their personal portfolios.

### 1.2 Key Objectives

- **Demistify Finance:** Explain market movements in simple English (and Urdu in future scope).
- **Personalization:** Filter noise by delivering news only relevant to the user's specific holdings.
- **Accessibility:** Operate entirely within WhatsApp, requiring no new app installation or complex login.
- **Actionability:** Provide concrete data (fees, sector exposure, valuations) to empower decision-making.

---

## 2. Target Audience & Personas

### 2.1 Primary: "The Passive Professional" (Ali)

- **Profile:** 32-year-old Corporate Manager.
- **Behavior:** Saves monthly via Mutual Funds (SIP).
- **Pain Point:** Sees fund balance drop and considers stopping investments due to panic; doesn't have time to read financial newspapers.
- **Goal:** Wants peace of mind and high-level summaries without effort.

### 2.2 Secondary: "The Aspiring Trader" (Sara)

- **Profile:** 24-year-old CS Student.
- **Behavior:** Has small savings (approx. Rs. 50k) and wants to start buying stocks.
- **Pain Point:** Fear of losing money; confused by balance sheets and technical jargon.
- **Goal:** Wants to find "safe," undervalued stocks to build a portfolio.

---

## 3. Functional Specifications

### 3.1 Epic 1: Onboarding & Account Setup

**Goal:** Frictionless registration and profile tailoring.

- **FR-1.1 (Trigger):** Bot activates upon receiving a prompt (e.g., "Hi", "Start").
- **FR-1.2 (Profiling):** User selects profile type:
  - _Index Investor:_ Selects Asset Management Company (e.g., Meezan, UBL).
  - _Stock Picker:_ Inputs specific stock tickers (e.g., OGDC, SYS) - Max 5 initially.
- **FR-1.3 (Security):** System confirms secure storage of preferences (Account ID mapped to WhatsApp Number).
- **FR-1.4 (Edit):** Command `PROFILE` allows users to restart or edit settings.

### 3.2 Epic 2: The Smart Daily Brief

**Goal:** Automated, personalized market intelligence.

- **FR-2.1 (Schedule):** Delivered automatically at 9:00 AM (Pre-market) and 5:00 PM (Post-market).
- **FR-2.2 (Market Pulse):** 1-sentence summary of KSE-100 index performance (Green/Red) + Primary Driver (Political/Economic/Corporate).
- **FR-2.3 (Personalized News):**
  - _Logic:_ Scans news for user's specific holdings (or top holdings of their mutual fund).
  - _Output:_ "Your fund's top holding, **[Company Name]**, [Action/Event] today."
- **FR-2.4 (Format):** Maximum 3 bullet points. No "wall of text."
- **FR-2.5 (Language):** Simple English, avoiding excessive jargon.

### 3.3 Epic 3: Portfolio X-Ray

**Goal:** Transparency for mutual fund holders.

- **FR-3.1 (Command):** User sends command `XRAY`.
- **FR-3.2 (Mapping):** System maps User's Fund -> Fund's Top Holdings (based on latest Fund Manager Report).
- **FR-3.3 (Output):**
  - Display top 3-5 underlying companies.
  - Sector allocation summary (e.g., "Heavy in Cement & Banking").
- **FR-3.4 (Advanced Metrics - _New_):**
  - **Fee Calculator:** "You paid approx **Rs. [Amount]** in fees this month."
  - **Sector Exposure:** Aggregated exposure across all funds.
  - **Dividend Alert:** Notification if an underlying stock declares a dividend.

### 3.4 Epic 4: Opportunity Radar

**Goal:** Data-driven discovery for active investors.

- **FR-4.1 (Command):** User sends command `OPP`.
- **FR-4.2 (Algorithm):** Filter stocks based on:
  - P/E Ratio < Sector Average.
  - Dividend Yield > 10%.
  - RSI < 30 (Oversold condition).
- **FR-4.3 (Output):** List of top 3 matches with key metric (e.g., "OGDC: 12% Yield").
- **FR-4.4 (Disclaimer):** Mandatory text: "Not financial advice. DYOR."

### 3.5 Epic 5: Sentiment Analysis

**Goal:** Emotional context for market moves.

- **FR-5.1 (Input):** Financial news headlines + Social media tags (#PSX, #KSE100).
- **FR-5.2 (Analysis):** NLP model scores sentiment from -1 (Fear) to +1 (Greed).
- **FR-5.3 (Output):** Visual Emoji Meter (e.g., 😨 Fear vs 🤑 Greed) with a score (0-100).

### 3.6 Epic 6: AI Predictive Alerts (Neural Network)

**Goal:** Proactive alerts based on historical pattern recognition.

- **FR-6.1 (Training Data):** Model trained on 10-year dataset of Tweets, News, Annual Reports, and PSX Indexes.
- **FR-6.2 (Inference):** Real-time processing of incoming news against the trained model.
- **FR-6.3 (Trigger):** Alert triggers ONLY if prediction confidence > 85% for a >2% price movement.
- **FR-6.4 (Output):** "🔮 **AI Prediction:** Breaking news regarding [Event] has an 88% similarity to [Past Event 2018]. Expect volatility."

### 3.7 Epic 7: Advanced Market Intelligence (External Data)

**Goal:** Provide comprehensive financial context beyond just stock prices.

- **FR-7.1 (Forex):** Display daily USD/PKR rates from SBP in the Daily Brief.
- **FR-7.2 (Smart Money):** Alert users if Foreign Investors (FIPI) are net buyers/sellers > $1M.
- **FR-7.3 (Dividends):** Notify users 2 days before an Ex-Date for their holdings (Data Source: PSX Financial Annals).
- **FR-7.4 (Insider):** Immediate alert if a Director/CEO buys shares of a user's holding (Data Source: PSX Corporate Annals).
- **FR-7.5 (Macro):** Push notification on Policy Rate changes or CPI Inflation spikes.

### 3.6 Epic 6: User Experience (UX)

**Goal:** App-like feel within chat.

- **FR-6.1 (Interaction):** Use WhatsApp Quick Reply buttons for common actions (`XRAY`, `OPP`, `MORE`).
- **FR-6.2 (Deep Dive):** Option to "Read More" on specific news snippets.
- **FR-6.3 (Freshness):** All data responses must include a "Last Updated" timestamp.
- **FR-6.4 (Opt-out):** Easy `STOP` or `UNSUBSCRIBE` command functionality.

---

## 4. Technical Architecture

### 4.1 Stack

- **Frontend:** WhatsApp Business API (Twilio/Meta) + Web Dashboard (Next.js/React).
- **Authentication:** AWS Cognito (User Pools/Identity Pools).
- **Backend:** AWS Lambda (Python 3.11) + AWS SageMaker (Model Hosting).
- **Database:** Amazon DynamoDB (User Profiles, Fund Mappings) + S3 (Data Lake).
- **AI/LLM:** Amazon Bedrock (Claude) + Custom Neural Network (Predictive Model).
- **Data Ingestion:** Python Scrapers (Custom) running on EventBridge schedule.

### 4.2 Constraints & NFRs

- **Latency:** Interactive commands (`XRAY`, `OPP`) must respond < 3 seconds.
- **Reliability:** Daily Brief delivery success rate > 99.9%.
- **Accuracy:** Financial data (Price, %) must be hard-coded from source, NOT generated by LLM (to prevent hallucinations).
- **Cost:** Architecture optimized for AWS Free Tier limits where possible.

---

## 5. Roadmap

### Phase 1: Hackathon MVP

- [x] Core WhatsApp Bot Setup
- [x] User Profiling (Mock Data)
- [x] Daily Brief Generation (Text)
- [x] Basic Portfolio X-Ray

### Phase 2: Enhanced Features

- [ ] Real-time API integration for stock prices.
- [ ] Advanced X-Ray (Fee calculation, personalized dividends).
- [ ] Sentiment Analysis integration.

### Phase 3: Post-Launch

- [ ] Voice Note Summaries (Urdu/Regional).
- [ ] PDF Report Analyzer (Upload Annual Report -> Get Summary).
- [ ] Direct Broker Integration (Trade execution).
