
# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(style="whitegrid", palette="colorblind")

# Load the dataset
# NOTE: Replace the file path below with the actual path to your CSV
df = pd.read_csv("dinesafe.csv")

# Display the first few rows to understand structure (optional)
print(df.head())

# Basic cleaning
# Drop rows with missing violation details
df_clean = df.dropna(subset=['infraction_details'])

# Count frequency of each violation
violation_counts = df_clean['infraction_details'].value_counts().head(10)

# Reset index for plotting
violation_df = violation_counts.reset_index()
violation_df.columns = ['Violation Description', 'Count']

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    data=violation_df,
    y='Violation Description',
    x='Count',
    palette='colorblind'
)

# Add labels and title
plt.title('Top 10 Most Common Food Safety Violations in Toronto', fontsize=14)
plt.xlabel('Number of Violations', fontsize=12)
plt.ylabel('')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Tight layout and save
plt.tight_layout()
plt.savefig("images/viz1_bar_chart.png", dpi=300)
plt.show()