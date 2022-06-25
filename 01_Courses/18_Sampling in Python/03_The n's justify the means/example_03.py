"""
# Be our guess,put our sample to the test

dice = expand_grid(
    {
        'die1':[1,2,3,4,5,6],
        'die2':[1,2,3,4,5,6],
        'die3':[1,2,3,4,5,6],
        'die4':[1,2,3,4,5,6]
    }
)

dice['mean_roll'] = (dice['die1'] + dice['die2'] + dice['die3'] + dice['die4']) / 4
print(dice) 

# Exact sampling distribution
dice['mean_roll'] = dice['mean_roll'].astype('category')
dice['mean_roll'].value_counts(sort=False).plot(kind="bar")

# The number of outcomes increases fast
n_dice = list(range(1,101))
n_outcomes = []

for n in n_dice:
    n_outcomes.append(6**n)

outcomes = pd.DataFrame(
    {"n_dice": n_dice,
     "n_outcomes": n_outcomes})

outcomes.plot(x="n_dice",
              y="n_outcomes",
              kind="scatter")
plt.show()

# Simulating the mean of four dice rolls
import numpy as np

sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(
        np.random.choice(list(range(1,7)), size=4, replace=True).mean()
    )
print(sample_means_1000)

# Approximate sampling distribution
plt.hist(sample_means_1000,bins=20)
plt.show()


"""