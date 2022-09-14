import matplotlib.pyplot as plt
import pandas as pd

mens_rowing = pd.read_csv("./data/mens_rowing",index_col=0)
mens_gymnastics = pd.read_csv("./data/mens_gymnastics",index_col=0)

fig,ax = plt.subplots()
ax.hist("Rowing",mens_rowing["Height"],
        bins=[range(150,210)],
        histtype="step")

ax.hist("Gymnastics",mens_gymnastics["Heigth"],
        bins=[range(150,210)],
        histtype="step")
ax.set_xlabel("Heigth (cm)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()