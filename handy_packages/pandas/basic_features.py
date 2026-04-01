import pandas as pd
import numpy as np

# ---------- 1. Creating Series & DataFrame ----------
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series:\n", s)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ---------- 2. Reading / Writing CSV ----------
# For demo purposes, we create a CSV in memory
df.to_csv("demo.csv", index=False)
df_loaded = pd.read_csv("demo.csv")
print("\nLoaded CSV:\n", df_loaded)

# ---------- 3. Indexing & selection ----------
print("\nSelect column 'Name':\n", df['Name'])
print("\nSelect first 2 rows:\n", df.iloc[:2])
print("\nSelect rows where Age > 30:\n", df[df['Age'] > 30])

# ---------- 4. Adding / modifying columns ----------
df['Age_plus_5'] = df['Age'] + 5
df['High_Earner'] = df['Salary'] > 65000
print("\nModified DataFrame:\n", df)

# ---------- 5. Aggregations ----------
print("\nMean Salary:", df['Salary'].mean())
print("Max Age:", df['Age'].max())
print("Sum of Age:", df['Age'].sum())

# ---------- 6. GroupBy ----------
grouped = df.groupby('High_Earner')['Salary'].mean()
print("\nAverage Salary by High_Earner:\n", grouped)

# ---------- 7. Handling missing data ----------
df_missing = df.copy()
df_missing.loc[1, 'Salary'] = np.nan
print("\nDataFrame with missing value:\n", df_missing)
print("Fill missing Salary with 0:\n", df_missing['Salary'].fillna(0))

# ---------- 8. Sorting ----------
print("\nSort by Age descending:\n", df.sort_values('Age', ascending=False))

# ---------- 9. Concatenation / merging ----------
df2 = pd.DataFrame({
    'Name': ['Eve', 'Frank'],
    'Age': [28, 33],
    'Salary': [55000, 62000]
})
concat_df = pd.concat([df, df2], ignore_index=True)
print("\nConcatenated DataFrame:\n", concat_df)