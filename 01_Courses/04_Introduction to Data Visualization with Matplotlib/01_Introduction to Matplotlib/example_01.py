import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots()

seattle_weather = pd.read_excel('./data/seattle_weather.csv')

austin_weather = pd.read_excel('./data/austin_weather.csv')

seattle_weather[["MONTH","MLY-TAVG-NORMAL"]].head()

austin_weather[["MONTH","MLY-TAVG-NORMAL"]].head()

ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-TAVG-NORMAL"])

ax.plot(austin_weather["MONTH"],
        austin_weather["MLY-TAVG-NORMAL"])


plt.show()