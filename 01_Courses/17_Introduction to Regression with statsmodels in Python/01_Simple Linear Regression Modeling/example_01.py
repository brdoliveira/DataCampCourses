"""
# A tale of two variables

# # Descriptive statistics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

swedish_motor_insurance = pd.read_csv("./swedish_motor_insurance.csv")
print(swedish_motor_insurance.mean())

print(swedish_motor_insurance['n_claims'].corr(swedish_motor_insurance['total_payment_sek']))

# What is regression?
# # Statistical models to explore the relationship a response variable and some explanatory variables.
# # Given values of explanatory variables, you can predict the values of the response variable.

# Jargon
# # Response variable (a.k.a. dependent variable)
# # # The variable that you want to predict
# # Explanatory variables (a.k.a. independent variables)
# # # The variables that explain how the response variable will charge

# Linear regression and logistic regression
# # Linear regression
# # # The response variable is numeric.
# # Logistic regression
# # # The response variable is logical.
# # Simple linear/logistic regression
# # # There is only one explanatory variable.

sns.scatterplot(x="n_claims",
                y="total_payment_sek",
                data=swedish_motor_insurance)
plt.show()

# Adding a linear trend line 
sns.regplot(x="n_claims",
            y="total_payment_sek",
            data=swedish_motor_insurance,
            ci=None)
plt.show()

# Python packages for regression
# # statsmodels
# # # Optimized for insight (focus in this course)
# # scikit-learn
# # # Optimized for prediction (focus in other DataCamp course)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

taiwan_real_estate = pd.read_csv("./data/taiwan_real_estate2.csv")

# Draw the scatter plot
sns.scatterplot(x="n_convenience",
                y="price_twd_msq",
                data=taiwan_real_estate)

# Draw a trend line on the scatter plot of price_twd_msq vs. n_convenience
sns.regplot(x="n_convenience",
         y="price_twd_msq",
         data=taiwan_real_estate,
         ci=None,
         scatter_kws={'alpha': 0.5})

# Show the plot
plt.show()