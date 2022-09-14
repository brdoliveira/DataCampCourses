import matplotlib.pyplot as plt
import pandas as pd

fig , ax = plt.subplots()

mens_rowing = pd.read_csv("./data/mens_rowing.csv")
mens_gymnastics = pd.read_csv("./data/mens_gymnastics.csv")

# ax.bar("Rowing",
#     mens_rowing["Height"].mean(),
#     yerr=mens_rowing["Height"].std())
# # yerr --> Adding number additional

# ax.bar("Gymnastics",
#     mens_gymnastics["Height"].mean(),
#     yerr=mens_gymnastics["Height"].std())


### Line plot with errobar ###

# fig,ax = plt.subplots()

# seattle_weather = pd.read_excel('./data/seattle_weather.csv')

# austin_weather = pd.read_excel('./data/austin_weather.csv')

# seattle_weather[["MONTH","MLY-TAVG-NORMAL"]].head()

# austin_weather[["MONTH","MLY-TAVG-NORMAL"]].head()

# ax.plot(seattle_weather["MONTH"],
#         seattle_weather["MLY-TAVG-NORMAL"],
#         yerr=seattle_weather["MLY-TAVG-NORMAL"])

# ax.plot(austin_weather["MONTH"],
#         austin_weather["MLY-TAVG-NORMAL"],
#         yerr=austin_weather["MLY-TAVG-STDDEV"])

# ax.set_ylabel("Temperature (Fahrenheit)")

# plt.show()

fig, ax = plt.subplots()
ax.boxplot([mens_rowing["Height"],
        mens_gymnastics["Height"]])
ax.set_xticklabels(["Rowing","Gymnastics"])
ax.set_ylabel("Height (cm)")