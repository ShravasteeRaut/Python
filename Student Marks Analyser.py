import pandas as pd

print('--- PART 1: Pandas series ---')
marks = [92, 85, 78, 88, 74]
students = pd.Series(marks, index=['Aarav', 'Diya', 'Kabir', 'Anaya', 'Rohan'])
print(students)



print()
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Student': ['Aarav', 'Diya', 'Kabir', 'Anaya', 'Rohan'],
    'Maths': [92, 85, 78, 88, 74],
    'Science': [89, 91, 76, 84, 79],
    'English': [86, 88, 82, 90, 75]
    }
df = pd.DataFrame(data)
print(df)



print()
print('--- PART 3: Accessing Rows ---')
print('Row 0(top student):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])



print()
print('--- PART 4: Reading a CSV File ---')
full_df = pd.read_csv('studentmarks.csv')
print('First 5 rows (head):')
print(full_df.head())
print()
print('Last 3 rows (tail):')
print(full_df.tail(3))
print()
print('Dataset info:')
print(full_df.info())


print()
print('--- PART 5: Cleaning Data ---')
print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('Missing values filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())