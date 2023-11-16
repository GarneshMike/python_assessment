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
max_val = bp[0]
max_idx = 0
for i in range(1, len(bp)):
    if bp[i] > max_val:
        max_val = bp[i]
        max_idx = i
print(max_idx, max_val)

# Finding the lowest value
low_val = bp[0]
low_idx = 0
for i in range(1, len(bp)):
    if bp[i] < low_val:
        low_val = bp[i]
        low_idx = i
print(low_idx, low_val)


# Compute Summary in Center of the Screen
total_x = len(bp)
range_value = max_val - low_val

summary_value = f"""
Highest Value = {max_val} 
Lowest Value = {low_val}
Data Range (Spread of data) = {range_value}
Total X (Unique) = {total_x}
"""

plt.text(total_x / 2, max_val - 30, summary_value, size=15, rotation=0,
         ha="center", va="center", color="white",
         bbox=dict(boxstyle="round", color="green")
         )


# Annotate Highest
plt.annotate('Highest Value', xy=(max_idx, max_val), xytext=(max_idx - 0.5, max_val + 1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='bottom')

# Annotate Lowest
plt.annotate('Lowest Value', xy=(low_idx, low_val), xytext=(low_idx - 0.5, low_val + 1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='center')


# Plot the Chart
plt.title('Health Chart')
plt.xlabel('Name')
plt.ylabel('Blood Pressure')
plt.tight_layout()
plt.show()
