import arcpy
import os
import tempfile
import shutil
import traceback


#Connection Parameters
instance = 'LOCALHOST\westlockgis'
databaseName = 'ToWInterim'
versionName = 'DBO.Editing'
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
    #loop to find all unique values of field names.
    #to find what fields may be holding editing information
    for dirpath, dirnames, filenames in walk:
        for filename in filenames:
            #print('^^^^^^^^^^^^^^^^^^^^^^^^')
            #print filename
            editorList = []
            fc = os.path.join(dirpath, filename)
            fields = arcpy.ListFields(fc)            
            for field in fields:
                #print field.name
                if field.name in ("LASTEDITOR"):#,"LastEditor"):
                    arcpy.DisableEditorTracking_management(fc)
                    edit = arcpy.da.Editor(workspace)
                    edit.startEditing()
                    edit.startOperation                   
                    print('^^^^^^^^^^^^^^^^^^^^^^^^')
                    print filename
                    with arcpy.da.UpdateCursor(fc, ["LASTEDITOR","created_user","last_edited_user"]) as cursor:
                        for row in cursor:
                            if row[0] in ['beth','Beth','BTHOLA','Bt','BT','bt hydrant','gas valve possible']:
                                row[0] = 'bt'
                            elif row[0] == None:
                                row[0] = 'unk'
                            else:
                                pass
                            cursor.updateRow(row)
                            if row[0] not in editorList:
                                editorList.append(row[0])
                    edit.stopOperation()
                    edit.stopEditing(True)
                    del edit
                    print(editorList)
                    arcpy.EnableEditorTracking_management(fc,"created_user","created_date","last_edited_user","last_edited_date")
                    
                                               
                    
            

#Cleanup
    shutil.rmtree(sdeTempPath)
except Exception:
    traceback.print_exc()
    ##When done, Remove the temp path containing connection files
    shutil.rmtree(sdeTempPath)

