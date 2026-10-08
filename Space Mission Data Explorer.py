import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("planets.csv")
df = df.dropna()

print("First 5 rows: ")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print("Discovery Methods:", df['method'].unique())
print("Discovery Years:", sorted(df['year'].unique()))
print()

sns.histplot(data=df, x='distance', bins=20, color='steelblue', log_scale=True)
plt.title('Distribution of Planet Distances (Log Scale)')
plt.xlabel('Distance (light years)')
plt.ylabel('Count')
plt.show()

top_methods = df['method'].value_counts().nlargest(3).index
df_filtered = df[df['method'].isin(top_methods)]

sns.kdeplot(data=df_filtered, x='orbital_period', hue='method', fill=True, log_scale=True)
plt.title('Orbital Period Shape by Method (KDE - Log Scale)')
plt.xlabel('Orbital Period (days)')
plt.show()

sns.histplot(data=df, x='mass', kde=True, color='coral', log_scale=True)
plt.title('Planet Mass - Histogram with KDE Curve (Log Scale)')
plt.xlabel('Mass (relative to Jupiter)')
plt.ylabel('Count')
plt.show()

sns.scatterplot(data=df_filtered, x='distance', y='orbital_period', hue='method')
plt.xscale('log')
plt.yscale('log')
plt.title('Distance vs Orbital Period by Discovery Method')
plt.xlabel('Distance (light years)')
plt.ylabel('Orbital Period (days)')
plt.show()

corr = df.corr(numeric_only=True)
print("Correlation Table:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Planet Attributes')
plt.show()

