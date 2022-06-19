"""
# Regression on the mean

# The concept
# # Response value = fitted value + residual
# # "The stuff you explained" + "the stuff you couldn't explain"
# # Extreme cases are often due to randomness
# # Regression to the mean menas extreme cases don't persist over time

# Pearson

fig = plt.figure()

sns.regplot(x="father_height_cm",
                y="son_height_cm,
                data=father_son,
                ci=None,
                line_kws={"color":"black"})

plt.axline(xy1=(150,150),
          slope=1,
          linewidth=2,
          color="green")

plt.axis("equal") equal to unit of measurement
plt.show()

mdl_son_vs_father = ols("son_height_cm ~ father_height_cm", data=father_son).fit()
print(mdl_son_vs_father.params)

# Making predictions
really_tall_father = pd.DataFrame({"father_height_cm" : [190]})
mdl_son_vs_father.predict(really_tall_father)

really_short_father = pd.DataFrame({"father_height_cm" : [150]})
mdl_son_vs_father.predict(really_short_father)

"""
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sp500_yearly_returns = pd.read_csv("./data/sp500_yearly_returns.csv")

# Create a new figure, fig
fig = plt.figure()

# Plot the first layer: y = x
plt.axline(xy1=(0,0), slope=1, linewidth=2, color="green")

# Add scatter plot with linear regression trend line
sns.regplot(x="return_2018",y="return_2019",data=sp500_yearly_returns,ci=None,line_kws={"color":"black"})

# Set the axes so that the distances along the x and y axes look the same
plt.axis("equal")

# Show the plot
plt.show()

# Run a linear regression on return_2019 vs. return_2018 using sp500_yearly_returns
mdl_returns = ols("return_2019 ~ return_2018", data=sp500_yearly_returns).fit()

# Print the parameters
print(mdl_returns.params)

# Create a DataFrame with return_2018 at -1, 0, and 1 
explanatory_data = pd.DataFrame({"return_2018": [-1, 0, 1]})

# Use mdl_returns to predict with explanatory_data
print(mdl_returns.predict(explanatory_data))