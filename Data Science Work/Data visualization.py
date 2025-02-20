# Step 1: Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Step 2: Load a dataset (Seaborn has a built-in dataset called "tips")
data = sns.load_dataset("tips")

# Step 3: Create a bar plot to show the total bill by day
plt.figure(figsize=(8, 5))  # Set figure size
sns.barplot(x='day', y='total_bill', data=data, palette='viridis', hue='sex')  # Add hue for better grouping
plt.title('Total Bill by Day')  # Title of the plot
plt.xlabel('Day of the Week')  # X-axis label
plt.ylabel('Total Bill ($)')  # Y-axis label
plt.show()  # Show the plot

# Step 4: Create a scatter plot to explore the relationship between total_bill and tip
plt.figure(figsize=(8, 5))  # Set figure size
sns.scatterplot(x='total_bill', y='tip', data=data, color='blue')  # Create scatter plot
plt.title('Scatter Plot of Total Bill vs Tip')  # Title of the plot
plt.xlabel('Total Bill ($)')  # X-axis label
plt.ylabel('Tip ($)')  # Y-axis label
plt.show()  # Show the plot

# Step 5: Create a heatmap to show correlations between numerical features
# First, handle non-numeric columns by converting them to numeric or removing them
data['sex'] = data['sex'].map({'Male': 1, 'Female': 0})  # Convert 'sex' to numeric (1 for Male, 0 for Female)

# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Now compute the correlation matrix on the numeric columns
corr_matrix = numeric_data.corr()

# Create a heatmap to show correlations
plt.figure(figsize=(8, 5))  # Set figure size
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')  # Create the heatmap
plt.title('Correlation Heatmap')  # Title of the plot
plt.show()  # Show the plot
