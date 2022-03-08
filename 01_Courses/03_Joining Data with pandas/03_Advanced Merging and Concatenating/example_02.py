# Concatenate DataFrames together vertically

# pandas .concat() method can concatenate both vertical an horizontal
# axis=0, vertical (is default)


# # Basic concatenation
# inv_jan (top)
# inv_feb (middle)
# inv_mar (bottom)

pd.concat([inv_jan,inv_feb,inv_mar])

# Ignoring the index
pd.concat([inv_jan,inv_feb,inv_mar],
        ignore_index=True)

# Setting labels to original tables
pd.concat([inv_jan,inv_feb,inv_mar],
        ignore_index=False,
        keys=['jan','feb','mar'])

# Concatenate tables with different column names
pd.concat([inv_jan,inv_feb], sort=True)

pd.concat([inv_jan,inv_feb],
        join='inner')

# Append the tables
inv_jan.append([inv_feb,inv_mar],
            ignore_index=True,
            sort=True)