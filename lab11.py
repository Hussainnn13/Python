import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('cars.csv')
data_cleaned = data.dropna()
data_cleaned = pd.get_dummies(data_cleaned, drop_first=True)

X = data_cleaned.drop(columns=['ending_price'])
y = data_cleaned['ending_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison.head())
