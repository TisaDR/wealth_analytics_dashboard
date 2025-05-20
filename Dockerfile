# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and CSV files
COPY app/portfolio_app.py .
COPY data/clients.csv .
COPY data/transactions.csv .

# Expose the port Streamlit runs on
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "portfolio_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
