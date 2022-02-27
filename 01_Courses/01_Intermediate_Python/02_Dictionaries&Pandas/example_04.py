import pandas as pd 

brics = pd.read_csv("data/brics.csv",index_col=0)

print(brics["country"]) # type is a Series (1D labelled array)
print("*" * 30)

print(brics[["country"]]) # type is a DataFrame
print("*" * 30)

brics[["country","capital"]] # sub DataFrame
print("*" * 30)

brics[1:4] # slice
print("*" * 30)

print(brics.loc["RU"]) # columns
print(brics.loc[["RU"]]) # labels
print("*" * 30)

print(brics.loc[["RU","IN","CH"]])
print(brics.loc[["RU","IN","CH"],
                ["country","capital"]]) # labels and columns
print(brics.loc[:,["country","capital"]])
print("*" * 30)

print(brics.loc[["RU"]])
print(brics.iloc[[1]]) # use index instead of name
print("*" * 30)

print(brics.iloc[[1,2,3],[0,1]])
print(brics.iloc[:,[0,1]]) # all labels
