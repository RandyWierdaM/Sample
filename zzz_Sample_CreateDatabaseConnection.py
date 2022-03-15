import arcpy
import os
import tempfile
import shutil


#Connection Parameters
instance = 'prodsql01\gissql01'
databaseName = 'SGMaster'
versionName = 'sde.Default'
ConnectionFile = 'ConnectionFile.sde'
AuthType = 'OPERATING_SYSTEM_AUTH'
userName = '#'
userPassword = '#'


#Create a temp directory using tempfile module to store SDE connection files
sdeTempPath = tempfile.mkdtemp()
ConnectionFilePth = os.path.join(sdeTempPath,ConnectionFile)

#Setup SDE Connection
arcpy.CreateDatabaseConnection_management(sdeTempPath,ConnectionFile,'SQL_SERVER',instance,AuthType,userName, userPassword, '#',databaseName,'#','#', versionName)




#test the connection

try:
    workspace = ConnectionFilePth
    walk = arcpy.da.Walk(workspace, datatype=["FeatureClass","Table"])
    for dirpath, dirnames, filenames in walk:
        for filename in filenames:
            print filename

#Cleanup
    shutil.rmtree(sdeTempPath)
except:
    ##When done, Remove the temp path containing connection files
    shutil.rmtree(sdeTempPath)

