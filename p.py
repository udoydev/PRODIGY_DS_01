import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the local file (ensure the path is correct)
# Example: 'world_population.csv' is the downloaded file
df = pd.read_csv('./API_SP.POP.TOTL_DS2_en_csv_v2_3401680/API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv', skiprows=4)

# Check the first few rows of the dataset to see its structure
print(df.head())

# Filter for population data of the most recent year (e.g., 2020 or the latest available year)
df_latest = df[['Country Name', '2020']].dropna().sort_values(by='2020', ascending=False).head(10)

# Rename columns for ease
df_latest.columns = ['Country', 'Population']

# Create a bar chart using matplotlib
plt.figure(figsize=(10,6))
plt.barh(df_latest['Country'], df_latest['Population'], color='skyblue')
plt.xlabel('Population')
plt.ylabel('Country')
plt.title('Top 10 Most Populated Countries in 2020')
plt.tight_layout()

# Display the plot
plt.show()
