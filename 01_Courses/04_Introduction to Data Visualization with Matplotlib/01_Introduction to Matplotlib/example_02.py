import pandas as pd

seattle_weather = pd.read_csv('./data/seattle_weather.csv',index_col=0)

ax.plot(seattle_weather["MONTH"],
	seattle_weather["MLY-PRCP-NORMAL"],
	marker="o") 
	
# marker="v" -> triangle
# linestyle="--" -> dashes
# linestyle="None" -> None line
# color = "r"

ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degress)")
ax.set_title("Weather in Seattle")

plt.show()
