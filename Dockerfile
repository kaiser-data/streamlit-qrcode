# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY qr_generator.py .
COPY .streamlit/config.toml .streamlit/

# Expose Streamlit port
EXPOSE 7860

# Set environment variable for Streamlit
ENV STREAMLIT_SERVER_PORT=7860
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run the app
CMD ["streamlit", "run", "qr_generator.py", "--server.port=7860", "--server.address=0.0.0.0"]
