import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read Dataset
data = pd.read_csv(r"D:\india_cancer_patients_2022_2025.csv.xls")

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
df = data[['Patient_ID',
           'Age',
           'Gender',
           'State']]

df.columns = ['PID', 'Age', 'Gender', 'State']

print(df)

# %%
# Display Head and Tail
print(data.head())
print(data.tail())

# %%
# Sort by State
today = df.sort_values(by='State')

print(today)

# %%
# Display column names
print(data.columns)

# %%
# Convert Age column to numeric
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

# Count patients in each state
top_states = (
    data.groupby('State')['Patient_ID']
    .count()
    .reset_index(name='Patients')
)

# Sort by number of patients
top_states = top_states.sort_values(
    by='Patients',
    ascending=False
).head(10)

# %%
# Bar Plot
plt.figure(figsize=(12,6))

sns.barplot(
    x='State',
    y='Patients',
    data=top_states
)

plt.title("Top 10 States by Number of Cancer Patients")
plt.xlabel("State")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
