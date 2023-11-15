# Task 4 - Sub Product Vs Count

import matplotlib.pyplot as plt
import pandas as pd

# Lets load the CSV
csv_file = "C:/Users/USER/Documents/PERSONAL/MBB-KL/PYTHON/bank_account_or_service_complaints.csv"
columns = ["sub_product", "issue"]
df_csv = pd.read_csv(csv_file, usecols=columns)
df_sub_product = df_csv.groupby(['sub_product'])['sub_product'].count()
df_issue = df_csv.groupby(['issue'])['issue'].count()
plt.plot(df_sub_product)

plt.show()
