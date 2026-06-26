import pandas as pd
df = pd.read_csv("../data/cleaned_sales.csv")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print(df.groupby("Category")["Sales"].sum())

print(df.groupby("Region")["Profit"].sum())