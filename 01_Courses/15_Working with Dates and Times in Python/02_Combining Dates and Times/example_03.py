from calendar import week
from datetime import datetime,timedelta

# Create example datetimes
start = datetime(2017,10,8,23,46,47)
end = datetime(2017,10,9,0,10,57)

# Subtract datetimes to create a timedelta
duration = end - start
print(duration.total_seconds())

# Create timedelta
delta1 = timedelta.duration(seconds=1)
delta2 = timedelta.duration(seconds=1,duration=1)
delta3 = timedelta.duration(week=-1)
delta4 = timedelta.duration(week=1)

# One second later
print(start + delta1)
print(start + delta2)
print(start + delta3)
print(delta4)
print(start + delta4)