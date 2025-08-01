import pandas as pd
import os

# Print Current Working Directory to verify path
print("Current Working Directory:", os.getcwd())

# Attempt to Load Dataset
try:
    df = pd.read_csv('Superstore_Dirty.csv')
    print("\nDataset loaded successfully! Here's a preview:")
    print(df.head())
except FileNotFoundError:
    print("\nERROR: Superstore_Dirty.csv not found in the current directory.")
except Exception as e:
    print("\nAn unexpected error occurred:", str(e))

# Check for duplicate rows
print("\nDuplicate rows before cleaning:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Verify duplicates removed
print("Duplicate rows after cleaning:", df.duplicated().sum())

# Check missing values count
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Fill missing 'Sales' with mean value
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Fill missing 'Category' with 'Unknown'
df['Category'] = df['Category'].fillna('Unknown')

# Drop rows where 'Order ID' is missing (assuming it's a critical field)
df = df.dropna(subset=['Order ID'])

# Verify missing values handled
print("\nMissing values after cleaning:\n", df.isnull().sum())

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Convert 'Sales' to float (if not already)
df['Sales'] = df['Sales'].astype(float)

# Clean column names: lowercase, no spaces
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

print("\nFinal cleaned data preview:\n", df.head())

# Save cleaned data to a new CSV
df.to_csv('Superstore_Cleaned.csv', index=False)
print("\nCleaned data saved as Superstore_Cleaned.csv")

import os

# Save cleaned data with full path
output_path = r'C:\Users\navya\OneDrive\Desktop\Desktop\pandas\dataset-main\dataset-main\jupp\Superstore_Cleaned.csv'
df.to_csv(output_path, index=False)

print(f"\nCleaned data saved successfully at: {output_path}")


