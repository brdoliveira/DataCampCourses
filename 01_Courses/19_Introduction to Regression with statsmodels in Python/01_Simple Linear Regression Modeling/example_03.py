"""
# Categorical explanatory variables
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Visualizing 1 numeric and 1 categorical variable
sns.distplot(data=fish,
            x="mass_g",
            col="species",
            col_wrap=2,
            bins=9)
plt.show()

summary_stats = fish.groupby("species")["mass_g"].mean()
print(summary_stats)

# From previous slide, model with intercept
mdl_mass_vs_species = ols("mass_g ~ species", data=fish).fit()

# Model without an intercept
mdl_mass_vs_species = ols("mass_g ~ species + 0", data=fish).fit()

print(mdl_mass_vs_species.params)
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

taiwan_real_estate = pd.read_csv("./data/taiwan_real_estate2.csv")

# Histograms of price_twd_msq with 10 bins, split by the age of each house
sns.displot(data=taiwan_real_estate,
            x="price_twd_msq",
            col="house_age_years",
            bins=10)

# Show the plot
plt.show()

# Calculate the mean of price_twd_msq, grouped by house age
mean_price_by_age = taiwan_real_estate.groupby("house_age_years")["price_twd_msq"].mean()

# Print the result
print(mean_price_by_age)

# Create the model, fit it
mdl_price_vs_age = ols("price_twd_msq ~ house_age_years", data=taiwan_real_estate).fit()

# Print the parameters of the fitted model
print(mdl_price_vs_age.params)

# Update the model formula to remove the intercept
mdl_price_vs_age0 = ols("price_twd_msq ~ house_age_years + 0", data=taiwan_real_estate).fit()

# Print the parameters of the fitted model
print(mdl_price_vs_age0.params)