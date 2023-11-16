import matplotlib.pyplot as plt

# Data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [7, 8, 2, 4, 7, 11, 15, 7, 10, 8, 4, 2, 7]
# s = [100, 8, 2, 4, 7, 11, 15, 7, 10, 8, 4, 2, 7]

# Using default value since not provided in Q2
size = 10
color = "red"

# Plot the Chart
plt.scatter(x, y, s=size, c=color, vmin=0, vmax=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Task2')

# Display Chart
plt.show()
