"""
# Fitting a linear regression

# Straight lines are defined by two things
# # Intercept
# # # The Y value at the point when X is zero.
# # Slope 
# # # The amount the Y value increases if you increase X by one.
# Equation
y = intercept + slope * x

from statsmodels.formula.api import ols

mdl_payment_vs_claims = ols("total_payment_sek ~ n_claims",
                            data=swedish_motor_insurance)

mdl_payment_vs_claims = mdl_payment_vs_claims.fit()
print(mdl_payment_vs_claims.params)

# total_payment_sek = 19.99 + 3.41 * n_claims
"""
import pandas as pd
from statsmodels.formula.api import ols

taiwan_real_estate = pd.read_csv("./data/taiwan_real_estate2.csv")

# Create the model object
mdl_price_vs_conv = ols("price_twd_msq ~ n_convenience", data=taiwan_real_estate)

# Fit the model
mdl_price_vs_conv = mdl_price_vs_conv.fit()

# Print the parameters of the fitted model
print(mdl_price_vs_conv.params)