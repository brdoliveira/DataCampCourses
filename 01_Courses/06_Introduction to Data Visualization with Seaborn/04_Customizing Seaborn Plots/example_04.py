import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Putting it all together

pandas_df = pd.read_csv("./data/pandasdf.csv")

# Relational plots
# #  Show the relationship between two quantitative variables
# # Examples : scatter plots, line plots
sns.relplot(x="x_variable_name",
            y="y_variable_name",
            data=pandas_df,
            kind="scatter")

# Categorical plots
# #  Show the distribuition of a quantitative variable within categories defined by a categorical variable
# # Examples: bar plots, count plots, box plots, point plots
sns.catplot(x="x_variable_name",
            y="y_variable_name",
            data=pandas_df,
            kind="box")

# Adding a third variable(hue)
# # Setting hue will create subgroups that are displayed as different colors on a single plot

# Adding a thid variable(col/row)
# # Setting row and/or col in relplot() or catplot() will create subgroups that are displayed on separate subplots. 

#  Customization
# # Change the background: sns.set_style()
# # Change the main element colors: sns.set_palette()
# # Change the scale: sns.set_context()

# Adding a title
# | Object type |   Plot types                  | How to Add Title |
# | FacetGrid   | relplot(),catplot()           | g.fig.suptitle() |
# | AxesSuplot  | scatterplot(),countplot(),etc.| g.set_title()    |

# Final touches

# # Add x- and y-axis labels:
gdp_data = pd.read_csv("./data/gdp_data.csv")

g = sns.catplot(x="Region",
                y="Bithrate",
                data = gdp_data,
                kind="box",
                col="Group")

g.set(xlabel="new x-axis label",
      ylabel="new y-axis label")

# # Rotate x-tick label:
plt.ticks(rotation=90)


plt.show()