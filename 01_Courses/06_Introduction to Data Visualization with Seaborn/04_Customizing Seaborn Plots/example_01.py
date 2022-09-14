import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

masculinity_data = pd.read_csv("./data/masculinity_data.csv")

# changing the bakcground, preset options:
# "white","dark","whitegrid","darkgrid","ticks"
sns.set_style("whitegrid")

# changing the palette
# sns.set_palette"("Rdbu") # see the website seaborn 

sns.catplot(x="age",
            y="masculinity_important",
            data=masculinity_data,
            hue="feel_masculine",
            kind="point")
plt.show()

## Example (changing the palette)
custom_palette = ['#FBB4AE','#B3CDE3','#CCEBC5',
                '#DECBE4','#FED9A6','#FFFFCC',
                '#E5D8BD',"#FDDAEC","#F2F2F2"]
sns.set_palette(custom_palette)
# sns.set_palette("RdBu") # or changing the default palette

category_order = ["No answer",
                "Not at all",
                "Not very",
                "Somewhat",
                "Very"]

# changing the scale
# "paper","notebook","talk","poster" ("paper" is default)
sns.set_context("talk")

sns.catplot(x="how_masculine",
            data=masculinity_data,
            kind="count",
            order=category_order)