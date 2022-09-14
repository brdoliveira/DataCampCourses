"""
# Generalization Error

# # Supervised Learning - Under the Hood
# # # Supervised Learning: y = f(x), f is unknown.

# # Goals of Supervisef Learning
# # # Find a model ^f that best approximates f: ^f = f
# # # ^f can be Logistic Regression, Decision Tree, Neural Network...
# # # Discard noise as much as possible.
# # # End goal: ^f should achiave a low predictive error on unseen datasets.

# # Difficulties in Approximating f
# # # Overfitting: ^f(x) fits the training set noise.
# # # Underfitting: ^f is not flexible enough to approximate f.

# # Generalization Error
# # # Generalization Error of ^f: Does ^f generalize well on unseen data?
# # # It can be decomposed as follow: Generalization Error of
# # # ^f = bias ** 2 + variance + irreducible error

# # Bias
# # # Bias: error term that tells you, on average, how much ^f != f.

# # Variance
# # # Variance: tells you how much ^f is inconsistent over different training sets.

# # Model Complexity
# # # Model Complexity: set the flebility of ^f.
# # # Example: Maximum tree depth, Minimum samples per leaf, ...
"""