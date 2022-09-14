"""
# Ensemble Learning

# # Advantages of CARTs
# # # Simple to undestand.
# # # Simple to interpret.
# # # Easy to use.
# # # Flexibility: ability to describe non-linear dependencies.
# # # Preprocessing: no need to standardize or normalize features, ...

# # Limitations of CARTs
# # # Classification: can only produce orthogonal decision boundaries.
# # # Sensitive to small variations in the training set
# # # High variance: unconstrained CARTs may overfit the training set
# # # Solution: ensemble learning.

# # Ensemble Learning
# # # Train different models on the same dataset.
# # # Let each model make its predictions.
# # # Meta-model: aggregates predictions of individual models.
# # # Final prediction: more robust and less prone to errors.
# # # Best results: models are skillfull in different ways.

# # Ensemple Learning in Practice: Voting Classifier
# # # Binary classification
# # # N classifiers make predictions: P1, P2, ... PN with Pi = 0 or 1.
# # # Meta-model prediction: hard voting.

# # Voting Classifier in sklearn (Breast-Cancer dataset)
# Import functions to compute accuracy and split data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Import models, including VotingClassifier meta-model
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.ensemble import VotingClassifier

# Set seed for reproducibility
SEED = 1

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X,y,
    test_size = 0.3,
    random_state=SEED
)

# Instantiate individual classifiers
lr = LogisticRegression(random_state=SEED)
knn = KNN()
dt = DecisionTreeClassifier(random_state=SEED)
# Define as list called classifier that contains the tuples (classifier_name, classifier)
classifiers = [('Logistic Regression', lr),
              ('K Nearest Neighbours',knn),
              ('Classification Tree',dt)]

# Iterate over the defined list of tuples containing the classifiers
for clf_name, clf in classifiers:
    # fit clf to the training set
    clf.fit(X_train,y_train)

    # Predict the labels of the test set
    y_pred = clf.predict(X_test)

    # Evaluate the accuracy of clf on the test set
    print('{:s} : {:.3f}'.format(clf_name, accuracy_score(y_test, y_pred)))

# Instantiate a VotingClassifier 'vc'
vc = VotingClassifier(estimators=classifiers)

# Fit 'vc' to the traing set and predict test set labels
vc.fit(X_train, y_train)
y_pred = vc.predict(X_test)

# Evaluate the test-set accuracy of 'vc'
print('Voting Classifier: {.3f}'.format(accuracy_score(y_test,y_pred)))
"""