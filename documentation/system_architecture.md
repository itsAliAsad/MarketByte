# System Architecture Document - MarketByte (The Financial Co-Pilot)

| Document Meta    | Details             |
| :--------------- | :------------------ |
| **Project Name** | MarketByte          |
| **Code Name**    | PSX-Brief           |
| **Version**      | 1.0 (Hackathon MVP) |
| **Status**       | 🟢 Proposed         |
| **Last Updated** | 2026-02-13          |

---

## 1. High-Level Architecture Overview

MarketByte utilizes a fully **serverless, event-driven architecture** built on AWS. This ensures scalability, low maintenance, and cost-effectiveness (leveraging the AWS Free Tier). The system is designed to be asynchronous to handle high volumes of messages and scheduled tasks without blocking.

### 1.1 Core Components

1.  **User Interface:** WhatsApp (Chat) & Web Dashboard (Portfolio Mgmt).
2.  **Auth & API:** AWS Cognito (Identity) & API Gateway (Webhooks/REST).
3.  **Compute:** AWS Lambda (Serverless logic) & SageMaker (Model Inference).
4.  **Intelligence:** Amazon Bedrock (GenAI) & Custom Neural Network (Predictive AI).
5.  **Data Persistence:** DynamoDB (Hot Data) & S3 (Historical Data Lake).
6.  **Orchestration:** EventBridge (Scheduler).

### 1.2 Architecture Diagram

```mermaid
graph TD
    subgraph "Client Layer"
        WA[WhatsApp User]
        Web[Web Dashboard User]
    end

    subgraph Authentication
        Cognito[AWS Cognito]
    end

    subgraph "Entry Point"
        META[WhatsApp Business API]
        APIGW[AWS API Gateway]
    end

    subgraph "Compute & Logic"
        AuthLambda[Auth Service]
        OnboardLambda[Onboarding Lambda]
        DailyLambda[Daily Brief Orchestrator]
        XRayLambda[X-Ray Service]
        OppLambda[Opportunity Service]
        ScraperLambda[Data Scraper]
    end

    subgraph Intelligence
        Bedrock[Amazon Bedrock<br>(Claude 3 Haiku)]
        SageMaker[Amazon SageMaker<br>(Predictive NN)]
    end

    subgraph "Data Persistence"
        DDB[(Amazon DynamoDB)]
        S3[(S3 Data Lake)]
    end

    subgraph "External Sources"
        PSX[PSX Data Portal]
        SBP[State Bank (Forex)]
        NCCPL[NCCPL (Smart Money)]
        News[Financial News]
    end

    %% Flows
    WA -->|Messages| META
    META -->|Webhook| APIGW
    Web -->|Auth/Link| Cognito
    Web -->|Portfolio View| APIGW

    APIGW -->|Route: Hi| OnboardLambda
    APIGW -->|Route: XRAY| XRayLambda
    APIGW -->|Route: OPP| OppLambda

    OnboardLambda -->|Verify Link| Cognito
    OnboardLambda -->|Save Profile| DDB

    DailyLambda -->|Schedule| EventBridge[EventBridge Scheduler]
    EventBridge -->|Trigger| DailyLambda
    DailyLambda -->|Fetch Portfolio| DDB
    DailyLambda -->|Summarize| Bedrock
    DailyLambda -->|Send Brief| META

    XRayLambda -->|Get Holdings| DDB
    OppLambda -->|Get Screeners| DDB

    ScraperLambda -->|Fetch Data| PSX
    ScraperLambda -->|Fetch Forex| SBP
    ScraperLambda -->|Fetch Flows| NCCPL
    ScraperLambda -->|Fetch News| News

    ScraperLambda -->|Write Hot Data| DDB
    ScraperLambda -->|Write Historical| S3

    S3 -->|Training Data| SageMaker
    SageMaker -->|Inference Alerts| DailyLambda
```

---

## 2. Technology Stack

| Layer             | Technology                          | Justification                                                                                                                                          |
| :---------------- | :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**      | **WhatsApp Business API**           | Ubiquitous platform in Pakistan; zero-install barrier for users. Integration via Meta Direct or Twilio (Sandbox).                                      |
| **API Layer**     | **AWS API Gateway**                 | Managed REST API to securely expose Lambda functions to the WhatsApp Webhook.                                                                          |
| **Compute**       | **AWS Lambda (Python 3.11)**        | Serverless execution model pays only for compute time. Python offers rich libraries for finance (`pandas`) and scraping (`requests`, `beautifulsoup`). |
| **Database**      | **Amazon DynamoDB**                 | Single-digit millisecond latency for user profile lookups. Schema flexibility for evolving financial data models.                                      |
| **AI / LLM**      | **Amazon Bedrock (Claude 3 Haiku)** | "Haiku" model acts as the sweet spot for speed and costintelligence for summarization tasks.                                                           |
| **Predictive AI** | **Amazon SageMaker**                | Hosts the custom Neural Network trained on 10 years of historical data for market prediction.                                                          |
| **Data Lake**     | **Amazon S3**                       | Stores raw historical tweets, news, and reports for model training and retraining.                                                                     |
| **Scheduling**    | **Amazon EventBridge**              | Reliable cron-like scheduling for the 9:00 AM and 5:00 PM briefing triggers.                                                                           |
| **IaC**           | **AWS SAM / Terraform**             | Infrastructure as Code for reproducible deployments.                                                                                                   |

---

## 3. Data Flow Architecture

### 3.1 Flow 1: Inbound Message Handling (User -> Bot)

This flow handles commands like "Hi", "XRAY", "OPP".

1.  **User** sends a message via WhatsApp.
2.  **WhatsApp** forwards the payload to the **API Gateway** webhook URL.
3.  **API Gateway** triggers the `entry-point-lambda`.
4.  **Lambda** parses the message intention:
    - _If "Hi":_ Triggers `onboarding-flow`.
    - _If "XRAY":_ Triggers `xray-service` -> Fetches Fund Data -> Calls Bedrock (Optional) -> Returns Formatted Text.
    - _If "OPP":_ Triggers `opportunity-service` -> Queries `MarketData` Table -> Returns Top 3 Stocks.
5.  **Lambda** calls the WhatsApp API to send the response back to the user.

### 3.2 Flow 2: Daily Briefing (Scheduled Push)

This flow executes at 9:00 AM and 5:00 PM.

1.  **EventBridge** triggers the `daily-brief-orchestrator-lambda`.
2.  **Orchestrator** scans the `Users` DynamoDB table for active subscribers.
3.  **Orchestrator** splits users into batches and puts messages onto an **SQS Queue** (for rate limiting and reliability).
4.  **Worker Lambdas** consume from SQS.
5.  **For each user:**
    - Fetch User Portfolio (e.g., Meezan Fund).
    - Fetch Daily Market Data & News from `MarketData` table.
    - **Filter:** specific news relevant to the portfolio.
    - **Generate:** Call **Amazon Bedrock** with a prompt: _"Summarize these 3 news items for a user who holds [Fund Name]. Keep it under 3 lines."_
6.  **Worker Lambda** sends the final personalized message via WhatsApp API.

### 3.3 Flow 3: Data Ingestion & Training Pipeline

This flow keeps the `MarketData` table fresh and feeds the Neural Network.

1.  **EventBridge** triggers `scraper-lambda` every 30 minutes (during market hours) and specifically at market close (5:00 PM).
2.  **Scraper** executes targeted fetch routines:
    - **Forex:** Scrapes SBP `ecodata/CRates` for USD/PKR.
    - **Market Data:** Queries PSX DPS for real-time rates.
    - **Smart Money:** Scrapes NCCPL `fipi-normal-daily` (parses PDF/HTML table).
    - **Corporate:** Scrapes PSX Financial & Corporate Announcements.
    - **Macro:** Checks SBP (Policy Rate) and PBS (CPI).
3.  **Scraper** writes hot data to **DynamoDB** (for current day access) and raw data to **S3 Data Lake** (for historical archive).
4.  **SageMaker Pipeline** (triggered weekly) retrains the Neural Network model using the updated S3 dataset to refine prediction accuracy.

---

## 4. Database Schema Design (DynamoDB)

### 4.1 Table: `MarketByte_Users`

- **Partition Key:** `whatsapp_id` (String)
- **Attributes:**
  - `name` (String)
  - `profile_type` (Enum: 'fund', 'stock')
  - `holdings` (List[String]) - e.g., `["Meezan Islamic Fund"]`
  - `joined_at` (Timestamp)
  - `status` (String) - e.g., "active", "blocked"

### 4.2 Table: `MarketByte_Funds`

- **Partition Key:** `fund_name` (String)
- **Attributes:**
  - `top_holdings` (Map) - e.g., `{"MEBL": 15.4, "LUCK": 8.1}`
  - `last_updated` (Timestamp)
  - `expense_ratio` (Number)

### 4.3 Table: `MarketByte_DailyData`

- **Partition Key:** `date` (String) - `YYYY-MM-DD`
- **Sort Key:** `data_type` (String) - e.g., `NEWS`, `PRICES`, `SENTIMENT`
- **Attributes:**
  - `payload` (JSON) - Raw data for that day.
  - `ttl` (Number) - Time to Live for automatic cleanup after 30 days.

---

## 5. Security & Compliance

1.  **Data Privacy:**
    - No PII (Personally Identifiable Information) other than the phone number is stored.
    - Portfolio data is aggregated; exact investment amounts are NOT stored (unless user actively inputs for a calculator session, which is transient).
2.  **API Security:**
    - **API Gateway** uses usage plans and API keys to prevent DDoS.
    - **WhatsApp Webhook** verification token implementation to ensure requests come from Meta.
3.  **IAM Roles:**
    - Strict **Least Privilege** access. Lambdas only have access to the specific DynamoDB tables and Bedrock models they need.

---

## 6. Scalability Strategy

- **Serverless:** Lambda scales automatically with the number of incoming requests.
- **DB Throttling:** DynamoDB configured with On-Demand Capacity mode to handle burst traffic during the 9:00 AM / 5:00 PM blasts.
- **Queueing:** SQS acts as a buffer for the notification system to ensure we don't hit WhatsApp API rate limits.

---

## 7. Interfaces & Integration Points

- **WhatsApp API:**
  - `POST /messages`: Send text and template messages.
  - `POST /media`: Upload images (for charts/graphs).
- **Amazon Bedrock:**
  - `InvokeModel`: Call Claude 3 Haiku.
  - _Prompt Engineering:_ Centralized prompt templates stored in Lambda layers or DynamoDB config for easy updates without code deploys.
