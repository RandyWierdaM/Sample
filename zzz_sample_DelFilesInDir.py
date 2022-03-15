import os

delDir = r"G:\RECURRENT_PROJECTS\Planning\Land Use Map Book\temp"
fileList = os.listdir(delDir)

for f in fileList:
    filePath = os.path.join(delDir,f)
    if os.path.isfile(filePath):
        os.remove(filePath)
    else:
        print ("Error: %s file not found" % f)
    print filePath
