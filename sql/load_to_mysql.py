import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/cleaned_sales.csv")


engine = create_engine(
    "mysql+pymysql://root:root123@localhost/retail_sales"
)

df.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")