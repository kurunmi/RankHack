#!/usr/bin/python3
import datetime
mytime = '02:01:00PM'
newtime = datetime.datetime.strptime(mytime, "%I:%M:%S%p")
print(mytime)
print(newtime.strftime("%H:%M:%S"))
#finaltime = newtime.strftime("%H:M:S")

