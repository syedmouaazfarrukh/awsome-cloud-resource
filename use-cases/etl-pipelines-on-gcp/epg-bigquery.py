# Import the necessary libraries
from google.cloud import bigquery

bigquery_client = bigquery.Client()
dataset = bigquery.Dataset('retail_id', bigquery_client)
table = bigquery.Table('test-retail_id', dataset)

# # Load data into the table
# - IN CASE YOU WANT TO LOAD DATA FROM GCS

# bigquery_client.load_table_from_uri(
#     source_uris=['gs://your-bucket/data.csv'],
#     destination=table,
#     job_config=bigquery.LoadJobConfig()
# )

# Query the table
query = 'INSERT INTO retail_id.test-retail_id (si_id) VALUES (1);'
query_job = bigquery_client.query(query)

# Query the table
query = 'SELECT * FROM retail_id.test-retail_id'
query_job = bigquery_client.query(query)

# Process the query results
for row in query_job:
    print(row)
