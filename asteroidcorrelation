import pandas as pd

df = pd.read_csv('https://gitlab.com/mirsakhawathossain/pha-ml/-/raw/master/Dataset/dataset.csv')

# Print high-level details about the dataset
def print_high_level_details(df):
    print("Shape of the dataset:", df.shape)
    print("\nColumn names:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print("\nMissing values per column:\n", df.isnull().sum())
    print("\nSummary statistics (numerical):\n", df.describe())
    print("\nSummary statistics (categorical):\n", df.describe(include=['object']))
    print("\nNumber of duplicate rows:", df.duplicated().sum())
    print("\nUnique values per column:")
    for col in df.columns:
        print(f"  {col}: {df[col].nunique()}")

print_high_level_details(df)

# Correlation analysis between two numerical columns: 'H' and 'diameter'
def print_correlation(df, col1, col2):
    if col1 in df.columns and col2 in df.columns:
        corr = df[[col1, col2]].corr().iloc[0,1]
        print(f"\nCorrelation between '{col1}' and '{col2}': {corr}")
    else:
        print(f"\nColumns '{col1}' and/or '{col2}' not found in the dataset.")

print_correlation(df, 'H', 'diameter')
# You can change 'H' and 'diameter' to any other numerical columns for different correlation analysis.
