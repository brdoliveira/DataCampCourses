"""
# Quatifying model fit

mdl_bream = ols("mass_g ~ length_cm", data=bream).fit()
print(mdl_bream.summary())

print(mdl_bream.rsquared)

# It's just correlation squared
coeff_determination = bream["length_cm"].corr(bream["mass_g"]) ** 2
print(coeff_determination)

# Residual standard error (RSE)
# # A "typical" different between a prediction and an observed response
# # Is has same unit as the response variable.
# # MSE = RSE^2

mse = mdl_bream.mse_resid
print("mse: ",mse)

rse = np.sqrt(mse)
print("rse: ",rse)

# Calculating RSE: residuals squared
residuals_sq = mdl_bream.resid ** 2
print("residuals sq: \n", residuals_sq)

# Calculating RSE: sum of residuals squared
resid_sum_of_sq = sum(residuals_sq)
print("resid sum of sq:", resid_sum_of_sq)

# Calculating RSE: degrees of freedom
deg_freedom = len(bream.index) - 2
print("deg freedom: ", deg_freedom) # degrees of freedom equals the number of observations minus the number of model coefficients.

# Calculating RSE: square root of ratio
rse = np.sqrt(resid_sum_of_sq/deg_freedom)
print("rse: ",rse)

# Root-mean-square-root (RMSE)
n_obs = len(bream.index)

rmse = np.sqrt(resid_sum_of_sq/n_obs)
print("rmse: ", rmse)
"""

