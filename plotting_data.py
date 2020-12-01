import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

#here we choose the style for the plot 
matplotlib.style.use('ggplot')

# Import data
df = pd.read_csv("population_data.csv")

#plotting total_cases
df.iloc[5658:5874].plot(x='Year', y='Total population', figsize=(10,5))
plt.title('Brazil Population Growth')
plt.show()

