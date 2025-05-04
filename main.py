import duckdb
import pyodbc
import pandas as pd

# Set up SQL Server connection
sql_conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your_server;"
    "DATABASE=your_db;"
    "UID=your_user;"
    "PWD=your_password"
)
sql_query = "SELECT TOP 100 * FROM your_table"

# Connect to SQL Server and fetch data
sql_conn = pyodbc.connect(sql_conn_str)
df = pd.read_sql(sql_query, sql_conn)
sql_conn.close()

print(f"Fetched {len(df)} rows from SQL Server.")

# Save to DuckDB
db_path = "sql_mirror.duckdb"
con = duckdb.connect(db_path)
con.register("df", df)
con.execute("CREATE OR REPLACE TABLE your_table AS SELECT * FROM df")

print("Saved to local DuckDB.")

# OPTIONAL: If MotherDuck is linked via token, this also syncs to cloud
# con = duckdb.connect('md:your_database') if you want full cloud usage
