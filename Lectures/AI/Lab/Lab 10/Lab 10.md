# Decision tree
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib import pyplot as plt

dataset = pd.read_csv('./social_network_ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(dataset.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)  # Use 'gini' for Gini impurity
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)

#  Evaluate the model by making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix: \n {cm}")

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Visualize the decision tree
plt.figure(figsize=(25, 20))
tree.plot_tree(classifier, class_names=['no', 'yes'], filled=True, rounded=True)
plt.show()

# Predicting a new result
new_data = [[30, 87000]]
prediction = classifier.predict(new_data)
print(f"Prediction for new data: {prediction}")

y_train_pred = classifier.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy  # Using the test accuracy you already calculated

print(f"Training Accuracy: {train_accuracy}")
print(f"Test Accuracy: {test_accuracy}")
print(f"Accuracy difference: {train_accuracy - test_accuracy}")

# Visualize the original tree
plt.figure(figsize=(15, 10))
tree.plot_tree(classifier, class_names=['no', 'yes'], filled=True, rounded=True, fontsize=8)
plt.title("Original Decision Tree")
plt.tight_layout()
plt.savefig('original_tree.png')
plt.show()

# Fix overfitting using pruning (limiting tree depth and min samples)
classifier_pruned = DecisionTreeClassifier(criterion='entropy',
                                          max_depth=3,  # Limit depth
                                          min_samples_split=10,  # Min samples to split
                                          min_samples_leaf=5,  # Min samples in leaf
                                          random_state=0)
classifier_pruned.fit(X_train, y_train)

# Evaluate pruned model
y_train_pred_pruned = classifier_pruned.predict(X_train)
y_test_pred_pruned = classifier_pruned.predict(X_test)

train_accuracy_pruned = accuracy_score(y_train, y_train_pred_pruned)
test_accuracy_pruned = accuracy_score(y_test, y_test_pred_pruned)

print("\nAfter pruning:")
print(f"Training Accuracy: {train_accuracy_pruned}")
print(f"Test Accuracy: {test_accuracy_pruned}")
print(f"Accuracy difference: {train_accuracy_pruned - test_accuracy_pruned}")

# Visualize the pruned tree
plt.figure(figsize=(15, 10))
tree.plot_tree(classifier_pruned, class_names=['no', 'yes'], filled=True, rounded=True, fontsize=10)
plt.title("Pruned Decision Tree")
plt.tight_layout()
plt.savefig('pruned_tree.png')
plt.show()

# Compare results with bar chart
labels = ['Original Model', 'Pruned Model']
train_accuracies = [train_accuracy, train_accuracy_pruned]
test_accuracies = [test_accuracy, test_accuracy_pruned]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, train_accuracies, width, label='Training Accuracy')
rects2 = ax.bar(x + width/2, test_accuracies, width, label='Test Accuracy')

ax.set_ylabel('Accuracy')
ax.set_title('Model Performance Before and After Pruning')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.savefig('accuracy_comparison.png')
plt.show()
```

# Classification on Adult Income Data
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib import pyplot as plt
dataset = pd.read_csv('./adult_income.csv')
print(dataset.head())

## Step 1:
X = dataset.drop('income_high', axis=1)
y = dataset['income_high']

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X, drop_first=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train decision tree
original_tree = DecisionTreeClassifier(random_state=42)
original_tree.fit(X_train, y_train)

# Evaluate on both sets
train_pred = original_tree.predict(X_train)
test_pred = original_tree.predict(X_test)
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)

print(f"Original Tree - Training Accuracy: {train_accuracy:.4f}")
print(f"Original Tree - Test Accuracy: {test_accuracy:.4f}")
print(f"Difference (Train-Test): {train_accuracy - test_accuracy:.4f}")

# Step 2:
pruned_tree = DecisionTreeClassifier(
    max_depth=5,              # Limit tree depth
    min_samples_split=50,     # Require more samples to split
    min_samples_leaf=20,      # Require more samples in leaf nodes
    random_state=42
)
pruned_tree.fit(X_train, y_train)

# Evaluate pruned tree
train_pred_pruned = pruned_tree.predict(X_train)
test_pred_pruned = pruned_tree.predict(X_test)
train_accuracy_pruned = accuracy_score(y_train, train_pred_pruned)
test_accuracy_pruned = accuracy_score(y_test, test_pred_pruned)

print(f"\nPruned Tree - Training Accuracy: {train_accuracy_pruned:.4f}")
print(f"Pruned Tree - Test Accuracy: {test_accuracy_pruned:.4f}")
print(f"Difference (Train-Test): {train_accuracy_pruned - test_accuracy_pruned:.4f}")


# Step 3:
plt.figure(figsize=(10, 6))
plt.bar(['Original Train', 'Original Test', 'Pruned Train', 'Pruned Test'],
        [train_accuracy, test_accuracy, train_accuracy_pruned, test_accuracy_pruned],
        color=['blue', 'orange', 'green', 'red'])
plt.axhline(y=test_accuracy, color='orange', linestyle='--')
plt.axhline(y=test_accuracy_pruned, color='red', linestyle='--')
plt.ylabel('Accuracy')
plt.title('Model Performance Before and After Pruning')
plt.ylim(0.7, 1.0)  # Adjust as needed

for i, v in enumerate([train_accuracy, test_accuracy, train_accuracy_pruned, test_accuracy_pruned]):
    plt.text(i, v + 0.01, f"{v:.4f}", ha='center')

plt.tight_layout()
plt.show()

# Visualize original tree (limited to depth=3 for display purposes)
plt.figure(figsize=(20, 10))
tree.plot_tree(original_tree, max_depth=3, feature_names=X.columns, filled=True, fontsize=10)
plt.title("Original Decision Tree (Limited to Depth 3)")
plt.tight_layout()
plt.show()

# Visualize pruned tree
plt.figure(figsize=(20, 10))
tree.plot_tree(pruned_tree, feature_names=X.columns, filled=True, fontsize=10)
plt.title("Pruned Decision Tree")
plt.tight_layout()
```