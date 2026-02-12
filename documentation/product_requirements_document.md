# Product Requirements Document (PRD) - MarketByte

| Document Meta    | Details                             |
| :--------------- | :---------------------------------- |
| **Project Name** | MarketByte (The Financial Co-Pilot) |
| **Code Name**    | PSX-Brief                           |
| **Version**      | 1.0 (Hackathon MVP)                 |
| **Status**       | 🟢 Approved                         |
| **Owner**        | User                                |
| **Last Updated** | 2026-02-13                          |

---

## 1. Executive Summary

**MarketByte** is a WhatsApp-based AI financial assistant designed to bridge the gap between complex market data and retail investor portfolios. By leveraging Generative AI (AWS Bedrock) and serverless architecture (AWS Lambda), it delivers hyper-personalized, jargon-free market intelligence directly to users' chat apps. The core innovation lies in filtering "noise" by focusing strictly on the user's specific holdings and translating technical financial events into actionable, simple English insights.

### 1.1 Problem Statement

Retail investors, particularly those new to mutual funds or stocks, often panic-sell during market downturns due to a lack of context. Traditional financial news is either too broad (irrelevant to their specific portfolio) or too technical (hard to understand).

### 1.2 Proposed Solution

An automated "Financial Co-Pilot" that:

1.  **Ingests** market data and news.
2.  **Filters** it against user portfolios.
3.  **Synthesizes** it into a 3-line summary using GenAI.
4.  **Delivers** it via WhatsApp at 9:00 AM and 5:00 PM.

---

## 2. User Personas

### 2.1 Primary: "The Passive Professional" (Ali)

- **Demographics:** 32 years old, Corporate Manager.
- **Financial Profile:** Saves Rs. 20k/month in a Meezan Mutual Fund (SIP).
- **Psychographics:** Risk-averse, busy, values peace of mind.
- **Pain Point:** Sees his fund balance drop in an app but doesn't know _why_. Panics and considers stopping his SIP.
- **Need:** A simple notification saying, "Your fund is down because Lucky Cement (a top holding) dropped due to a one-time tax. Fundamentals are strong."

### 2.2 Secondary: "The Aspiring Trader" (Sara)

- **Demographics:** 24 years old, CS Student.
- **Financial Profile:** Rs. 50k savings, wants to try direct stock trading.
- **Psychographics:** Tech-savvy, curious, but intimidated by complex charts.
- **Pain Point:** Doesn't know how to screen thousands of stocks to find "safe" value buys.
- **Need:** A "scanner" that lists undervalued stocks based on logical metrics (P/E, Dividend Yield).

---

## 3. Scope & Feature Requirements

### 3.1 Functional Requirements (FR)

#### Epic 1: Onboarding & User Profiling

- **FR-1.1:** The system shall provide a web-based portal for secure user sign-up and sign-in using **AWS Cognito**.
- **FR-1.2:** The system must enforce authentication before allowing access to portfolio configuration.
- **FR-1.3:** The system shall allow users to configure their portfolio (Funds/Stocks) via the web interface.
- **FR-1.4:** The system shall generate a unique linking code or mechanism to associate the web account with the user's WhatsApp ID.
- **FR-1.5:** The system shall securely map the authenticated Cognito User ID (sub) to the WhatsApp ID in DynamoDB.

#### Epic 2: The Smart Daily Brief (Core)

- **FR-2.1:** The system shall trigger a batch process at 9:00 AM and 5:00 PM PKT daily.
- **FR-2.2:** The AI model shall generate a "Market Pulse" summary (1 sentence) explaining the KSE-100 index movement.
- **FR-2.3:** The system must cross-reference daily news with each user's portfolio.
  - _Constraint:_ If no specific news exists for a holding, show sector-level news.
- **FR-2.4:** The briefing must not exceed 3 bullet points per user.
- **FR-2.5:** The output language must be simple English (Grade 8 reading level).

#### Epic 3: Portfolio X-Ray

- **FR-3.1:** Upon receiving the command `XRAY`, the system shall retrieve the latest "Fund Manager Report" data for the user's selected fund.
- **FR-3.2:** The response must list the Top 5 holdings of that fund with their percentage weights.
- **FR-3.3:** The system shall display a "Sector Breakdown" summary (e.g., "Banks: 40%, Oil: 20%").
- **FR-3.4 (New):** The system shall calculate an estimated monthly fee in Rupees based on the user's total investment value (input optional) and the fund's expense ratio.

#### Epic 4: Opportunity Radar

- **FR-4.1:** Upon receiving the command `OPP`, the system shall query the latest market data.
- **FR-4.2:** The system shall filter stocks based on:
  - **Value:** P/E < Sector Average.
  - **Income:** Dividend Yield > 10%.
  - **Technical:** RSI < 30 (Oversold).
- **FR-4.3:** The response shall list the top 3 matching stocks with the relevant metric highlighted.
- **FR-4.4:** Every `OPP` response must append a disclaimer: "Not financial advice. Do Your Own Research (DYOR)."

#### Epic 5: Sentiment Analysis

- **FR-5.1:** The system shall analyze daily financial news headlines and relevant tweets (#PSX).
- **FR-5.2:** The system shall generate a "Fear & Greed" score (0-100) and assign a corresponding emoji.
- **FR-5.3:** This score shall be included in the Daily Briefing footer.

#### Epic 6: AI Predictive Alerts (Neural Network)

- **FR-6.1:** The system shall maintain a historical data lake containing 10 years of: PSX market movements, financial news, company annual reports, and social media tweets.
- **FR-6.2:** A custom Neural Network model shall be trained on this dataset to identify correlations between events and price movements.
- **FR-6.3:** The system shall ingest real-time news/events and run inference through the model to predict potential impact (Bullish/Bearish > X% confidence).
- **FR-6.4:** If a high-confidence prediction is made, the system shall push an immediate "Market Alert" to relevant users.
- **FR-6.5:** The system shall continuously retrain/fine-tune the model with new daily data.

#### Epic 7: Advanced Data Ingestion

- **FR-7.1 (Forex):** The system shall scrape daily USD/PKR weighted average customer exchange rates from the State Bank of Pakistan (SBP).
- **FR-7.2 (Market Data):** The system shall fetch real-time/delayed volume, price, and High/Low data from the PSX Data Portal (DPS).
- **FR-7.3 (Smart Money):** The system shall ingest daily Foreign Investor Portfolio Investment (FIPI) and Local Investor Portfolio Investment (LIPI) data from NCCPL.
- **FR-7.4 (Corporate Actions):** The system shall track "Book Closure" and "Ex-Dates" from the PSX Financial Announcements page.
- **FR-7.5 (Insider Trading):** The system shall scan PSX Corporate Announcements for keywords like "Director," "CEO," or "Buy/Sell."
- **FR-7.6 (Macro):** The system shall monitor SBP for Policy Rate changes and PBS for monthly CPI Inflation reports.

### 3.2 Non-Functional Requirements (NFR)

- **NFR-1 (Performance):** Interactive commands (`XRAY`, `OPP`) must respond within 3 seconds to prevent WhatsApp timeouts.
- **NFR-2 (Reliability):** The scheduled Daily Brief must have a delivery success rate of 99.9%.
- **NFR-3 (Accuracy):** Numerical data (Price, Change %, Yield) must be deterministic (database lookup), _never_ generated by the LLM. The LLM is strictly for text summarization.
- **NFR-4 (Cost):** The architecture must primarily utilize AWS Free Tier resources (Lambda, DynamoDB WCU/RCU limits).
- **NFR-5 (Compliance):** All messages must comply with WhatsApp Business Policy (no promotional spam).

---

## 4. User Interaction Design

### 4.1 Flow: Onboarding (Web - Hybrid)

1.  **Web Portal:** User visits `marketbyte.app` and signs up/logs in via AWS Cognito.
2.  **Web Portal:** User selects "Mutual Fund Investor" and adds "Meezan Islamic Fund" to their dashboard.
3.  **Web Portal:** User clicks "Connect WhatsApp". System displays a QR code or unique text code (e.g., `MB-1234`).
4.  **WhatsApp:**
    > **User:** (Sends code) MB-1234
    > **Bot:** Verified! ✅ Your WhatsApp is now linked to your web profile. You'll receive your first Smart Brief at 5:00 PM.

### 4.2 Flow: Daily Brief

> **Bot:** 🔔 **MarketByte Evening Brief**
>
> 📉 **Market Pulse:** KSE-100 fell 400 points today due to uncertainty regarding the IMF tranche release.
>
> 💼 **Your Portfolio Impact:**
>
> - **Meezan Bank (MEBL):** Your fund's top holding announced a record dividend of Rs. 8/share. This is positive for long-term growth.
>
> 🧠 **Sentiment:** 😨 Fear (Score: 32)
>
> 👇 _Want more?_
> [ Button: View X-Ray ] [ Button: Find Opportunities ]

---

## 5. Technical Architecture

### 5.1 System Diagram

- **Authentication:** AWS Cognito (User Pools for Identity, Identity Pools for Access).
- **Data Source:** Custom Python Scraper (runs on AWS Lambda + EventBridge).
- **Historical Data:** S3 Data Lake (10 years of Tweets, News, Reports, Prices).
- **Intelligence:**
  - **GenAI:** Amazon Bedrock (Claude 3 Haiku) for summarization.
  - **Predictive AI:** Custom Neural Network (TensorFlow/PyTorch) for trend forecasting.
- **Database:** DynamoDB (Tables: `Users`, `MarketData`, `FundHoldings`).
- **Backend:** AWS Lambda (Function URLs / API Gateway) + SageMaker (Model Inference).
- **Frontend:** WhatsApp Business API (via Meta) & Web Dashboard (React/Next.js).

### 5.3 External Data Sources

| Data Point                  | Source                        | URL                                                                                | Notes                                             |
| :-------------------------- | :---------------------------- | :--------------------------------------------------------------------------------- | :------------------------------------------------ |
| **USD/PKR Parity**          | State Bank of Pakistan (SBP)  | [Link](https://www.sbp.org.pk/ecodata/CRates/index.asp)                            | Official weighted average customer rates.         |
| **Market Data**             | PSX Data Portal (DPS)         | [Link](https://dps.psx.com.pk/)                                                    | Real-time/delayed volume, prices, High/Low.       |
| **Smart Money (FIPI/LIPI)** | NCCPL                         | [Link](https://www.nccpl.com.pk/en/market-information/fipi-lipi/fipi-normal-daily) | Daily summary (PDF/Table) of foreign/local flows. |
| **Corporate Calendar**      | PSX Financial Announcements   | [Link](https://www.psx.com.pk/psx/announcement/financial-announcements)            | Track "Book Closure" and "Ex-Date".               |
| **Insider Dealings**        | PSX Corporate Announcements   | [Link](https://www.psx.com.pk/psx/announcement/corporate-announcements)            | Filter for "Director", "CEO", "Buy/Sell".         |
| **Policy Rate**             | State Bank of Pakistan (SBP)  | [Link](https://www.sbp.org.pk/m_policy/index.asp)                                  | Interest Rate announcements.                      |
| **Inflation (CPI)**         | Pakistan Bureau of Statistics | [Link](https://www.pbs.gov.pk/detail-info)                                         | Monthly Price Indices / Inflation Reports.        |

### 5.2 Data Model

**Table: Users**

```json
{
  "user_id": "ITEM_UUID_FROM_COGNITO",
  "cognito_sub": "d4e5f6g7-h8i9-...",
  "whatsapp_id": "923001234567",
  "profile_type": "fund",
  "holdings": ["Meezan Islamic Fund"],
  "subscription_status": "active",
  "last_interaction": "2023-10-27T10:00:00Z"
}
```

**Table: FundHoldings**

```json
{
  "fund_name": "Meezan Islamic Fund",
  "updated_at": "2023-10-01",
  "top_holdings": [
    { "symbol": "MEBL", "weight": 15.5 },
    { "symbol": "LUCK", "weight": 8.2 },
    { "symbol": "ENGRO", "weight": 7.1 }
  ]
}
```

---

## 6. Success Metrics (KPIs)

- **Activation Rate:** % of users who complete onboarding (Target: >80%).
- **Retention:** % of users who do NOT block the bot after 7 days (Target: >90%).
- **Engagement:** % of users who tap "Deep Dive" or "XRAY" buttons (Target: >15%).

---

## 7. Risks & Mitigation

| Risk                  | Probability | Impact | Mitigation                                                              |
| :-------------------- | :---------- | :----- | :---------------------------------------------------------------------- |
| **LLM Hallucination** | Medium      | High   | Hard-code all numbers. Use LLM only for "Why" explanations.             |
| **WhatsApp Ban**      | Low         | High   | Strictly adhere to "Utility" template categories. Provide easy Opt-out. |
| **Data Latency**      | High        | Medium | Timestamp all data. Explicitly state "Closing Price" vs "Real-time".    |

---

## 8. Development Roadmap (Hackathon)

1.  **Day 1:** Set up AWS Environment, DynamoDB Tables, and Scraper.
2.  **Day 2:** Implement Bedrock integration and "Daily Brief" Prompt Engineering.
3.  **Day 3:** Build WhatsApp integration (Twilio/Meta) and "XRAY" logic.
4.  **Day 4:** End-to-end testing, refinement of notification schedules.

---

**Approvals**

- [ ] Product Owner
- [ ] Tech Lead
