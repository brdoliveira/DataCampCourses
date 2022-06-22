"""
# Quantifying logistic regression fit

# # Confusion Matrix: counts of outcomes
# # True positive: The customer churned and the model predicted they would.
# # False positive: The customer didn't churn, but the model predicted they would.
# # True negative: The customer didn't churn and the model predicted they wouldn't.
# # False negative: The customer churned, but the model predicted they wouldn't.

actual_response = churn["has_churned"]

predicted_response = np.round(mdl_recency.predict())

outcomes = pd.DataFrame({"actual_response": actual_response,
                         "predicted_response": predicted_response})

print(outcomes.value_counts(sort=False))

coef_matrix = mdl_recency.pred_table()
print(coef_matrix)

from statsmodels.graphics.mosaicplot import mosaic

mosaic(coef_matrix)

# Accuracy
# # Acuracy is the proportion of correct predictions.
# # # accuracy = (TN + TP) / (TN + FN + FP + TP)

TN = conf_matrix[0,0]
TP = conf_matrix[1,1]
FN = conf_matrix[1,0]
FP = conf_matrix[0,1]

acc = (TN + TP) / (TN + FN + FP + TP)
print(acc)

# Sensitivy 
# # Sensitivy is the proportion of true positives.
# # # sensitivity = TP / (FN + TP)

TN = conf_matrix[0,0]
TP = conf_matrix[1,1]
FN = conf_matrix[1,0]
FP = conf_matrix[0,1]

sens = TP / (FN + TP)
print(sens)

# Specificity 
# # Specificity is the proportion of true negatives.
# # # specificity = TN / (TN + FP)

TN = conf_matrix[0,0]
TP = conf_matrix[1,1]
FN = conf_matrix[1,0]
FP = conf_matrix[0,1]

spec = TN / (TN + FP)
print(spec)

"""