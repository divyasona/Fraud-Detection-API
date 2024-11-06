# Fraud Detection and Financial Analysis API

Welcome to the Fraud Detection and Financial Analysis API repository! This project demonstrates the integration of data analytics, financial analysis, and manual testing through a FastAPI-based RESTful API. It includes endpoints for transaction retrieval, fraud detection, financial summaries, and synthetic data generation, making it a comprehensive solution for financial transaction analysis and anomaly detection.

## Features

- **Fraud Detection**: Identifies suspicious transactions based on transaction patterns and anomaly detection.
- **Financial Analysis**: Provides summaries of transactions by type, including total debits and credits.
- **Manual and Automated Testing**: Includes `pytest` test cases and manual testing procedures for endpoint validation.
- **Generative AI for Synthetic Data**: Generates synthetic transaction data to support model training and testing.

## Technology Stack

- **Backend Framework**: FastAPI
- **Data Processing**: Pandas
- **Testing**: pytest, TestClient
- **Data Generation**: scikit-learn (for synthetic data)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd Fraud-Detection-API
2. **Set Up Virtual Environment**:
python -m venv venv
3. **Activate the Virtual Environment**:
.\venv\Scripts\activate
4. **Install Dependencies**:
pip install -r requirements.txt
5. Run the API:
uvicorn main:app --reload
6. Access the API Documentation: Open http://127.0.0.1:8000/docs in your browser to explore and test the API endpoints via Swagger UI.

**Data Description**
**File**: transactions.csv
**Columns**:
transaction_id: Unique transaction identifier
customer_id: Customer identifier
transaction_date: Transaction date in YYYY-MM-DD format
amount: Monetary amount of the transaction
transaction_type: Type of transaction (e.g., debit, credit)
is_fraud: Binary label (0 or 1) indicating if the transaction is fraudulent

**main.py**
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load data
transactions_df = pd.read_csv("transactions.csv")

@app.get("/transactions")
async def get_transactions():
    return transactions_df.to_dict(orient="records")

**test_main.py**
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200

**Future Enhancements**
**Enhanced Fraud Detection Algorithm**: Improve fraud detection logic using advanced ML models.
User Authentication: Add authentication to secure API endpoints.
Data Visualization: Use Matplotlib or Plotly to provide visual insights for transaction patterns.


 
