import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read Dataset
data = pd.read_csv(r"D:\covid_19_india.csv.xls")

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
df = data[['Date', 'Time', 'State/UnionTerritory', 'ConfirmedIndianNational']]
df.columns = ['Dt', 'Tt', 'St', 'Cfmd']
print(df)

# %%
# Display Head and Tail
print(data.head())
print(data.tail())

# %%
# Sort by State
today = df.sort_values(by='St')
print(today)

# %%
# Display column names
print(data.columns)

# %%
# Convert Deaths column to numeric
data['Deaths'] = pd.to_numeric(data['Deaths'], errors='coerce')

# Group by State and calculate total deaths
top_states = (
    data.groupby('State/UnionTerritory')['Deaths']
    .sum()
    .reset_index()
)

# Sort by deaths
top_states = top_states.sort_values(by='Deaths', ascending=False).head(10)

# Plot Bar Chart
plt.figure(figsize=(6,4))

sns.barplot(
    x='State/UnionTerritory',
    y='Deaths',
    data=top_states
)

plt.title("Top 10 States by Deaths")
plt.xlabel("State/Union Territory")
plt.ylabel("Deaths")
plt.xticks(rotation=45)

plt.show()
