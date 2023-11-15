import matplotlib.pyplot as plt

# Data
x = ['Apple', 'Oranges', 'Watermelon', 'Pear']
y = [10, 22, 1, 5]

# Plot the Chart
plt.bar(x, y, width=1, edgecolor='white', align='center', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Task3')

# Display Chart
plt.show()
