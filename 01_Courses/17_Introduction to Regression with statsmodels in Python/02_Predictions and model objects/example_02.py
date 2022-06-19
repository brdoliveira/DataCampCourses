"""
# Working with model objects
# # .params atribute 
from statsmodels.formula.api import ols

mdl_mass_vs_length = ols("mass_g ~ length_cm", data = bream).fit()
print(mdl_mass_vs_length.params)

# ------------------

# fitted values: predictions on the original dataset
print(mdl_mass_vs_length.fittedvalues)

# or equivalently
explanatory_data = bream["length_cm"]
print(mdl_mass_vs_length.predict(explanatory_data))

# ------------------

# resid attribute: actual response values minus predicted response values
print(mdl_mass_vs_length.resid)

# or equivalently
print(bream["mass_g"] - mdl_mass_vs_length.fittedvalues)

print(mdl_mass_vs_length.summary())

"""
from statsmodels.formula.api import ols
import pandas as pd
import numpy as np

# Create explanatory_data 
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

taiwan_real_estate = pd.read_csv("./data/taiwan_real_estate2.csv")

# Create the model object
mdl_price_vs_conv = ols("price_twd_msq ~ n_convenience", data=taiwan_real_estate)

# Fit the model
mdl_price_vs_conv = mdl_price_vs_conv.fit()

# Print the parameters of the fitted model
print(mdl_price_vs_conv.params)

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)

# Create prediction_data
prediction_data = explanatory_data.assign(
    price_twd_msq = mdl_price_vs_conv.predict(explanatory_data))

# Get the coefficients of mdl_price_vs_conv
coeffs = mdl_price_vs_conv.params

# Get the intercept
intercept = coeffs[0]

# Get the slope
slope = coeffs[1]

# Manually calculate the predictions
price_twd_msq = intercept + slope * explanatory_data
print(price_twd_msq)

# Compare to the results from .predict()
print(price_twd_msq.assign(predictions_auto=mdl_price_vs_conv.predict(explanatory_data)))