from datetime import datetime

dt = datetime(2017,12,30,15,19,13)
print(dt.strftime("%Y-%m-%d"))
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.strftime("%H:%M:%S on %Y/%m/%d"))

# ISO 8601 format
print(dt.isoformat())

# Parsing datetimes with strptime
dt = datetime.strptime("12/20/2017 15:19:12","%m/%d/%Y %H:%M:%S")

# We did we make?
print(type(dt))

# Print out datetime object
print(dt)

# Incorrect format string
dt = datetime.strptime("12/20/2017 15:19:12","%Y-%m-%d")

# A timestamp
ts = 1514665153.0

# Convert to datetime and print
print(datetime.fromtimestamp(ts))