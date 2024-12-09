import pandas as pd

# Load the dataset
data = pd.read_csv("cars.csv")

#first 5 rows will be displayed
print("First 5 rows of the dataset:")
print(data.head())

# information of dataset using info 
print("\nDataset Information:")
print(data.info())

# display stats
print("\nStatistical Summary:")
print(data.describe())

# check for empty cells
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

print("\nShape of the Dataset (Rows, Columns):")
print(data.shape)

#column names will be displayed
print("\nColumn Names:")
print(data.columns)

#checking unique column
print("\nUnique Values in 'fuel_type' Column:")
print(data['fuel_type'].unique())
