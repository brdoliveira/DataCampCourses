import pandas as pd



dogs = pd.read_csv("./data/dogs.csv",index_col=0)

print(dogs)

dogs.head() # Return first five lines

dogs.info() # The info method displays the names of columns, the data types they 
# contain, and whether they have any missing values.

dogs.shape # returns the number of rows and columns of the DataFrame

dogs.describe() # calculates a few summary statistics for each column.

dogs.values # A two-dimensional NumPy array of values.

dogs.columns # An index of columns: the column names.

dogs.index # An index for the rows: either row numbers or row names.


