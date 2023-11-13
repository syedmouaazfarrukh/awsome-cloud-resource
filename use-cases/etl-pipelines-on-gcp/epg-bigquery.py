# Import the necessary libraries
from google.cloud import bigquery

# Create a BigQuery client
bigquery_client = bigquery.Client()

# Create a dataset
dataset = bigquery.Dataset('retail_data', bigquery_client)

# Create a table
table = bigquery.Table('transactions', dataset)

# Load data into the table
bigquery_client.load_table_from_uri(
    source_uris=['gs://your-bucket/data.csv'],
    destination=table,
    job_config=bigquery.LoadJobConfig()
)

# Query the table
query = 'SELECT * FROM retail_data.transactions'
query_job = bigquery_client.query(query)

# Process the query results
for row in query_job:
    print(row)
