import pandas as pd
import sqlite3

df = pd.read_csv("stage_viewership.csv")

conn = sqlite3.connect("stage_analytics.db")

df.to_sql(
    "viewership",conn,index=False,if_exists="replace"
)

conn.close()
print("✅ Data loaded into stage_analytics.db (table: viewership)")
