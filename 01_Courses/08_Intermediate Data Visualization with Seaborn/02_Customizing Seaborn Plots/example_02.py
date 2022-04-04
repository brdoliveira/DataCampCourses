import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("wines.csv")

sns.set(color_code=True)
sns.distplot(df['Tuition'],color='g')

for p in sns.palettes.SEABORN_PALETTES:
    sns.set_palette(p)
    sns.palplot(sns.color_palette()) # Show the colors
    sns.distplot(df['Tuition'])

# Defining Custom Palettes
sns.palplot(sns.color_palette("Paired",12))
sns.palplot(sns.color_palette("Blues",12))
sns.palplot(sns.color_palette("BrBG",12))