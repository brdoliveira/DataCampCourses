"""
# Classification-Tree Learning

# # Building Blocks of a Decision-Tree
# # # Decision-Tree: data structure consisting of a hierarchy of nodes.
# # # Node: question or prediction. 
# # # Three kinds of nodes:
# # # # Root: no parent node, question giving rise to two children nodes.
# # # # Internal node: one parent node, question giving rise to two children node.
# # # # Leaf: one parent node, no children nodes --> prediction.

# # Information Gain (IG)
# # # Criteria to measure the impurity of a node I (node):
# # # # gini index,
# # # # entropy. ...

# # Classification-Tree Learning
# # # Nodes are grown recursively.
# # # At each node, split the data based on:
# # # # feature f and split-point sp to maximize IG(node).
# # # If IG(node)=0, declare the node a later. ...

# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClasifier
# Import train_test_split
from sklean.model_selection import train_test_split
# Import accuracy_score
from sklearn.metrics import accuracy_score
# Split the dataset into 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    statify=y,
    random_state=1       
)
# Instantiate dt, set 'criterion' to 'gini'
dt = DecisionTreeClassifier(criterion='gini',random_state=1)

# # Information Criterion in scikit-learn

# Fit dt to the training set
dt.fit(X_train,y_train)
# Predict test-set labels
y_pred = dt.predict(X_test)
# Evaluate test-set accuracy
accuracy_score(y_test, y_pred)

"""