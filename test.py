import pyarrow.parquet as pq
table = pq.read_table("records.parquet")
# Optionally convert to Pandas DataFrame
df = table.to_pandas()
print(df)