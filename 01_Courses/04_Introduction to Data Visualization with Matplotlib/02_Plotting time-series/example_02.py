from pydoc import cli
from turtle import color
import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('climate_change.csv',
                            parse_dates=["date"],
                            index_col="date")

print(climate_change.head())

fig , ax = plt.subplots()
ax.plot(climate_change.index,
        climate_change["co2"],
        color='blue')
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)',
                color='blue')
ax.tick_params('y',color='blue') # y values blue

ax2 = ax.twinx()
ax.plot(climate_change.index,
        climate_change["relative_temp"],
        color='red')
ax2.set_ylabel('Relative temperature (Celsius)',
                color='red')
ax.tick_params('y',color='red') # y values red

plt.show()

def plot_timeseries(axes,x,y,color,xlabel,ylabel):
    axes.plot(x,y,color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel,color=color)
    axes.tick_params('y',colors=color)