import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Sales': [500, 600, 750, 900, 1000],
    'Expenses': [420, 520, 600, 750, 800]
}
# Creating a DataFrame
df = pd.DataFrame(data)

# Plotting using Pandas and Matplotlib
df.plot(x='Year', y=['Sales', 'Expenses'], kind='line', marker='o')
plt.title('Sales and Expenses Over Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.grid(True)
plt.legend()
plt.show()
