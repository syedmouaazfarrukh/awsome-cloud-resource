import pandas as pd
from sqlalchemy import create_engine

#  ----------- EXTRACT -----------------
# Load Excel files into pandas DataFrames
file1_path = 'D://OneDrive - Octopus Digital//Desktop//HandsOnClouds//hands-on-clouds//use-cases//containers//containerize-etl-jobs//etl-order//olist_order_items_dataset.csv'
file2_path = 'D://OneDrive - Octopus Digital//Desktop//HandsOnClouds//hands-on-clouds//use-cases//containers//containerize-etl-jobs//etl-order//olist_order_payments_dataset.csv'

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)


#  ----------- TRANSFORM -----------------

merged_df = pd.merge(df1, df2, on='order_id', how='inner')
print(merged_df)

#  ----------- LOAD -----------------

# Replace the placeholders with your actual RDS information
username = 'your-username'
password = 'password'
host = 'endpoint'
port = 'port'  # Default is usually 3306 for MySQL
database = 'your-database-name'

# Construct the connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
# print(engine)

table_name = 'merged_on_orderID'
load = merged_df.to_sql(table_name, con=engine, index=False, if_exists='append')
print(f'Data in "{table_name}" appended successfully.')