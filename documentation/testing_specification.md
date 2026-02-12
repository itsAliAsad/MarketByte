# Testing Specification & Quality Benchmarks - MarketByte

| Document Meta    | Details                             |
| :--------------- | :---------------------------------- |
| **Project**      | MarketByte (The Financial Co-Pilot) |
| **Version**      | 1.0                                 |
| **Status**       | 🟢 Draft                            |
| **Last Updated** | 2026-02-13                          |

---

## 1. Testing Strategy

### 1.1 Unit Testing

**Scope:** Individual functions and components.

- **Backend (Python/Lambda):** Use `pytest` to test isolated logic (e.g., parsing a PSX HTML table, calculating a P/E ratio, formatting a WhatsApp message).
- **Frontend (Web/React):** Use `Jest` + `React Testing Library` to test UI components (e.g., "Link WhatsApp" button click, Portfolio Card rendering).

### 1.2 Integration Testing

**Scope:** Interaction between two or more modules.

- **API -> Lambda:** Verify that API Gateway correctly triggers the Lambda and passes the payload.
- **Scraper -> DynamoDB:** Verify that scraped data is correctly written to the `MarketData` table with the right schema.
- **Lambda -> Bedrock:** Verify that the LLM receives the prompt and returns a valid string (mocking the actual Bedrock response for cost/speed, but occasionally hitting the real API).

### 1.3 End-to-End (E2E) Testing

**Scope:** Full user flows simulating real-world usage.

- **Onboarding Flow:**
  1. User Signs up on Web (Cognito).
  2. User scans QR / enters code on WhatsApp.
  3. System verifies link and sends "Welcome" message.
- **Daily Brief Flow:**
  1. Trigger EventBridge Scheduler manually.
  2. Verify `MarketData` is fetched.
  3. Verify `Users` table is scanned.
  4. Verify WhatsApp API endpoint receives the correct payload for a test user.

---

## 2. Quality Benchmarks (KPIs)

### 2.1 Core Platform

| Feature            | Metric                              | Benchmark / SLA                                        |
| :----------------- | :---------------------------------- | :----------------------------------------------------- |
| **Authentication** | Login Latency                       | **< 2.0 seconds** for 95% of requests.                 |
| **Responsiveness** | Interactive Command (`XRAY`, `OPP`) | **< 3.0 seconds** (WhatsApp Timeout limit).            |
| **Reliability**    | Daily Brief Delivery Rate           | **99.9%** (No more than 1 failed day per 3 years).     |
| **Scalability**    | Peak Throughput                     | Support **10,000 messages/min** during 9am/5pm bursts. |

### 2.2 Data Accuracy & Scrapers

| Feature          | Metric           | Benchmark / SLA                                                   |
| :--------------- | :--------------- | :---------------------------------------------------------------- |
| **Market Data**  | Price Accuracy   | **100%** match with PSX Data Portal.                              |
| **Parity Rates** | USD/PKR Accuracy | **100%** match with SBP Official Rate.                            |
| **Freshness**    | Data Latency     | Scraped data available in DB **< 5 minutes** after source update. |

### 2.3 AI & Intelligence

| Feature         | Metric                    | Benchmark / SLA                                                             |
| :-------------- | :------------------------ | :-------------------------------------------------------------------------- |
| **Summaries**   | Hallucination Rate        | **< 0.1%** (Strictly monitor numerical stats).                              |
| **Sentiment**   | Classification Accuracy   | **> 85%** alignment with human consensus (Fear vs Greed).                   |
| **Predictions** | High-Confidence Precision | **> 85%** accuracy for alerts claiming ">85% confidence".                   |
| **Predictions** | Recall                    | **> 60%** (It is better to miss an opportunity than to send a false alarm). |

---

## 3. Test Cases & Scenarios

### 3.1 Scenario: "Market Crash Alert" (Neural Network)

- **Input:** Simulate a -1000 point drop in KSE-100 and negative news text.
- **Expected Behavior:**
  - NN Model predicts "Bearish" with >90% confidence.
  - System filters for "Active Traders".
  - Push notification sent within 60 seconds of inference.
  - **Test Pass:** Alert delivered containing the phrase "Market Alert".

### 3.2 Scenario: "Web-to-WhatsApp Linking"

- **Input:**
  - Web User: `user@example.com` generates code `123456`.
  - WhatsApp User: `+923001234567` sends `123456`.
- **Expected Behavior:**
  - DynamoDB updates user record: `whatsapp_id` + `cognito_sub` linked.
  - Bot replies: "Verified! ✅".
  - **Test Pass:** User status changes to "Active" in DB.

### 3.3 Scenario: "Ex-Date Notification" (External Data)

- **Input:** `LUCK` announces Book Closure starting `2026-03-01`. Today is `2026-02-27`.
- **Expected Behavior:**
  - Scraper picks up date from PSX.
  - Logic identifies users holding `LUCK`.
  - Notification sent: "Reminder: LUCK Ex-Date is in 2 days."

---

## 4. Load & Stress Testing Plan

- **Tool:** Locust or AWS Distributed Load Testing.
- **Target:** API Gateway Endpoint (Webhook).
- **Load:** Simulate 500 concurrent users sending "XRAY" commands.
- **Success Criteria:**
  - API Gateway Error Rate < 0.1% (5xx).
  - Lambda Throttles < 1%.
  - DynamoDB Throttles = 0 (On-Demand mode active).
