import pandas as pd
import matplotlib.pyplot as plt

clients = pd.read_csv("data/clients.csv")
portfolios = pd.read_csv("data/portfolios.csv")

# Merge on client_id to get location in portfolio data
merged = portfolios.merge(clients[["client_id", "location"]], on="client_id", how="left")

# Group by location and asset_class, sum value
grouped = merged.groupby(["location", "asset_class"])["value"].sum().unstack(fill_value=0)

# Export to CSV for Tableau
grouped.reset_index().to_csv("data/product_adoption_by_location.csv", index=False)
print("✅ Exported product_adoption_by_location.csv for Tableau")

# Plot stacked bar chart
grouped.plot(kind="bar", stacked=True, figsize=(12, 7), colormap="tab20")

plt.title("Product Adoption by Location")
plt.xlabel("Location")
plt.ylabel("Total Asset Value ($)")
plt.legend(title="Asset Class", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
