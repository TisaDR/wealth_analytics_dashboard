import pandas as pd
import matplotlib.pyplot as plt

clients = pd.read_csv("data/clients.csv")
portfolios = pd.read_csv("data/portfolios.csv")

# Aggregate portfolio value per client using the correct column name 'value'
portfolio_sum = portfolios.groupby("client_id")["value"].sum().reset_index()

# Join with clients on client_id
client_portfolio = clients.merge(portfolio_sum, on="client_id", how="inner")

plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    client_portfolio["risk_score"],
    client_portfolio["value"],   # note: 'value' column here is the total portfolio value
    s=client_portfolio["income"] / 1000,  # scale size for better visibility
    c=client_portfolio["age"],
    cmap="viridis",
    alpha=0.7,
    edgecolors="w",
    linewidth=0.5
)

plt.colorbar(scatter, label="Age")
plt.title("Client Risk Score vs Total Portfolio Value")
plt.xlabel("Risk Score")
plt.ylabel("Total Portfolio Value ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
client_portfolio.to_csv("data/client_risk_vs_portfolio_value.csv", index=False)
print("✅ Exported client_risk_vs_portfolio_value.csv for Tableau")
