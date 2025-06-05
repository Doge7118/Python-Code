import pandas as pd # type: ignore

url = "https://raw.githubusercontent.com/YBIFoundation/Dataset/refs/heads/main/Stars.csv"

try:
    df = pd.read_csv(url)
    print("Printing the entire DataFrame summary")
    print(df)
    print("Printing the first 5 rows of the DataFrame")
    print(df.head())
    print("Printing the last 5 rows of the DataFrame")
    print(df.tail())
    print("Printing the summary statistics of the DataFrame")
    print(df.describe())
    print("Printing the data types of each column in the DataFrame")
    print(df.dtypes)
    print("Printing the shape of the DataFrame")
    print(df.shape)
    print("Printing the columns of the DataFrame")
    print(df.columns)
    print("Printing the index of the DataFrame")
    print(df.index)
    print("Printing the unique values in the 'Star color' column")
    print(df['Star color'].unique())
    print("Printing the unique values in the 'Spectral Class' column")
    print(df['Spectral Class'].unique())
    print("Printing the unique values in the 'Star category' column")
    print(df['Star category'].unique())
except Exception as e:
    print(f"Error reading CSV from URL: {e}")
