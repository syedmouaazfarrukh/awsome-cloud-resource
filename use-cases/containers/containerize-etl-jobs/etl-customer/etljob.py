import pandas as pd
from sqlalchemy import create_engine

#  ----------- EXTRACT -----------------
# Load Excel files into pandas DataFrames
file1_path = 'your-dataset-directory'

df1 = pd.read_csv(file1_path)

#  ----------- TRANSFORM -----------------

col_df = df1["column-name"]
print(col_df)

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

table_name = 'your-table-name'
load = col_df.to_sql(table_name, con=engine, index=False, if_exists='append')
print(f'Data in "{table_name}" created/appended successfully.')