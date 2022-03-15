import os
import arcpy
import time
import datetime

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
            mxdPath = (os.path.join(root, name))
            mxdList.append(mxdPath)
            lastSave = ("%s" % time.ctime(os.path.getmtime(mxdPath)))
            #print(lastSave + " " + name)
            tic = tic + 1


for m in mxdList:
    print m.split("\\")[-1]
print tic
                                             
