import pandas as pd
from fredapi import Fred
import snowflake.connector
from datetime import datetime

# FRED API Key
FRED_API_KEY = “539250f7e29d67c391d3cec5022f3d67”


# Snowflake connection
SNOWFLAKE_CONFIG = {
    "account": "NGCPQFA-XCC30653",
    "user": "jmilanes1",
    "password": “Sevaelcaiman88!”,
    "warehouse": "PERSONAL_WH",
    "database": "DEV",
    "schema": "RAW",
    "role": "DEV_ROLE"
}

def load_series(cursor, fred, series_id, table_name):
    print(f"Loading {series_id}...")
    data = fred.get_series(series_id, observation_start="2000-01-01")
    df = pd.DataFrame({"DATE": data.index, "VALUE": data.values})
    df["SERIES_ID"] = series_id
    df["UPDATED_AT"] = datetime.now()
    df = df.dropna()
    
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO DEV.RAW.{table_name} (DATE, VALUE, SERIES_ID, UPDATED_AT)
            VALUES (%s, %s, %s, %s)
        """, (row["DATE"].date(), float(row["VALUE"]), row["SERIES_ID"], row["UPDATED_AT"]))
    
    print(f"Loaded {len(df)} rows into {table_name}")

def main():
    fred = Fred(api_key=FRED_API_KEY)
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = conn.cursor()
    
    load_series(cursor, fred, "GDP", "GDP")
    load_series(cursor, fred, "UNRATE", "UNEMPLOYMENT")
    load_series(cursor, fred, "CPIAUCSL", "INFLATION")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("All data loaded successfully!")

if __name__ == "__main__":
    main()
