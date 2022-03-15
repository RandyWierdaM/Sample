import os
import re
import arcpy
import time
import datetime
from operator import itemgetter

mxdList = []
exList = [] #List to hold maps that need to be skipped in the process
tic = 0
folder = r"S:\Fire Services\Pre Incident Plans\PIP Files"

for root, dirs, files in os.walk(folder, topdown=True):
  dirs[:] = [d for d in dirs if d not in set([r"S:\Fire Services\Pre Incident Plans\PIP Files\zz_ArcGIS_Database\TrainingMapX001"])] #set is a list of directories to skip
  for name in files:
      ext = os.path.splitext(name)[1]
      filePath = (os.path.join(root, name))
      if ext == ".mxd" and filePath not in exList:
            mxdInfo = []
            mxdPath = (os.path.join(root, name))
            mxdTime = os.path.getmtime(mxdPath)
            mxdInfo.append(mxdPath)
            mxdInfo.append(mxdTime)
            mxdList.append(mxdInfo)
            tic = tic + 1


#sort by timestamps of last saved in desending order
mxdList.sort(key=itemgetter(1),reverse=True)

completion = 0
for m in mxdList:
  if m[1] > 1571243730: #timestamp on Oct 22, 2019
    mxd = arcpy.mapping.MapDocument(m[0])
    brokenLayers = arcpy.mapping.ListBrokenDataSources(mxd)
    if not brokenLayers:
      print "Not broken: " + (m[0]).split("\\")[-1] + "; " + str(m[1])
      del (mxd)
    else:
      print "Broken: " + (m[0]).split("\\")[-1]
      os.startfile(m[0])
      del (mxd)
      time.sleep(60)
  else:
    completion = completion + 1
    print "Already done: " + (m[0]).split("\\")[-1] + "; " + str(completion) + " of " + str(tic)
    
                   

print tic
                                             
