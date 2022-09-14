"""
# Outliers, leverage, and influence

roach = fish[fish['species'] == "Roach"]
print(roach.head())

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None)
plt.show()

# Exteme explanatory values
roach["extreme_l"] = ((roach["length_cm"] < 15) | (roach["length_cm"] > 26))

fig = plt.figure()

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None)

sns.scatterplot(x="length_cm",
                y="mass_g",
                hue="extreme_l",
                data=roach)

plt.show()

# Response values away from the regression line
roach["extreme_m"] = roach["mass-g"] < 1

fig = plt.figure()

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None)

sns.scatterplot(x="length_cm",
                y="mass_g",
                hue="extreme_l",
                style="extreme_m"
                data=roach)

# Levarage and influence
# # Leverage is a measure of how extreme the explanatory variable values are.
# # Influence measures how much the model would change if you left the observation out of the dataset when modeling

# # .get_influence() and .summary_frame()
mdl_roach = ols("mass_g ~ length_cm", data=roach).fit()
summary_roach = mdl_roach.get_influence().summary_frame()
roach["leverage"] = summary_roach["hat_dig"]

print(roach.head())

# Cook's distance 
# # Cook's distance is the most common measure of influence
roach["cooks_dist"] = summary_roach["cooks_d"]
print(roach.head())

# Most influential roaches
print(roach.sort_values("cooks_dist",ascending=False))

# Removing the most influential roach
roach_not_short = roach[roach["length_cm"] != 12.9]

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None,
            line_kws={"color":"green"})

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach_not_short,
            ci=None,
            line_kws={"color":"red"})

plt.show()
"""