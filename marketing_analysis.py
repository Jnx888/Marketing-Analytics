import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('marketing_dataset.csv')  # Ensure the file name matches exactly

# Aggregate opportunities across the different quarters
df['Total Opportunities'] = df.filter(regex='^Opps').sum(axis=1)

# Average deal sizes across quarters (assuming they are numbers and ignoring any non-numeric values)
deal_size_cols = df.filter(regex='^Avg Deal Size').columns
df[deal_size_cols] = df[deal_size_cols].apply(pd.to_numeric, errors='coerce')
df['Average Deal Size'] = df[deal_size_cols].mean(axis=1)

# Plot Total Opportunities by Marketing Bucket
plt.figure(figsize=(12, 6))
df.groupby('Marketing Bucket')['Total Opportunities'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Opportunities by Marketing Bucket')
plt.xlabel('Marketing Bucket')
plt.ylabel('Total Opportunities')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Total_Opportunities_by_Marketing_Bucket.png')
plt.show()

# Plot Average Deal Size by Marketing Bucket
plt.figure(figsize=(12, 6))
df.groupby('Marketing Bucket')['Average Deal Size'].mean().plot(kind='bar', color='lightgreen')
plt.title('Average Deal Size by Marketing Bucket')
plt.xlabel('Marketing Bucket')
plt.ylabel('Average Deal Size ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Average_Deal_Size_by_Marketing_Bucket.png')
plt.show()

# Print summary
print(df[['Marketing Bucket', 'Total Opportunities', 'Average Deal Size']].head())

# Save the modified DataFrame to a new CSV
df.to_csv('updated_marketing_dataset.csv', index=False)
