import pandas as pd

# Assuming the file delimiter is a semicolon (;), change it if it's different
delimiter = ';'

# Read the CSV file into a pandas dataframe
df = pd.read_csv('bank.csv', delimiter=delimiter)

# Inspect the dataframe
print("DataFrame Information:")
print(df.info())
print("\nColumn Names:")
print(df.columns)
