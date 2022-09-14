import seaborn as sns
import matplotlib.pyplot as plt


height =  [62,64,69,75,66,68,65,71,76,73]
weight = [120,136,148,175,137,165,154,172,200,187]
sns.scatterplot(x=height,y=weight)
plt.show()

gender = ["Female","Female",
          "Female","Female",
          "Male","Male","Male",
          "Male","Male","Male"]
sns.countplot(x=gender)
plt.show()