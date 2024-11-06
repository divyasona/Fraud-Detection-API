from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Load data
data = pd.read_csv("transactions.csv")

# Define data model for POST requests
class Transaction(BaseModel):
    transaction_id: int
    customer_id: int
    transaction_date: str
    amount: float
    transaction_type: str
    is_fraud: int
# main.py (continued)

def detect_fraud(transaction):
    # Simple fraud detection based on transaction amount
    return transaction['amount'] > 5000

@app.get("/transactions")
def get_transactions():
    """Retrieve all transactions"""
    return data.to_dict(orient="records")

@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int):
    """Retrieve a specific transaction"""
    transaction = data[data['transaction_id'] == transaction_id]
    if transaction.empty:
        return {"error": "Transaction not found"}
    return transaction.to_dict(orient="records")[0]

@app.get("/fraudulent-transactions")
def get_fraudulent_transactions():
    """Get transactions flagged as fraud"""
    frauds = data[data.apply(detect_fraud, axis=1)]
    return frauds.to_dict(orient="records")
# main.py (continued)

@app.get("/financial-summary")
def financial_summary():
    """Provide a summary of total debit and credit transactions"""
    summary = data.groupby("transaction_type")['amount'].sum()
    return summary.to_dict()

