<div align="center">

```mermaid
graph TD
    %% Hack: Using mermaid graph title solely for purple-styled text render (if supported) isn't standard,
    %% so we stick to standard ASCII text below but wrapped in a specific language block for potential coloration.
```

```text
  __  __            _        _   ____        _
 |  \/  | __ _ _ __| | _____| |_| __ ) _   _| |_ ___
 | |\/| |/ _` | '__| |/ / _ \ __|  _ \| | | | __/ _ \
 | |  | | (_| | |  |   <  __/ |_| |_) | |_| | ||  __/
 |_|  |_|\__,_|_|  |_|\_\___|\__|____/ \__, |\__\___|
                                       |___/
```

# MarketByte: The Financial Co-Pilot

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

---

## 🟣 Executive Summary

**MarketByte** (Code Name: _PSX-Brief_) is an AI-driven "Financial Co-Pilot" that lives inside WhatsApp. Our mission is to transform "blind" retail investors into informed wealth-builders by delivering personalized, jargon-free market intelligence that connects abstract indices to their daily lives.

In a market where retail investors often panic-sell due to a lack of context, **MarketByte** provides a frictionless bridge between complex financial data and actionable insights.

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

- **Logic**: Maps _Fund Name_ -> _Top 10 Holdings_.
- **User Action**: Reply "XRAY".
- **Response**: "You own Meezan Islamic Fund. This means you actually own: 1. Meezan Bank (15%), 2. Lucky Cement (8%)..."

### 3. 📡 Opportunity Radar

- **Logic**: Daily script filters stocks based on P/E < Sector Avg, Yield > 10%, RSI < 30.
- **User Action**: Reply "OPP".
- **Response**: "👀 **Undervalued Watch**: OGDC is trading at P/E 3.5x with 12% Yield."

### 4. 😰/🤑 Sentiment Analysis (Fear & Greed)

- **Input**: Financial news + Social sentiment.
- **Processing**: NLP scores from -1 (Extreme Fear) to +1 (Extreme Greed).
- **Display**: Visual Emoji Meter to help time the market.

---

## 🟣 Technical Architecture

MarketByte leverages the power of the **AWS Free Tier** to deliver enterprise-grade AI analysis at zero initial cost.

### Tech Stack

- **Interface**: WhatsApp Business API (via Meta/Twilio)
- **Backend Logic**: **AWS Lambda** (Python) for serverless execution.
- **Database**: **Amazon DynamoDB** (NoSQL) for fast user profiling and portfolio mapping.
- **AI/LLM**: **Amazon Bedrock** (Claude Haiku or Titan) for intelligent summarization and sentiment analysis.
- **Data Source**: Custom Python Scraper targeting market data portals.

### Data Flow

1.  **Ingest**: Scraper fetches Market Summary + News + Fund Reports.
2.  **Process**: Lambda cleans data.
3.  **Analyze**: **Amazon Bedrock** analyzes sentiment and extracts entities.
4.  **Match**: System queries **DynamoDB** for users matching extracted entities.
5.  **Draft**: Bedrock generates a personalized 3-line summary.
6.  **Deliver**: WhatsApp API sends the personalized payload.

---

## 🟣 UX / Interaction Flow

**Scenario: Morning Briefing**

> **Bot**: ☀️ Good Morning Ali!
>
> 📉 **KSE-100 is Down (-0.4%)** due to profit-taking before upcoming holidays.
>
> **Your Portfolio News**:
> 🏭 **Lucky Cement (LUCK)**: Announced a solar power plant. This cuts costs and improves long-term margins.
>
> **Market Mood**: 😨 Fear (Score: 35/100).
>
> 👇 _Tap below for more_
> [ 🔍 Deep Dive LUCK ] [ 📊 High Yield Stocks ]

---

## 🟣 Roadmap (Post-Hackathon)

- [ ] **Voice Notes**: Daily 30-second audio summary in Urdu/Regional languages. 🎙️
- [ ] **Analyst Tool**: User sends a PDF annual report -> Bot summarizes it. 📄
- [ ] **Broker Integration**: "One-tap" order placement (Regulatory Sandbox). 🏦

---

<div align="center">

**Current Status**: 🛠️ _Prototype / Planning Phase_
_Submitted for AWS 10,000 AIdeas Competition_

</div>
