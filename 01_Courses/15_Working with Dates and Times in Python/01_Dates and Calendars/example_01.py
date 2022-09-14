# Import date
from datetime import date

# Create dates
two_hurricanes_dates = [date(2016,10,7), date(2017,6,21)]
# two_hurricanes = ["10/7/2016","6/21/2016"]
print(two_hurricanes_dates[0].year)
print(two_hurricanes_dates[0].month)
print(two_hurricanes_dates[0].day)

print(two_hurricanes_dates[0].weekday()) 
# 0 = monday
# 1 = tuesday
# ...
# 6 = sunday