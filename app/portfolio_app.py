import pandas as pd
import streamlit as st
from pypfopt import EfficientFrontier, risk_models, expected_returns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Portfolio Optimization & RBC Dashboard", layout="wide")
st.title("📊 Portfolio Optimization Tool & RBC Wealth Insights Dashboard")

# File uploader to optionally upload portfolio CSV
uploaded_file = st.file_uploader("Upload your portfolio CSV with historical prices", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0, parse_dates=True)
    st.write("✅ Uploaded Portfolio Data (showing first 5 rows):")
    st.dataframe(df.head())

    try:
        # Calculate expected returns and sample covariance matrix
        mu = expected_returns.mean_historical_return(df)
        S = risk_models.sample_cov(df)

        # Optimize for max Sharpe ratio
        ef = EfficientFrontier(mu, S)
        weights = ef.max_sharpe()
        cleaned_weights = ef.clean_weights()

        st.subheader("📈 Optimized Portfolio Weights")
        st.write(cleaned_weights)

        # Display pie chart of weights
        fig, ax = plt.subplots()
        ax.pie(cleaned_weights.values(), labels=cleaned_weights.keys(), autopct='%1.1f%%')
        ax.set_title("Portfolio Weights Distribution")
        st.pyplot(fig)

        # Show portfolio performance metrics
        ret, vol, sharpe = ef.portfolio_performance(verbose=False)
        st.write(f"**Expected annual return:** {ret:.2%}")
        st.write(f"**Annual volatility:** {vol:.2%}")
        st.write(f"**Sharpe Ratio:** {sharpe:.2f}")

    except Exception as e:
        st.error(f"Error optimizing portfolio: {e}")

else:
    st.info("Upload a CSV file with historical prices indexed by date to get started.")

    # Show default clients and transactions data if no upload
    try:
        clients_df = pd.read_csv("clients.csv")
        transactions_df = pd.read_csv("transactions.csv")

        st.subheader("Clients Overview")
        st.dataframe(clients_df.head())

        st.subheader("Transactions Overview")
        st.dataframe(transactions_df.head())
    except FileNotFoundError:
        st.warning("clients.csv or transactions.csv not found. Make sure these files exist in the app directory.")
