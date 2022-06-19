"""
# Making predictions

bream = fish[fish["especies"] == "Bream"]
print(bream.head())

sns.regplot(x="length_cm",
            y="mass_g",
            data=bream,
            ci=None)

plt.show()

# Running the model
mdl_mass_vs_length = ols("mass_g ~length_cm",data=bream).fit()
print(mdl_mass_vs_length.params)

explantory_data = pd.DataFrame({"length_cm": np.arange(20,41)})

print(mdl_mass_vs_length.predict(explanatory_data))

prediction_data = explanatory_data.assign(
    mass_g = mdl_mass_vs_lenght.predict(explanatory_data) 
)

print(prediction_data)

import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()
sns.regplot(x="length_cm",
            y="mass_g",
            data=bream,
            ci=None)
sns.scatterplot(x="length_cm",
                y="mass_g",
                data=prediction_data,
                color="red",
                marker="s")
plt.show()

# Extrapolating
# # Extrapoling means ranking predictions outside the range of observed data.

little_beam = pd.DataFrame({"length_cm": [10] })
pred_little_beam = little_beam.assign(
    mass_g = mdl_mass_vs_lenght.predict(little_beam)
)
print(pred_little_beam)
"""
# Import numpy with alias np
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
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

# Print the result
print(prediction_data)

# Create a new figure, fig
fig = plt.figure()

sns.regplot(x="n_convenience",
            y="price_twd_msq",
            data=taiwan_real_estate,
            ci=None)
# Add a scatter plot layer to the regplot
sns.scatterplot(x="n_convenience",
                y="price_twd_msq",
                data=prediction_data,
                color="r",
                marker="s")

# Show the layered plot
plt.show()