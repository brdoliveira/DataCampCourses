"""
# Transforming variables

perch = fish[fish["especies"] == "Perch"]
print(perch.head())

sns.regplot(x="length_cm",
            y="mass_g",
            data=perch,
            ci=None)

plt.show()

# Plotting mass vs. length cubed
perch["length_cm_cubed"] = perch["length_cm"] ** 3
sns.regplot(x="length_cm_cubed",
            y="mass_g",
            data=perch,
            ci=None)

plt.show()

mdl_perch = ols("mass_g ~ length_cm_cubed",data=perch).fit()
print(mdl_perch.params)

# Predicting mass vs. length cubed
explanatory_data = pd.DataFrame({"length_cm_cubed": np.arange(10,41,5) ** 3,
                                 "length_cm": np.arange(10,41,5)})

prediction_data = explanatory_data.assign(
    mass_g = mdl_perch.predict(explanatory_data)
)
print(prediction_data)

fig = plt.figure()
sns.regplot(x="length_cm_cubed",
            y="mass_g",
            data=perch,
            ci=None)
sns.scatterplot(x="length_cm_cubed",
                y="mass_g",
                data=prediction_data,
                color="red",
                marker="s")
plt.show()
"""
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

ad_conversion = pd.read_csv("./data/ad_conversion.csv")
# print(ad_conversion.head())

ad_conversion["sqrt_spent_usd"] = np.sqrt(ad_conversion["spent_usd"])
ad_conversion["sqrt_n_impressions"] = np.sqrt(ad_conversion["n_impressions"])

sns.regplot(x="sqrt_spent_usd",
            y="sqrt_n_impressions",
            data=ad_conversion,
            ci=None)
plt.show()

# Modeling and predicting
mdl_ad = ols("sqrt_n_impressions ~ sqrt_spent_usd", data=ad_conversion).fit()

explanatory_data = pd.DataFrame({"sqrt_spent_usd": np.sqrt(np.arange(0,601,100)),
                                 "spent_usd": np.arange(0,601,100)})

prediction_data = explanatory_data.assign(sqrt_n_impression=mdl_ad.predict(explanatory_data),
                                         n_impressions=mdl_ad.predict(explanatory_data) ** 2)

print(prediction_data)