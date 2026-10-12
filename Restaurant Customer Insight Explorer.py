import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tips2.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="day", y="total_bill", errorbar=None)
plt.title("Average Customer Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill ($)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="day")
plt.title("Customer Count by Day")
plt.xlabel("Day")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Spread of Customer Bills by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.stripplot(data=df, x="day", y="total_bill", jitter=True)
plt.title("Individual Customer Bills by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.swarmplot(data=df, x="day", y="total_bill", size=4)
plt.title("Customer Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

sns.jointplot(data=df, x="total_bill", y="tip", kind="scatter", height=7)
plt.suptitle("Relationship Between Total Bill and Tip", y=1.02)
plt.show()

sns.pairplot(df, vars=["total_bill", "tip", "size"], hue="sex")
plt.suptitle("Pair Plot of Bills, Tips, and Party Size", y=1.02)
plt.show()

plt.figure(figsize=(8, 5))
sns.pointplot(data=df, x="day", y="tip", hue="sex", errorbar=None)
plt.title("Average Tip by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Average Tip ($)")
plt.tight_layout()
plt.show()

sns.lmplot(data=df, x="total_bill", y="tip", height=5, aspect=1.4)
plt.title("Trend Between Total Bill and Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

print("CUSTOMER INSIGHTS")
print("-----------------")
print("Number of records:", len(df))
print("Average total bill: $", round(df["total_bill"].mean(), 2))
print("Average tip: $", round(df["tip"].mean(), 2))
print("\\nAverage bill by day:")
print(df.groupby("day")["total_bill"].mean().round(2))
print("\\nAverage tip by gender:")
print(df.groupby("sex")["tip"].mean().round(2))
