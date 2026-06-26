import pandas as pd
import pandas as pd

df = pd.read_csv(
    r"C:\Users\phani\OneDrive\Desktop\Retail-Sales-Analytics\data\SampleSuperstore.csv",
    encoding="latin1"   # or "cp1252"
)

print(df.info())
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df['Order Date'] = pd.to_datetime(df['Order Date'])

df.columns = df.columns.str.replace(" ", "_")

df.to_csv("cleaned_sales.csv", index=False)

print("Data cleaned successfully")
