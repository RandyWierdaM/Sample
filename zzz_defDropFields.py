import arcpy

featureClass = "Database Connections\OSA_SGMaster.sde\SGMaster.SDE.Address\SGMaster.SDE.SiteAddress"
keepFields = ["PARCELID"]
dropFields = []

def dropFieldsFunc(fc, kf, df):
    #fc is file path to dataset
    #kf is list of field names that are to be kept
    #df is list of field names to be dropped, usually empty
    #editor tracking can cause the function to fail
    allFields = arcpy.ListFields(fc)
    for a in allFields: #Add any required fields to the keep list
        if a.required == True:
            kf.append(a.name)
    for a in allFields: #expand drop fields list 
        if a.name not in kf:
            df.append(a.name)
    return 


dropFieldsFunc(featureClass,keepFields,dropFields)

print dropFields
