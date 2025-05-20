import pandas as pd

# Load your wide-format CSV
df = pd.read_csv("data/product_adoption_by_location.csv")

# Reshape from wide to long format
df_long = df.melt(id_vars=["location"], var_name="asset_class", value_name="value")

# Save the reshaped data
df_long.to_csv("dashboards/product_adoption_long.csv", index=False)

print("✅ Reshaped product adoption data saved as dashboards/product_adoption_long.csv")
