import pandas as pd
import matplotlib.pyplot as plt

climate_change = pd.read_csv("./data/climate_change.csv",index_col=0)
print(climate_change.index)

sixties = climate_change["1960-01-01":"1969-12-31"]

# Zooming in on a decade
# # climate_change[["relative_temp","co2"]]
fig , ax = plt.subplots()
ax.plot(sixties.index, sixties['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

# Zooming in on a year
sixty_nine = climate_change['1969-01-01":"1969-12-31']
fig , ax = plt.subplots()
ax.plot(sixty_nine.index, sixty_nine['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()