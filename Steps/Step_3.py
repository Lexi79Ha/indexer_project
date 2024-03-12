# The attributes with the json file are pulled and isolated using pandas
# The attributes are then assigned to columns
# The script is then connected to a postgres database
# Tablename is determined by the last 10 characters of the type attribute, this ensures that tables will be organized by transaction type
# The nested sql queries are designed to first search the database for if a similar table name exists in the database
# If a table under that name already exists the data from each attribute will be loaded to its corresponded column
# If a table does not exist then a table will be generated, and then the data will be inserted into the table

# %%
import psycopg2

DB_NAME = 'blockchain'
DB_USER = 'postgres'
DB_PASSWORD = 'auth2020'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Create a PostgreSQL connection
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
# This section of code uses json and pandas to clean json file and get it ready to sort it into a tabular format to prepare for postgres
import pandas as pd
import json
# Specify the file path
file_path = r'C:\Users\lmhmo\indexer\Decrypted_files\5845389_1.json'

with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Slight modifications made to make data postgres friendly
def replace_empty_strings(item):
    return "N/A" if item == "null" else item

for field in ["sender", "receiver", "memo"]:
    json_data["tx"]["body"]["messages"][0][field] = replace_empty_strings(json_data["tx"]["body"]["messages"][0][field])
# This section of code calls the paths of all the attributes needs for the postgres table
df_messages = pd.json_normalize(json_data["tx"]["body"]["messages"])
df_auth_info = pd.json_normalize(json_data["tx"]["auth_info"]["signer_infos"])
df_fee_info = pd.json_normalize(json_data["tx"]["auth_info"]["fee"]["amount"])
df_sig_info = pd.DataFrame({"signatures": json_data["tx"]["signatures"]})
df_gas_info = pd.DataFrame({"gas_limit": [json_data["tx"]["auth_info"]["fee"]["gas_limit"]]})
df_payer_info = pd.DataFrame({"payer": [json_data["tx"]["auth_info"]["fee"]["payer"]]})
df_granter_info = pd.DataFrame({"granter": [json_data["tx"]["auth_info"]["fee"]["granter"]]})
df_tip_info = pd.DataFrame({"tip": [json_data["tx"]["auth_info"]["tip"]]})

# Combine dataframes
df_combined = pd.concat(
    [df_messages, df_auth_info, df_fee_info, df_sig_info, df_gas_info, df_payer_info, df_granter_info, df_tip_info],
    axis=1)

# Display the combined dataframe
print(df_combined)
# %%
# Creates tabular format
column_names = list(df_combined.columns)
# Slight modifications that needed to be made to prepare for postgres
def clean_column_name(col): # Special symbols can not be inside of column names
    return col.replace("@", "").replace(" ", "_").replace('.', '')

column_names_cleaned = [clean_column_name(col) for col in column_names]

message = json_data["tx"]["body"]["messages"][0]
table_name = message["@type"].split(".")[-1][-10:]
table_name = table_name.lower()  # This has to be specified for check_table_query to work

# %%
# Create a cursor
cur = conn.cursor()

# Check if the table already exists
check_table_query = f"""
    SELECT EXISTS (
        SELECT 1
        FROM pg_tables
        WHERE schemaname = 'public' AND tablename = '{table_name}'
    );
"""

cur.execute(check_table_query)
table_exists = cur.fetchone()[0]  # Fetch the result of the query

if table_exists:
    print(f"Table '{table_name}' already exists. Data will be appended to the existing table.")
else:
    print(f"Table '{table_name}' does not exist. Creating a new table...")

# %%

if not table_exists:
    # Create the table with dynamic column names (matching cleaned attributes)
    create_table_query = f"""
        CREATE TABLE {table_name} (
            id SERIAL PRIMARY KEY,
            {', '.join(f"{column_names_cleaned[i]} VARCHAR(255)" for i in range(len(column_names)))}, block INTEGER NOT NULL
        );
    """
    cur.execute(create_table_query)
    print(f"Table '{table_name}' created successfully.")
else:
    print(f"Table '{table_name}' already exists. Data will be appended to the existing table.")

# Insert data into the table
for _, row in df_combined.iterrows():
    # Assuming you have already defined the variable block_number
    # Modify the INSERT query to include the block number
    insert_query = f"""
        INSERT INTO {table_name} ({', '.join(column_names_cleaned)}, block)
        VALUES ({', '.join(f"'{row.iloc[i]}'" for i in range(len(column_names)))}, {block});
    """
cur.execute(insert_query)

# Commit changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

# Display the resulting DataFrame
print(df_combined)
