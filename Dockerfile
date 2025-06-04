FROM python:3.11-slim-bookworm
WORKDIR /app
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
