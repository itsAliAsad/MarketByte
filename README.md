<div align="center">
<<<<<<< HEAD
<img src="assets/header.svg" alt="MarketByte ASCII Art" width="600"/>

### _Democratizing Financial Literacy for Retail Investors_

[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-7F39FB?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/bedrock/)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/lambda/)
[![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-4053D6?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/dynamodb/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![WhatsApp API](https://img.shields.io/badge/WhatsApp-Business%20API-25D366?style=for-the-badge&logo=whatsapp)](https://www.whatsapp.com/business/api)

<br/>

**Built for the [AWS 10,000 AIdeas Competition](https://aws.amazon.com/)**
_Track: Daily Life Enhancement / Workplace Efficiency_

<br/>

</div>

## 🟣 Executive Summary

**MarketByte** (Code Name: _PSX-Brief_) is an AI-driven "Financial Co-Pilot" that lives inside WhatsApp. Our mission is to transform "blind" retail investors into informed wealth-builders by delivering personalized, jargon-free market intelligence that connects abstract indices to their daily lives.

By leveraging **AWS Bedrock (GenAI)** and **Serverless Architecture**, MarketByte filters the noise of the financial world, delivering only what matters to _your_ portfolio.

> **"From panic-selling to data-driven confidence."**

---

## 🟣 The Problem: "Blind" Investing

Retail investors in Pakistan, especially Mutual Fund/SIP holders, face significant challenges:

- 📉 **Panic Selling**: They see fund balances drop and react emotionally without understanding the "why".
- 😵 **Information Overload**: Existing tools are either too complex (Bloomberg terminals) or too generic/spammy (broad news sites).
- 📵 **Lack of Context**: News is rarely filtered by what the user actually _owns_.

---

## 🟣 The Solution: Personalized Intelligence

**MarketByte** is a frictionless WhatsApp bot that filters daily market news based on the user's actual portfolio.

- **Smart Filtering**: Connects market movements directly to the user's holdings.
- **Plain Language**: Explains "why" in simple English/Urdu.
- **Data-Driven**: Highlights undervalued opportunities using real-time data, not rumors.

---

## 🟣 Target Audience

| Persona                                 | Profile                              | Pain Point                                         | Goal                                                 |
| :-------------------------------------- | :----------------------------------- | :------------------------------------------------- | :--------------------------------------------------- |
| **"The Passive Professional" (Ali)** 👔 | 32yo Manager, saves via Mutual Funds | Sees balance drop, considers stopping SIP          | Wants peace of mind without reading newspapers       |
| **"The Aspiring Trader" (Sara)** 👩‍💻     | 24yo CS Student, small savings       | Scared of losing money, confused by balance sheets | Wants "safe" undervalued stocks to start a portfolio |

---

## 🟣 Key Features

### 1. 🌤️ The Smart Daily Brief

_Delivered at 9:00 AM (Pre-market) or 5:00 PM (Post-market)_

- **Market Pulse**: 1-sentence summary of KSE-100 (Red/Green) + Context (e.g., Political/Economic).
- **Portfolio Match**: AI scans news specifically for _your_ holdings.
  - _Example_: "Your fund's top holding, **Engro**, reported profits today."

### 2. 🔍 Portfolio X-Ray

_Demystifying Mutual Funds_

- **Logic**: Maps _Fund Name_ -> _Top 10 Holdings_.
- **User Action**: Reply "XRAY".
- **Response**: "You own Meezan Islamic Fund. This means you actually own: 1. Meezan Bank (15%), 2. Lucky Cement (8%)..."
- **Sector Breakdown**: Shows exposure (e.g., "40% Banks, 20% Oil").

### 3. 📡 Opportunity Radar

_Data-Driven Discovery_

- **Logic**: Daily script filters stocks based on P/E < Sector Avg, Yield > 10%, RSI < 30.
- **User Action**: Reply "OPP".
- **Response**: "👀 **Undervalued Watch**: OGDC is trading at P/E 3.5x with 12% Yield."

### 4. 😰/🤑 Sentiment Analysis (Fear & Greed)

_The "Vibe Check"_

- **Input**: Financial news + Social sentiment (#PSX, #KSE100).
- **Processing**: NLP model scores sentiment from -1 (Fear) to +1 (Greed).
- **Display**: Visual Emoji Meter (😰 vs 🤑) to help time the market.

### 5. 🔮 AI Predictive Alerts

_Neural Network Forecasting_

- **Model**: Trained on 10 years of historical data (Tweets, Reports, Prices).
- **Action**: Alert triggers if prediction confidence > 85%.
- **Output**: "Breaking news regarding [Event] has an 88% similarity to [Past Event]. Expect volatility."

---

### Tech Stack

| Layer          | Technology                | Justification                                                |
| :------------- | :------------------------ | :----------------------------------------------------------- |
| **Frontend**   | **WhatsApp Business API** | Zero-install barrier; ubiquitous in Pakistan.                |
| **Compute**    | **AWS Lambda (Python)**   | Serverless, pay-per-use, rich financial libraries.           |
| **Database**   | **Amazon DynamoDB**       | Millisecond latency for user lookups; flexible schema.       |
| **AI / LLM**   | **Amazon Bedrock**        | Claude 3 Haiku is fast and cost-effective for summarization. |
| **Predictive** | **Amazon SageMaker**      | Hosts custom Neural Network for market trend prediction.     |
| **Storage**    | **Amazon S3**             | Data lake for historical news, tweets, and reports.          |

---

## 🟣 Data Sources & Integrity

We believe in **Data over Hype**. Our system aggregates data from trusted sources:

| Data Point           | Source                                          |
| :------------------- | :---------------------------------------------- |
| **USD/PKR Rates**    | State Bank of Pakistan (SBP) Official Rates     |
| **Market Prices**    | PSX Data Portal (DPS) - Real-time/Delayed       |
| **Foreign Flows**    | NCCPL (FIPI/LIPI) Daily Reports                 |
| **Corporate Action** | PSX Financial Announcements (Dividends/Bonuses) |

---

## 🟣 Roadmap

### Phase 1: Hackathon MVP (Current)

- [x] Core WhatsApp Bot Setup
- [x] User Profiling (Mock Data)
- [x] Daily Brief Generation (Text)
- [x] Basic Portfolio X-Ray

### Phase 2: Enhanced Features

- [ ] Real-time API integration for stock prices
- [ ] Sentiment Analysis integration
- [ ] Advanced Fee Calculator

### Phase 3: Post-Launch

- [ ] Voice Note Summaries (Urdu/Regional) 🎙️
- [ ] PDF Report Analyzer 📄
- [ ] Direct Broker Integration 🏦

---

<div align="center">

**Current Status**: 🛠️ _Prototype / Planning Phase_
_Submitted for AWS 10,000 AIdeas Competition_

</div>
