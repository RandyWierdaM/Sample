import arcpy
import os

def firstObjectID(featureClass):
    iterator = 0
    cursor = arcpy.SearchCursor(featureClass,["OID@"])
    idField = (arcpy.ListFields(featureClass,"","OID")[0].name).encode('ascii', 'ignore')
    firstRecord = -1
    for row in cursor:        
        firstRecord = row.getValue(idField)
        iterator = iterator +1
        if iterator > 0:
            break
    return(idField,firstRecord)
        
    

    
#Testing of the def
#Set workspace environment to geodatabase
workspace = r"C:\Users\rwierda\AppData\Roaming\ESRI\Desktop10.6\ArcCatalog\SGMaster.sde"
scratch = r"G:\WORKING\Randy\Scratch\Scratch.gdb"
fc = os.path.join(workspace,"SGMaster.SDE.swManhole")
moveLayer = "moveLayer"
SQLInfo = firstObjectID(fc)

sql = '"' + SQLInfo[0] + '" = ' + str(SQLInfo[1])
print sql
inFeatures = arcpy.MakeFeatureLayer_management(fc,moveLayer,sql)
outFeatures = os.path.join(scratch,"testMove")
arcpy.CopyFeatures_management(inFeatures,outFeatures)














##walk = arcpy.da.Walk(workspace, datatype=["FeatureClass"])
##
##for dirpath, dirnames, filenames in walk:
##    for filename in filenames:
##        fc = os.path.join(dirpath, filename)
##        print filename + " " +  str(firstObjectID(fc)[0]) + " " + str(firstObjectID(fc)[1])

                
