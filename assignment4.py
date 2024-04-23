import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df3' is your dataframe with dummy variables
# Example DataFrame 'df3'
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

# Create heatmap of correlation coefficients
correlation_matrix = df3.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Correlation Coefficients')
plt.show()

# Describe the correlation
print("Description of Correlation:")
print(correlation_matrix.describe())
