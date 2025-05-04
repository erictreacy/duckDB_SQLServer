# SQL Server to MotherDuck Sync (Proof of Concept)

This repo demonstrates how to:
- Connect to Microsoft SQL Server using `pyodbc`
- Query data into a Pandas DataFrame
- Save that data into a DuckDB database file
- Optionally sync that `.duckdb` file to the cloud with [MotherDuck](https://motherduck.com)

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Update the main.py with your SQL Server credentials and table name. 

3. Run:

```bash
python main.py
```

4. Open sql_mirror.duckdb in the [DuckDB CLI](https://duckdb.org/docs/duckdb_cli) or in your local MotherDuck instance.

# Optional: Use MotherDuck Cloud

If you have a MotherDuck, you can: 

```python
duckdb.connect('md:your_database')
```

