import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
from sklearn.ensemble import RandomForestRegressor

file_path = 'data10.csv'
data = pd.read_csv(file_path)

target = 'price'

numeric_data = data.select_dtypes(include=[np.number])

features = [col for col in numeric_data.columns if col != target]

raw_data = data.dropna(subset=[target])

non_numeric_cols = data.select_dtypes(include=[object]).columns
data_cleaned = data.drop(columns=non_numeric_cols)

imputer = KNNImputer(n_neighbors=5)
data_imputed = data_cleaned.copy()
data_imputed[features] = imputer.fit_transform(data_cleaned[features])

data_imputed = data_imputed.dropna(subset=[target])

scaler = StandardScaler()
data_imputed[features] = scaler.fit_transform(data_imputed[features])

X_imputed = data_imputed[features]
y_imputed = data_imputed[target]
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y_imputed, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae_after = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error After Cleaning: {mae_after:.2f}")

X_raw = raw_data[features]
y_raw = raw_data[target]
X_raw = X_raw.dropna()  # Drop rows with NaN values in features
y_raw = y_raw[X_raw.index]  # Align y_raw with the cleaned X_raw
X_raw_train, X_raw_test, y_raw_train, y_raw_test = train_test_split(X_raw, y_raw, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_raw_train, y_raw_train)
y_raw_pred = lr_model.predict(X_raw_test)
mae_before = mean_absolute_error(y_raw_test, y_raw_pred)
print(f"Mean Absolute Error Before Cleaning: {mae_before:.2f}")

improvement = mae_before - mae_after
print(f"Improvement in Accuracy (MAE): {improvement:.2f}")

print("\nBasic Information:")
print(data.info())

print("\nMissing Values After Cleaning:")
print(data.isnull().sum())

plt.figure(figsize=(12, 8))
correlation_matrix = data_imputed.select_dtypes(include=[np.number]).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data_imputed['price'], kde=True, bins=50)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

cleaned_file_path = 'cleaned_data.csv'
data_imputed.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")
