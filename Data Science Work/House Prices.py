import pandas as pd

# Load the data with the first column as a string (if necessary)
data = pd.read_csv('data.csv', dtype={'Index': str})  # Explicitly setting column 'Index' as string

# Check the percentage of missing values for each column
missing_data_percentage = data.isnull().mean() * 100
print("Missing data percentage for each column:\n", missing_data_percentage)

# Drop columns with more than 50% missing values
columns_to_drop = missing_data_percentage[missing_data_percentage > 50].index
data.drop(columns=columns_to_drop, inplace=True)

# Separate numeric and non-numeric columns for handling missing values
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
non_numeric_columns = data.select_dtypes(exclude=['float64', 'int64']).columns

# Fill missing numeric values with the mean of the respective columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# Fill missing non-numeric values with the mode (most frequent value)
for column in non_numeric_columns:
    mode_value = data[column].mode()[0]  # Get the most frequent value
    data[column] = data[column].fillna(mode_value)

# Verify if there are any remaining missing values
print("\nMissing values after imputation:\n", data.isnull().sum())
