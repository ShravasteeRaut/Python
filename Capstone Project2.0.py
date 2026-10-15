import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("penguins_size.csv")

print(df.head(10))

print(df.shape)

print(df.tail())

print(df.isnull().sum())

print(df.describe())

print(df.dtypes)

print(df.info())

print(df.describe(include='all'))

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.show()

df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False, figsize=(8,12))
plt.show()

print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

sns.countplot(data=df, x='sex')
plt.show()

sns.countplot(data=df, x='island')
plt.show()

sns.countplot(data=df, x='species')
plt.show()

sns.countplot(data=df, x='sex', hue='species')
plt.show()

sns.countplot(data=df, x='island', hue='species')
plt.show()

sns.countplot(data=df, x='species', hue='species')
plt.show()



body_mass = np.array(df['body_mass_g'].dropna())

print("Original array:")
print(body_mass)

print("Sort by body mass:")
print(np.sort(body_mass))



print('--- Pandas Series ---')

penguins = pd.Series(df['body_mass_g'])
print(penguins)



print('--- Pandas DataFrame ---')

penguins_df = pd.DataFrame(df)
print(penguins_df)



print('--- Accessing Rows ---')

print('Row 0:')
print(df.loc[0])

print()

print('Rows 2 and 3:')
print(df.loc[2:3])



print('First 5 rows:')
print(df.head())

print()

print('Last 3 rows:')
print(df.tail(3))



print('--- Cleaning Data ---')

print('Rows with missing values removed:')
clean_df = df.dropna()
print(clean_df.to_string())

print()

print('Missing values filled with 0:')
filled_df = df.fillna(0)
print(filled_df.to_string())



print("Species:", df['species'].unique())
print("Islands:", df['island'].unique())



plt.plot(clean_df['body_mass_g'])
plt.show()

plt.plot(clean_df['body_mass_g'])
plt.title('Penguin Body Mass')
plt.xlabel('Penguin Index')
plt.ylabel('Body Mass (grams)')
plt.grid(True)
plt.ylim(0, clean_df['body_mass_g'].max())
plt.show()

plt.plot(clean_df['body_mass_g'], color='blue', marker='o', linestyle='dashed', linewidth=2)
plt.title('Penguin Body Mass')
plt.xlabel('Penguin Index')
plt.ylabel('Body Mass (grams)')
plt.grid(True)
plt.ylim(0, clean_df['body_mass_g'].max())
plt.show()



plt.bar(df.species.value_counts().index, df.species.value_counts(), color='orange')
plt.title('Number of Penguins by Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()


sns.histplot(data=clean_df, x='body_mass_g', bins=20, color='steelblue')
plt.title('Distribution of Penguin Body Mass')
plt.xlabel('Body Mass (grams)')
plt.ylabel('Count')
plt.show()



sns.kdeplot(data=clean_df, x='flipper_length_mm', hue='species', fill=True)
plt.title('Flipper Length Shape by Species (KDE)')
plt.xlabel('Flipper Length (mm)')
plt.show()



sns.histplot(data=clean_df, x='flipper_length_mm', kde=True, color='coral')
plt.title('Flipper Length - Histogram with KDE Curve')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Count')
plt.show()



sns.scatterplot(data=clean_df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Flipper Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (grams)')
plt.show()



corr = clean_df.corr(numeric_only=True)

print("Correlation Table:")
print(corr)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Penguin Measurements')
plt.show()



sns.barplot(x='species', y='body_mass_g', hue='sex', data=clean_df)
plt.title('Average Body Mass per Species by Sex')
plt.xlabel('Species')
plt.ylabel('Average Body Mass (grams)')
plt.show()



sns.boxplot(x='species', y='body_mass_g', data=clean_df)
plt.title('Spread of Body Mass per Species')
plt.xlabel('Species')
plt.ylabel('Body Mass (grams)')
plt.show()



sns.stripplot(x='species', y='body_mass_g', data=clean_df, jitter=True)
plt.title('Every Body Mass per Species (Strip Plot)')
plt.xlabel('Species')
plt.ylabel('Body Mass (grams)')
plt.show()



sns.swarmplot(x='species', y='body_mass_g', data=clean_df)
plt.title('Every Body Mass per Species (Swarm Plot)')
plt.xlabel('Species')
plt.ylabel('Body Mass (grams)')
plt.show()



sns.jointplot(x='flipper_length_mm', y='body_mass_g', data=clean_df)
plt.suptitle('Flipper Length vs Body Mass', y=1.02)
plt.show()



sns.jointplot(x='flipper_length_mm', y='body_mass_g', data=clean_df, kind='kde')
plt.suptitle('Flipper Length vs Body Mass - KDE Joint Plot', y=1.02)
plt.show()



sns.pairplot(clean_df.select_dtypes(include=[np.number]))
plt.suptitle('Pair Plot - Penguin Measurements', y=1.02)
plt.show()



sns.pointplot(x='species', y='body_mass_g', hue='sex', data=clean_df)
plt.title('Average Body Mass per Species by Sex')
plt.xlabel('Species')
plt.ylabel('Average Body Mass (grams)')
plt.show()



sns.lmplot(x='flipper_length_mm', y='body_mass_g', data=clean_df)
plt.title('Flipper Length vs Body Mass - Trend Line')
plt.show()