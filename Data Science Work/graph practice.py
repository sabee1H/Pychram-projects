import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Revenue': [100, 120, 140, 160, 180]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting a bar graph
df.plot(x='Year', y='Revenue', kind='bar', color='skyblue')
plt.title('Revenue by Year')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.show()
