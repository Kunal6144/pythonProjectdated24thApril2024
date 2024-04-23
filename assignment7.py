from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from assignment6 import X_train, y_train, X_test, y_test

# Assuming X_train, X_test, y_train, y_test are already defined

# Initialize logistic regression model
logistic_model = LogisticRegression()

# Train the model on the training data
logistic_model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = logistic_model.predict(X_test)

# Calculate accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of Logistic Regression Model:", accuracy)
