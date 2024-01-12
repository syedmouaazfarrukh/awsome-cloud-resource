FROM python:3.8-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libmariadb-dev gcc pkg-config

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY etljob.py  .
COPY olist_customers_dataset.csv  .
CMD ["python3", "etljob.py"]
