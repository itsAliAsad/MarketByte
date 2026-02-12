# User Stories - The Financial Co-Pilot (PSX-Brief)

**Project Name:** The Financial Co-Pilot (Code Name: PSX-Brief)
**Version:** 1.0 (Hackathon MVP)
**Status:** Draft

## 1. Personas Overview

### primary: "The Passive Professional" (Ali)

- **Profile:** 32-year-old Corporate Manager. Saves Rs. 20k/month in a Meezan Mutual Fund.
- **Goal:** Wants peace of mind. Wants to know his money is safe without reading a newspaper.

### Secondary: "The Aspiring Trader" (Sara)

- **Profile:** 24-year-old CS Student. Has Rs. 50k savings.
- **Goal:** Wants to find "safe" undervalued stocks to start her portfolio.

---

## 2. Epics & User Stories

### Epic 1: Onboarding & User Profiling

**Goal:** Successfully register users and understand their investment type (Index vs. Stock Picker) with zero friction.

| ID         | As a...                | I want to...                                                                 | So that...                                                              |
| ---------- | ---------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **US-1.1** | First-time User        | Sign up and log in securely via the website using **AWS Cognito**            | My account is protected and my portfolio settings are secure.           |
| **US-1.2** | New Investor           | Configure my "Index Investor" or "Stock Picker" profile on the web dashboard | It is easier to select funds/stocks with a full UI than typing in chat. |
| **US-1.3** | Dashboard User         | Generate a secure "Link WhatsApp" code/token                                 | I can connect my mobile number to my web account.                       |
| **US-1.4** | WhatsApp User          | Send the link code to the bot to activate my subscription                    | The bot knows exactly who I am and what I want to track.                |
| **US-1.5** | Privacy-Conscious User | Know that my authentication is handled by a standard provider (AWS)          | I trust the platform with my basic identity info.                       |

### Epic 2: The Smart Daily Brief (Core Feature)

**Goal:** Deliver a concise, personalized market summary at 9:00 AM or 5:00 PM.

| ID         | As a...                | I want to...                                                                    | So that...                                                                                                       |
| ---------- | ---------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **US-2.1** | Passive Investor (Ali) | Receive a notification at a predictable time (9:00 AM / 5:00 PM)                | I can build a habit of checking the market without thinking about it.                                            |
| **US-2.2** | Busy Professional      | Read a 1-sentence summary of the KSE-100 index performance (Red/Green + Reason) | I can instantly know the general market mood without reading a strictly detailed report.                         |
| **US-2.3** | Portfolio Holder       | See news specifically about _my_ holdings (or my fund's top holdings)           | I don't waste time filtering through irrelevant noise about companies I don't own.                               |
| **US-2.4** | User                   | Identify the key reason for market movement (Political vs. Economic)            | I understand context (e.g., "Market down due to profit-taking" vs. "Market crash due to political instability"). |
| **US-2.5** | User                   | Read the brief in simple English (or Urdu in future scope)                      | I can understand the content even if I am not a financial expert.                                                |
| **US-2.6** | User                   | Have a strict limit of 3 bullet points per brief                                | I am not overwhelmed by a "wall of text."                                                                        |

### Epic 3: Portfolio X-Ray

**Goal:** Demystify mutual funds by showing the underlying assets.

| ID         | As a...            | I want to...                                                                                    | So that...                                                |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **US-3.1** | Mutual Fund Holder | Send the command "XRAY" to the bot                                                              | I can trigger an analysis of my specific mutual fund.     |
| **US-3.2** | Passive Investor   | See the top 3-5 companies my fund actually owns (e.g., "Your Meezan Fund owns 15% Meezan Bank") | I feel a sense of tangible ownership in the real economy. |
| **US-3.3** | Investor           | Understand the sector allocation of my fund (e.g., "Heavy in Cement & Banking")                 | I know which industries my money is exposed to.           |

### Epic 3.5: X-Ray Advanced Enhancements (New)

**Goal:** Provide deeper transparency and actionable insights for fund holders.

| ID           | As a...                | I want to...                                                                               | So that...                                                                        |
| ------------ | ---------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **US-3.5.1** | Fee-Conscious Investor | See the _actual Rupee amount_ I paid in management fees this month (e.g., "Rs. 208")       | I understand the real cost of my investment beyond just a percentage.             |
| **US-3.5.2** | Diversified Investor   | See my aggregated sector exposure across _all_ my funds                                    | I can spot concentration risks (e.g., "45% of your total portfolio is in Banks"). |
| **US-3.5.3** | Income Investor        | Get notified when a company inside my fund declares a dividend                             | I know when to expect a potential NAV boost from "invisible" income.              |
| **US-3.5.4** | Vigilant Investor      | Be alerted if my Fund Manager makes a significant buy/sell decision (e.g., "Sold 50% TRG") | I can track "Smart Money" moves and adjust my own strategy.                       |
| **US-3.5.5** | Analytical Investor    | Know exactly which stock is responsible for my fund's daily drop (Performance Attribution) | I understand _why_ I lost money today (e.g., "Fund down due to LUCK -3%").        |
| **US-3.5.6** | Aspiring Trader        | See a "Cost of Convenience" comparison (Fund Fees vs. Direct Stock Ownership costs)        | I can decide if I should graduate to buying stocks directly.                      |
| **US-3.5.7** | Risk-Aware Investor    | Simulate market shocks (e.g., "What if Oil drops 20%?") on my specific portfolio           | I can understand my downside risk in concrete terms.                              |

### Epic 4: Opportunity Radar & Discovery

**Goal:** Help users find undervalued investment opportunities based on data.

| ID         | As a...                | I want to...                                                                | So that...                                                           |
| ---------- | ---------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **US-4.1** | Aspiring Trader (Sara) | Send the command "OPP" (Opportunity)                                        | I can request a list of potential investment ideas on demand.        |
| **US-4.2** | Value Investor         | See stocks with a P/E ratio lower than their sector average                 | I can identify companies that are potentially undervalued.           |
| **US-4.3** | Dividend Seeker        | See stocks with a Dividend Yield > 10%                                      | I can find stocks that provide regular passive income.               |
| **US-4.4** | Technical Trader       | See stocks with RSI < 30 (Oversold)                                         | I can identify potential "dip buy" opportunities.                    |
| **US-4.5** | Cautious Investor      | See a clear disclaimer ("Not financial advice") with every opportunity list | I remember to do my own research and don't blame the bot for losses. |

### Epic 5: Sentiment Analysis (The "Vibe Check")

**Goal:** Quantify market emotion to prevent panic selling or FOMO buying.

| ID         | As a...             | I want to...                                                               | So that...                                                                              |
| ---------- | ------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **US-5.1** | Nervous Investor    | See a visual "Fear & Greed" meter (Emoji based: 😨 vs 🤑)                  | I can intuitively grasp the market's psychological state.                               |
| **US-5.2** | Contrarian Investor | Know when the market is in "Extreme Fear"                                  | I can consider this a potential buying opportunity (be greedy when others are fearful). |
| **US-5.3** | User                | See the sentiment score derived from news and social media (#PSX, #KSE100) | I know the sentiment is based on real-time discussions, not just price action.          |

### Epic 6: AI Predictive Alerts (Neural Network)

**Goal:** Leverage 10 years of historical data to predict market reactions to new events.

| ID         | As a...          | I want to...                                                               | So that...                                                             |
| ---------- | ---------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **US-6.1** | Active Trader    | Be alerted _immediately_ if a news event is predicted to cause a >2% drop  | I can exit my position before the wider market reacts.                 |
| **US-6.2** | Long-Term Holder | Receive a "Volatility Warning" based on similar historical patterns        | I am visually prepared for a dip and don't panic sell.                 |
| **US-6.3** | Analytical User  | See the "Confidence Score" of the AI's prediction (e.g., "88% Confidence") | I can weigh the AI's advice against my own judgment.                   |
| **US-6.4** | Data Skeptic     | Know that the prediction is based on 10 years of tweets, reports, and news | I trust that this isn't just a random guess but a data-backed insight. |

### Epic 6: User Interaction & Experience (UX)

**Goal:** Ensure the WhatsApp interface is intuitive and "app-like" without being an app.

| ID         | As a...      | I want to...                                                  | So that...                                                   |
| ---------- | ------------ | ------------------------------------------------------------- | ------------------------------------------------------------ |
| **US-6.1** | Mobile User  | Interact via clickable WhatsApp buttons/menus (Quick Replies) | I don't have to memorize text commands like "XRAY" or "OPP". |
| **US-6.2** | Curious User | Tap "Deep Dive" on a specific news item                       | I can get more details if a headline catches my interest.    |
| **US-6.3** | User         | See the "Last Updated" timestamp on market data               | I know I am looking at fresh data and not stale cache.       |
| **US-6.4** | User         | Opt-out or unsubscribe easily                                 | I don't feel trapped if I no longer want the service.        |

---

## 3. Non-Functional Requirements (Constraints)

- **Latency:** The bot must respond to commands ("XRAY", "OPP") within 3 seconds.
- **Reliability:** The Daily Brief must be delivered with 99.9% reliability at the scheduled time.
- **Accuracy:** Financial data (Price, % Change) must be hard-coded from the source, minimizing AI hallucination risk.
- **Compliance:** All "advice" or specific stock mentions must include a standard financial disclaimer.
- **Platform:** Must operate strictly within WhatsApp Business API rate limits and template guidelines to avoid bans.
