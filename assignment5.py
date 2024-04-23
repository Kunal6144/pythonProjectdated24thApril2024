# Assuming 'df3' is your dataframe with dummy variables
# Example DataFrame 'df3'
import pandas as pd

data = {
    'y': [0, 1, 1, 0],
    'job_teacher': [1, 0, 0, 0],
    'job_engineer': [0, 1, 0, 0],
    'job_doctor': [0, 0, 1, 0],
    'job_lawyer': [0, 0, 0, 1],
    'marital_single': [1, 0, 1, 0],
    'marital_married': [0, 1, 0, 1],
    'default_no': [1, 0, 1, 1],
    'default_yes': [0, 1, 0, 0],
    'housing_yes': [1, 1, 0, 1],
    'housing_no': [0, 0, 1, 0],
    'poutcome_success': [1, 0, 1, 0],
    'poutcome_failure': [0, 1, 0, 0],
    'poutcome_unknown': [0, 0, 0, 1]
}

df3 = pd.DataFrame(data)

# Selecting the 'y' column as the target variable
y = df3['y']

# Selecting all remaining columns as the explanatory variables X
X = df3.drop(columns=['y'])

# Display the target variable y and explanatory variables X
print("Target Variable y:")
print(y)
print("\nExplanatory Variables X:")
print(X)
