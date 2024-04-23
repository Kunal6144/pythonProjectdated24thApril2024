import pandas as pd

# Assuming 'df2' is your dataframe containing the selected columns
# Example DataFrame 'df2'
data = {
    'y': [0, 1, 1, 0],
    'job': ['teacher', 'engineer', 'doctor', 'lawyer'],
    'marital': ['single', 'married', 'single', 'married'],
    'default': ['no', 'yes', 'no', 'no'],
    'housing': ['yes', 'yes', 'no', 'yes'],
    'poutcome': ['success', 'failure', 'success', 'unknown']
}

df2 = pd.DataFrame(data)

# Convert categorical variables to dummy numerical values
df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'])

# Display the resulting dataframe
print("DataFrame with Dummy Variables:")
print(df3)
