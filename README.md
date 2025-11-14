# 📰 Event-Driven ETL Pipeline

## Project Overview

This repository hosts a modular, production-ready **ETL (Extract, Transform, Load) pipeline** designed to monitor and analyze market sentiment based on global news flow.

The core goal is to demonstrate end-to-end Data Engineering skills by processing unstructured text data, enriching it with **Sentiment Analysis (VADER)**, and structuring it for DWH (Data Warehouse) consumption.

---

## 🛠️ Technology Stack

| Category | Tools Used | Purpose |
| :--- | :--- | :--- |
| **Orchestration** | Apache Airflow (Conceptual DAG) | Scheduling and managing task dependencies (E -> T -> L). |
| **Containerization**| **Docker** | Packaging the entire environment (Python, dependencies) for portable deployment. |
| **Languages/Libraries**| Python (Pandas, Requests, NLTK) | Data extraction, cleaning, and transformation. |
| **Storage/Query** | SQLite (Imitation DWH), Advanced SQL (CTE, Window Functions) | Storing structured results and performing complex analytical queries. |

---

## 🎯 Pipeline Architecture and Flow

The project is structured into three main modules:

1.  **Extraction (`src/extract.py`):** Connects to a public News API, handles paginated requests to bypass rate limits, and ingests raw articles.
2.  **Transformation & Load (`src/transform_load.py`):**
    * Cleans raw data and applies **VADER Sentiment Analysis** to the headlines.
    * Generates a `sentiment_score` (-1.0 to +1.0) and loads the structured data into the SQLite DWH.
3.  **Analysis (`.ipynb`):** Runs advanced SQL queries (e.g., source comparison, sentiment bias calculation) against the DWH to derive business-relevant insights.

## 🚀 How to Run the Project (Local/Codespaces)

### Prerequisites

1.  **API Key:** Obtain a valid API key from a news provider (e.g., News API).
2.  **Dependencies:** Ensure Python 3.9+ is installed.

### Step 1: Clone and Set Up Environment

```bash
# Clone the repository
git clone [https://github.com/Ekakatya/social-impact-data-flow.git](https://github.com/Ekakatya/social-impact-data-flow.git)
cd social-impact-data-flow

# Install dependencies
pip install -r requirements.txt
