from datetime import datetime,timezone,timedelta

spring_ahead_159am = datetime(2017,3,12,1,59,59)
spring_ahead_159am.isoformat()

spring_ahead_3am = datetime(2017,3,12,3,0,0)
spring_ahead_3am.isoformat()


(spring_ahead_3am-spring_ahead_159am).total_seconds()

# Start of Daylight Saving Time
EST = timezone(timedelta(hours=-5))
EDT = timezone(timedelta(hours=-4))

spring_ahead_159am = spring_ahead_159am.replace(tzinfo=EST)
spring_ahead_159am.isoformat()

spring_ahead_3am = spring_ahead_3am.replace(tzinfo=EDT)
spring_ahead_3am.isoformat()

(spring_ahead_3am-spring_ahead_159am).total_seconds()

# Import tz
from dateutil import tz

eastern = tz.gettz('America/New_York')

# 2017-03-12 1:59:59 in Eastern Time (EST)
spring_ahead_159am = datetime(2017,3,12,1,59,59,tzinfo=eastern)

# 2017-03-12 03:00:00 in Eastern Time (EDT)
spring_ahead_3am = datetime(2017,3,12,3,0,0,tzinfo=eastern)