import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/transactions.csv")

# Normalize transaction_type to lowercase & strip spaces
df["transaction_type"] = df["transaction_type"].str.strip().str.lower()

# Filter for 'buy' transactions (instead of 'investment')
df_investments = df[df["transaction_type"] == "buy"]

# Convert date column to datetime
df_investments["date"] = pd.to_datetime(df_investments["date"], errors="coerce")

# Group by date and sum amounts
aum_daily = df_investments.groupby("date")["amount"].sum().reset_index()

# Export CSV for Tableau (optional)
aum_daily.to_csv("data/aum_trend.csv", index=False)
print("Exported data/aum_trend.csv")

# Plot
plt.figure(figsize=(12, 6))
plt.plot(aum_daily["date"], aum_daily["amount"], marker="o", linestyle="-", color="teal")
plt.title("📈 AUM (Assets Under Management) Over Time (Using Buy Transactions)")
plt.xlabel("Date")
plt.ylabel("Total Buy Amount ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
