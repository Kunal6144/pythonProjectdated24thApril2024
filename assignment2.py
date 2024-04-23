import pandas as pd

# Assuming 'df' is your original dataframe
# Example DataFrame creation
data = {
    'y': [0, 1, 1, 0],
    'job': ['teacher', 'engineer', 'doctor', 'lawyer'],
    'marital': ['single', 'married', 'single', 'married'],
    'default': ['no', 'yes', 'no', 'no'],
    'housing': ['yes', 'yes', 'no', 'yes'],
    'loan': ['no', 'yes', 'no', 'no'],
    'poutcome': ['success', 'failure', 'success', 'unknown']
}

df = pd.DataFrame(data)

# Selecting specific columns for the second dataframe
columns_to_select = ['y', 'job', 'marital', 'default', 'housing', 'poutcome']
df2 = df[columns_to_select].copy()

# Display the second dataframe
print("Second DataFrame:")
print(df2)
