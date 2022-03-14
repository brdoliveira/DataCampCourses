import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot") # --> changing a style
# plt.use.style("default")
# plt.use.style("bmh")
# plt.use.style("seaborn-colorlind")

fig,ax = plt.subplots()

seattle_weather = pd.read_excel('./data/seattle_weather.csv')

austin_weather = pd.read_excel('./data/austin_weather.csv')

seattle_weather[["MONTH","MLY-TAVG-NORMAL"]].head()

austin_weather[["MONTH","MLY-TAVG-NORMAL"]].head()

ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-TAVG-NORMAL"])

ax.plot(austin_weather["MONTH"],
        austin_weather["MLY-TAVG-NORMAL"])

ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degress)")

plt.show()

# Dark backgrounds are generally discouraged as they are less visible, so only use them if you have a good reason to do so.
# If colors are important, consider using a colorblind-friendly style, such as "seaborn-colorblind" or "tableau-colorblind10".
# These are designed to retain color differences even when viewed by colorblind individuals. 
# That might sound like a minor consideration, but approximately 1 out of 20 individuals is colorblind.
# Figures that are designed for use on websites have different considerations than figures in printed reports. 
# For example, if someone is going to print out your figures, you might want to use less ink. That is, avoid colored backgrounds,
# like the background that appears in the "ggplot" style that we demonstrated before. If the printer used is likely to be 
# black-and-white, consider using the "grayscale" style. This will retain the differences you see on your screen when 
# printed out in a black-and-white printer.