import pandas as pd
import os

# Load Data
clients = pd.read_csv('data/clients.csv')
transactions = pd.read_csv('data/transactions.csv')
portfolios = pd.read_csv('data/portfolios.csv')

# --- Helper Functions ---
def check_missing_values(df, name):
    print(f"\n[Missing Values] {name}")
    print(df.isnull().sum())

def check_outliers(df, column, name):
    if column in df.columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]
        print(f"\n[Outliers] {name} - {column}")
        print(f"{len(outliers)} potential outliers found")
    else:
        print(f"Column '{column}' not found in {name}")

def check_date_format(df, column, name):
    if column in df.columns:
        try:
            pd.to_datetime(df[column])
            print(f"[Date Format] {name} - {column}: OK")
        except Exception as e:
            print(f"[Date Format] {name} - {column}: ERROR - {e}")

# --- Run Checks ---
check_missing_values(clients, "Clients")
check_missing_values(transactions, "Transactions")
check_missing_values(portfolios, "Portfolios")

check_outliers(transactions, 'amount', "Transactions")
check_outliers(portfolios, 'value', "Portfolios")

check_date_format(transactions, 'transaction_date', "Transactions")
check_date_format(clients, 'date_of_birth', "Clients")

print("\n✅ Data validation completed.")
