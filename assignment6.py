from sklearn.model_selection import train_test_split

from assignment5 import X, y

# Assuming you have already defined 'X' and 'y'

# Split the dataset into training and testing sets with a 75/25 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Display the shapes of the resulting datasets
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)
