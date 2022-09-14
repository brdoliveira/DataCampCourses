# Lets us compare between two strings
from fuzzywuzzy import fuzz,process
import pandas as pd

# Compare reeding vs reading
fuzz.WRatio('Reeding','Reading')

# Partial string comparison
fuzz.WRatio('Houston','Rockets')

# Parital string comparison with different order
fuzz.WRatio('Houston Rockets vc Los Angeles Lakers','Lakers vs Rockets')

string = "Houston Rockets vs Los Angeles Lakers"
choices = pd.Series(['Rockets vs Lakers','Lakers vs Rockets','Houson vs Los Angeles','Heat vs Bulls'])
process.extract(string,choices,limit=2)

survey = pd.read_csv('./data/survey.csv')
print(survey['state'].unique())

categories = pd.read_csv('./data/categories.csv')

# For each correct category
for state in categories['state']:
    # Find potential matches in states with typoes
    matches = process.extract(state,survey['state'],limit=survey.shape[0])
    # For each potential match match
    for potential_match in matches:
        # If high similarity score
        if potential_match[1] >= 80:
            # Replace typo with correct category
            survey.loc[survey['state'] == potential_match[0],'state'] = state