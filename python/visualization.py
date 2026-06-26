csimport pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_sales.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
plt.savefig("../screenshots/monthly_sales.png")