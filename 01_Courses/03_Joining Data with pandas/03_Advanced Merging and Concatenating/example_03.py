import pandas as pd
# Verifying integrity

tracks.merge(specs, on='tid', 
            validate='one_to_one') # its not one_to_one

albums.merge(tracks,on='aid',
            validate='one_to_many')

pd.concat([inv_feb,inv_mar],
        verify_integrity=True) # check the index, dont check the columns

pd.concat([inv_feb,inv_mar],
        verify_integrity=False)