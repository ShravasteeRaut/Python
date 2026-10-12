import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("tips.csv")
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Totla Bill per Day By Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.barplot(x='day', hue='sex', data=df)
plt.title('Number of Diners per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
plt.title('Every Bill Amount per day (Strip Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount per day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.jointplot(x='total_bill',y='tip', data=df)
plt.title('Total Bill vs Tip', y=1.02)
plt.show()

sns.jointplot(x='total_bill',y='tip', data=df, kind='kde')
plt.suptitle('Total Bill vs Tip - KDE Joint Plot', y=1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair plot = Bill, Tip and Party Size', y=1.02)
plt.show()

sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.lmplot(x='total_bill',y='tip', data=df)
plt.title('Total Bill vs Tip - Trend Line')
plt.show()

