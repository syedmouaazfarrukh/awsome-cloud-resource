FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY etljob.py  .
COPY olist_order_items_dataset.csv  .
COPY olist_order_payments_dataset.csv  .

CMD ["python", "etljob.py"]
