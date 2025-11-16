import duckdb

# Point to your CSV files (edit these)
sku_master_path = "q-duckdb-sku-benchmark-sku_master.csv"
shipments_path  = "q-duckdb-sku-benchmark-shipments.csv"

con = duckdb.connect()

# Load the master table
con.execute(f"""
    CREATE TEMP TABLE sku_master AS
    SELECT * FROM read_csv_auto('{sku_master_path}');
""")

# Load the shipments table
con.execute(f"""
    CREATE TEMP TABLE shipments AS
    SELECT * FROM read_csv_auto('{shipments_path}');
""")

# Run the margin calculation
# Final Query: Compute gross margin by category
result = con.execute("""
    SELECT 
        category,
        SUM(units * unit_price) AS revenue,
        SUM(units * production_cost) AS cost,
        (SUM(units * unit_price) - SUM(units * production_cost)) / SUM(units * unit_price) AS gross_margin_ratio
    FROM shipments s
    JOIN sku_master m USING (sku_id)
    WHERE ship_date >= '2024-05-15'
    GROUP BY category
    ORDER BY gross_margin_ratio DESC;
""").fetchdf()

print("\n=== Gross Margin After 2024-05-15 ===")
print(result)

print("\nTop Category:", result.loc[0, "category"])
