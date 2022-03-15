import datetime
import time

currentTime = datetime.datetime.now()
dateString = currentTime.strftime('%Y%m%d')# %H:%M:%S')
dateStringDash = currentTime.strftime('%Y-%m-%d')# %H:%M:%S')
dateStringAltalis = currentTime.strftime('%Y_%B_%d')# %H:%M:%S')
secondsSinceEpoch = time.time() - 604800



print(currentTime)
print (dateString)
print (dateStringAltalis)
print (secondsSinceEpoch)
