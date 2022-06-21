"""
# Visualizing model fit

# Residual properties of a good fit
# # Raesiduals are normally distributed
# # The mean of the residuals is zero

# # Residuals vs. fitted
sns.resiplot(x="length_cm",y="mass_g",data=bream,lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Residuals")

# # Q-Q PLOT
from statsmodels.api import qqplot
qqplot(data=mdl_bream.resid,fit=True,line="45")

# # Scale-Location PLOT
model_norm_residuals_bream = mdl_bream.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt_bream = np.sqrt(np.abs(model_norm_residuals_bream))
sns.regplot(x=mdl_bream.fittedvalues, y=model_norm_residuals_abs_sqrt_bream, ci=None, lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Sqrt of abs val of stdized residuals")

plt.show()
"""
from statsmodels.formula.api import ols
from statsmodels.api import qqplot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

taiwan_real_estate = pd.read_csv("./data/taiwan_real_estate2.csv")

# Plot the residuals vs. fitted values
sns.residplot(x="n_convenience", y="price_twd_msq", data=taiwan_real_estate,lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Residuals")

# Show the plot
plt.show()

# ------------------------

# Create the model object
mdl_price_vs_conv = ols("price_twd_msq ~ n_convenience", data=taiwan_real_estate)

# Fit the model
mdl_price_vs_conv = mdl_price_vs_conv.fit()

# Create the Q-Q plot of the residuals
qqplot(data=mdl_price_vs_conv.resid, fit=True, line="45")

# Show the plot
plt.show()

# ------------------------

# Preprocessing steps
model_norm_residuals = mdl_price_vs_conv.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))

# Create the scale-location plot
sns.regplot(x=mdl_price_vs_conv.fittedvalues, y=model_norm_residuals_abs_sqrt, ci=None, lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Sqrt of abs val of stdized residuals")

# Show the plot
plt.show()