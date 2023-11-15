import matplotlib.pyplot as plt
import pandas as pd


# plt.style.use('seaborn')  # to get seaborn scatter plot

# read the csv file to extract data
data = pd.read_csv('ganesh_ds.csv')
name = data['name']
weight = data['weight']
bp = data['bp']

# Define Scatter graph
plt.scatter(name, bp, s=weight, alpha=0.6, edgecolor='black', linewidth=1, vmin=0, vmax=200)

# Finding the maximum value
max_val = 0
max_idx = 0
for i in range(1, len(bp)):
    if bp[i] > max_val:
        max_val = bp[i]
        max_idx = i
print(max_idx, max_val)

# Annotate Highest
plt.annotate('Highest Value', xy=(max_idx, max_val), xytext=(max_idx - 0.5, max_val + 1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='bottom')

# Plot the Chart
plt.title('Health Chart')
plt.xlabel('Name')
plt.ylabel('Blood Pressure')
plt.tight_layout()
plt.show()
