from datetime import datetime

dt = datetime(2017,10,1,15,23,25) # October 1 2017, 3:23:25 PM 
dt = datetime(2017,10,1,15,23,25,50000) # Add microseconds

dt_hr = dt.replace(minute=0,second=0,microsecond=0)
print(dt_hr)