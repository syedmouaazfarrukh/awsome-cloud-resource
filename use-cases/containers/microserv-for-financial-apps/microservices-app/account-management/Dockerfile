FROM python:3.8-slim

# Install system dependencies
RUN apt-get update 

WORKDIR /app

# COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY account_management_service.py  .
CMD ["python3", "account_management_service.py"]
