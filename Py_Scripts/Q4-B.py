import matplotlib.pyplot as plt
import pandas as pd

# Load CSV File - Credit Card Complaint
csv_file = "credit_card_complaints.csv"

# Define Column
columns = ["issue", "state"]
df_csv = pd.read_csv(csv_file, usecols=columns)

df_issue_count = df_csv.groupby(['state'])['issue'].count()
df_issue_count.plot(kind='bar')

# Add Value as label for each bar
for idx, val in enumerate(df_issue_count):
    plt.text(idx, val + 100, val, color='red')
    print(idx, val)

# Finding the maximum value
max_val = df_issue_count[0]
max_idx = 0
for i in range(1, len(df_issue_count)):
    if df_issue_count[i] > max_val:
        max_val = df_issue_count[i]
        max_idx = i
print(max_idx, max_val)

# Finding the lowest value
low_val = df_issue_count[0]
low_idx = 0
for i in range(1, len(df_issue_count)):
    if df_issue_count[i] < low_val:
        low_val = df_issue_count[i]
        low_idx = i
print(low_idx, low_val)

# Annotate Highest
plt.annotate('Highest Value', xy=(max_idx, max_val), xytext=(max_idx - 0.5, max_val + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='bottom')

# Annotate Lowest
plt.annotate('Lowest Value', xy=(low_idx, low_val), xytext=(low_idx - 0.5, low_val + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='center')


# Legend
plt.legend()

# Plot the Chart
plt.xlabel('State')
plt.ylabel('Count')
plt.title('Issue Vs State')
plt.show()
