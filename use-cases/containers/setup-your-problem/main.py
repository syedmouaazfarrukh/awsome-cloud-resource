import pandas as pd
from sqlalchemy import create_engine
import boto3

#  ----------- EXTRACT -----------------
# Load Excel files into pandas DataFrames
file1_path = 'D://OneDrive - Octopus Digital//Desktop//HandsOnClouds//hands-on-clouds//use-cases//containers//dataset//olist_order_payments_dataset.csv'
file2_path = 'D://OneDrive - Octopus Digital//Desktop//HandsOnClouds//hands-on-clouds//use-cases//containers//dataset//olist_order_items_dataset.csv'

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
# print(df1,df2)


#  ----------- TRANSFORM -----------------

merged_df = pd.merge(df1, df2, on='order_id', how='inner')
# print(merged_df)

# Additional transformations as needed

# 1. **Selecting/Filtering Data:**
#    - `df[col]` or `df[[col1, col2]]`: Select specific columns.
#    - `df.loc[row_indexer, col_indexer]`: Access a group of rows and columns by labels or a boolean array.
#    - `df.iloc[row_indexer, col_indexer]`: Access a group of rows and columns by integer index.

# 2. **Cleaning Data:**
#    - `df.drop(labels, axis)`: Remove rows or columns by specifying labels.
#    - `df.fillna(value)`: Replace missing values with a specified value.
#    - `df.drop_duplicates()`: Remove duplicate rows.
#    - `df.rename(columns={'old_name': 'new_name'})`: Rename columns.

# 3. **Merging/Joining DataFrames:**
#    - `pd.concat([df1, df2], axis)`: Concatenate two DataFrames along rows or columns.
#    - `pd.merge(df1, df2, on='common_column', how='inner')`: Merge DataFrames based on a common column.

# 4. **Aggregation/Grouping:**
#    - `df.groupby('column').mean()`: Compute mean for each group.
#    - `df.groupby('column').agg({'column1': 'sum', 'column2': 'count'})`: Aggregate using custom functions.

# 5. **Applying Functions:**
#    - `df.apply(func)`: Apply a function along the axis of the DataFrame.
#    - `df.applymap(func)`: Apply a function to a DataFrame element-wise.

# 6. **Reshaping/Transforming Data:**
#    - `df.pivot(index, columns, values)`: Pivot a DataFrame based on column values.
#    - `pd.melt(df, id_vars, value_vars)`: Unpivot a DataFrame.
#    - `df.stack()` and `df.unstack()`: Reshape DataFrame from long to wide and vice versa.

# 7. **Working with Strings:**
#    - `df['column'].str.upper()`: Convert strings to uppercase.
#    - `df['column'].str.contains('substring')`: Check for substring presence.

# 8. **Date and Time Operations:**
#    - `pd.to_datetime(df['date_column'])`: Convert a column to datetime format.
#    - `df['date_column'].dt.month`: Extract month from datetime column.
#    - `df['date_column'].dt.strftime('%Y-%m-%d')`: Format datetime as string.

# 9. **Handling Categorical Data:**
#    - `pd.get_dummies(df['categorical_column'])`: One-hot encode categorical variables.
#    - `df['categorical_column'].astype('category')`: Convert a column to a categorical type.

# 10. **Sorting Data:**
#     - `df.sort_values(by='column')`: Sort DataFrame by one or more columns.
#     - `df.sort_index()`: Sort DataFrame by index.

# These are just some of the key functionalities in pandas. Depending on your specific transformation needs, you might use a combination of these operations to clean, reshape, and manipulate your data effectively.



#  ----------- LOAD -----------------


# Replace 'your_connection_string' with your RDS connection string
# connection_string = "etlb.c3g2sa6aqpxp.eu-north-1.rds.amazonaws.com"
# engine = create_engine(connection_string)
# print(engine)




# Replace the placeholders with your actual RDS information
username = 'admin'
password = 'BgYlwxiBBmYEWf8LgylG'
host = 'etlb.c3g2sa6aqpxp.eu-north-1.rds.amazonaws.com'
port = '3306'  # Default is usually 3306 for MySQL
database = 'ETLB_AWS'

# Construct the connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
print(engine)

table_name = 'merged_on_orderID'
load = merged_df.to_sql(table_name, con=engine, index=False, if_exists='replace')
print(f'Table "{table_name}" created successfully.')
