import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read Dataset
data = pd.read_csv(r"D:\Indian_Traffic_Violations.csv.xls")

# Display complete dataset
print(data)

# %%
# Display first 5 rows
print(data.head())

# %%
# Display last 5 rows
print(data.tail())

# %%
# Select required columns
df = data[['Violation_ID',
           'Violation_Type',
           'Fine_Amount',
           'Location']]

df.columns = ['ID', 'Type', 'Fine', 'Place']

print(df)

# %%
# Display Head and Tail
print(data.head())
print(data.tail())

# %%
# Sort by Violation Type
today = df.sort_values(by='Type')

print(today)

# %%
# Display column names
print(data.columns)

# %%
# Convert Fine Amount to numeric
data['Fine_Amount'] = pd.to_numeric(data['Fine_Amount'], errors='coerce')

# Count top 10 violation types
top_violation = (
    data.groupby('Violation_Type')['Fine_Amount']
    .count()
    .reset_index(name='Count')
)

top_violation = top_violation.sort_values(
    by='Count',
    ascending=False
).head(10)

# %%
# Bar Plot
plt.figure(figsize=(12,6))

sns.barplot(
    x='Violation_Type',
    y='Count',
    data=top_violation
)

plt.title("Top 10 Traffic Violation Types")
plt.xlabel("Violation Type")
plt.ylabel("Number of Violations")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
