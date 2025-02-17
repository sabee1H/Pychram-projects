import requests
import pandas as pd

API_KEY = "0768077f341df1fa35bd4c07decf9faa"  # Replace with your API key
CITY = "Karachi"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)
data = response.json()

# Extract relevant weather details
weather_list = data['list']
temperature_data = []

for entry in weather_list:
    date = entry['dt_txt']
    temp = entry['main']['temp']
    temperature_data.append([date, temp])
# Convert to DataFrame
df = pd.DataFrame(temperature_data, columns=["Date", "Temperature"])
df.to_csv("karachi_weather.csv", index=False)  # Save data for later use
print("Weather data fetched and saved successfully!")
# Load data
df = pd.read_csv("karachi_weather.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values(by="Date")

# Remove missing values if any
df.dropna(inplace=True)

# Print first few rows
print(df.head())
df["Prev_Temp"] = df["Temperature"].shift(1)  # Shift temp by 1 row
df.dropna(inplace=True)  # Drop first row since it has no previous temp

print(df.head())
from sklearn.model_selection import train_test_split
X = df[["Prev_Temp"]]  # Features
y = df["Temperature"]   # Target (what we predict)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")
from sklearn.linear_model import LinearRegression
# Create model and train
model = LinearRegression()
model.fit(X_train, y_train)
# Predict on test data
y_pred = model.predict(X_test)
print("Model training complete!")
last_temp = df["Temperature"].iloc[-1]
# Predict next day’s temperature
predicted_temp = model.predict([[last_temp]])
print(f"Predicted Temperature for Tomorrow: {predicted_temp[0]:.2f}°C")

