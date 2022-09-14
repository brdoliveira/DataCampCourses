import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv("./data/seattle_weather.csv",index_col=0)
austin_weather = pd.read_csv("./data/austin_weather.csv",index_col=0)

fig,ax = plt.subplots(2,1,sharey=True)

# seattle_weather
ax[0].plot(seattle_weather["MONTH"],
	seattle_weather["MLY-PRCP-NORMAL"],
	color='b')
ax[0].set_ylabel("Precipitation (inhces)")

ax[0].plot(seattle_weather["MONTH"],
		seattle_weather["MLY-PRCP-25PCTL"],
		linestyle='--',
		color='b')

ax[0].plot(seattle_weather["MONTH"],
		seattle_weather["MLY-PRCP-75PCTL"],
		linestyle='--',
		color='b')

# austin_weather
ax[1].plot(austin_weather["MONTH"],
	austin_weather["MLY-PRCP-NORMAL"],
	color='b')
ax[1].set_xlabel("Time (months)")
ax[1].set_ylabel("Precipitation (inhces)")

ax[1].plot(austin_weather["MONTH"],
		austin_weather["MLY-PRCP-25PCTL"],
		linestyle='--',
		color='b')

ax[1].plot(austin_weather["MONTH"],
		austin_weather["MLY-PRCP-75PCTL"],
		linestyle='--',
		color='b')
plt.show()
