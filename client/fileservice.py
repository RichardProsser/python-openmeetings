"""
Generated Python API code, for FileService
"""

from . import call

def importFile(SID, externalUserId, externalFileId, externalType, room_id, isOwner, path, parentFolderId, fileSystemName):

    """
    Import file from external source
     
     to upload a file to a room-drive you specify: externalUserId, user if of
     openmeetings user for which we upload the file room_id = openmeetings
     room id isOwner = 0 parentFolderId = 0
     
     to upload a file to a private-drive you specify: externalUserId, user if
     of openmeetings user for which we upload the file room_id = openmeetings
     room id isOwner = 1 parentFolderId = -2
    
    Return Type: org.apache.openmeetings.util.process.FileImportError[]
    
    # Parameters:
    String
    SID
    The logged in session id with minimum webservice level
    
    String
    externalUserId
    the external user id => If the file should goto a private
                section of any user, this number needs to be set
    
    Long
    externalFileId
    the external file-type to identify the file later
    
    String
    externalType
    the name of the external system
    
    Long
    room_id
    the room Id, if the file goes to the private folder of an
                user, you can set a random number here
    
    boolean
    isOwner
    specify a 1/true AND parentFolderId==-2 to make the file goto
                the private section
    
    String
    path
    http-path where we can grab the file from, the file has to be
                accessible from the OpenMeetings server
    
    Long
    parentFolderId
    specify a parentFolderId==-2 AND isOwner == 1/true AND to make
                the file goto the private section
    
    String
    fileSystemName
    the filename => Important WITH file extension!
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/importFile?SID=VALUE&externalUserId=VALUE&externalFileId=VALUE&externalType=VALUE&room_id=VALUE&isOwner=VALUE&path=VALUE&parentFolderId=VALUE&fileSystemName=VALUE
    
    """
    return call("importFile", SID, externalUserId, externalFileId, externalType, room_id, isOwner, path, parentFolderId, fileSystemName)
    
def importFileByInternalUserId(SID, internalUserId, externalFileId, externalType, room_id, isOwner, path, parentFolderId, fileSystemName):

    """
    Import file from external source
     
     to upload a file to a room-drive you specify: internalUserId, user if of
     openmeetings user for which we upload the file room_id = openmeetings
     room id isOwner = 0 parentFolderId = 0
     
     to upload a file to a private-drive you specify: internalUserId, user if
     of openmeetings user for which we upload the file room_id = openmeetings
     room id isOwner = 1 parentFolderId = -2
    
    Return Type: org.apache.openmeetings.util.process.FileImportError[]
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    internalUserId
    the openmeetings user id => If the file should goto a private
                section of any user, this number needs to be se
    
    Long
    externalFileId
    the external file-type to identify the file later
    
    String
    externalType
    the name of the external system
    
    Long
    room_id
    the room Id, if the file goes to the private folder of an
                user, you can set a random number here
    
    boolean
    isOwner
    specify a 1/true AND parentFolderId==-2 to make the file goto
                the private section
    
    String
    path
    http-path where we can grab the file from, the file has to be
                accessible from the OpenMeetings server
    
    Long
    parentFolderId
    specify a parentFolderId==-2 AND isOwner == 1/true AND to make
                the file goto the private section
    
    String
    fileSystemName
    the filename => Important WITH file extension!
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/importFileByInternalUserId?SID=VALUE&internalUserId=VALUE&externalFileId=VALUE&externalType=VALUE&room_id=VALUE&isOwner=VALUE&path=VALUE&parentFolderId=VALUE&fileSystemName=VALUE
    
    """
    return call("importFileByInternalUserId", SID, internalUserId, externalFileId, externalType, room_id, isOwner, path, parentFolderId, fileSystemName)
    
def addFolderByExternalUserIdAndType(SID, externalUserId, parentFileExplorerItemId, folderName, room_id, isOwner, externalFilesid, externalType):

    """
    to add a folder to the private drive, set parentFileExplorerItemId = 0
     and isOwner to 1/true and externalUserId/externalUserType to a valid user
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    String
    externalUserId
    the external file-type to identify the file later
    
    Long
    parentFileExplorerItemId
    
    
    String
    folderName
    the name of the folder
    
    Long
    room_id
    the room Id, if the file goes to the private folder of an
                user, you can set a random number here
    
    Boolean
    isOwner
    specify a 1/true AND parentFolderId==-2 to make the file goto
                the private section
    
    Long
    externalFilesid
    the external file-type to identify the file later
    
    String
    externalType
    the name of the external system
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/addFolderByExternalUserIdAndType?SID=VALUE&externalUserId=VALUE&parentFileExplorerItemId=VALUE&folderName=VALUE&room_id=VALUE&isOwner=VALUE&externalFilesid=VALUE&externalType=VALUE
    
    """
    return call("addFolderByExternalUserIdAndType", SID, externalUserId, parentFileExplorerItemId, folderName, room_id, isOwner, externalFilesid, externalType)
    
def addFolderByUserId(SID, userId, parentFileExplorerItemId, folderName, room_id, isOwner, externalFilesid, externalType):

    """
    to add a folder to the private drive, set parentFileExplorerItemId = 0
     and isOwner to 1/true and userId to a valid user
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    userId
    the openmeetings user id
    
    Long
    parentFileExplorerItemId
    specify a parentFolderId==-2 AND isOwner == 1/true AND to make the file goto the private section
    
    String
    folderName
    the name of the folder
    
    Long
    room_id
    the room Id, if the file goes to the private folder of an user, you can set a random number here
    
    Boolean
    isOwner
    specify a 1/true AND parentFolderId==-2 to make the file goto the private section
    
    Long
    externalFilesid
    the external file-type to identify the file later
    
    String
    externalType
    the name of the external system
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/addFolderByUserId?SID=VALUE&userId=VALUE&parentFileExplorerItemId=VALUE&folderName=VALUE&room_id=VALUE&isOwner=VALUE&externalFilesid=VALUE&externalType=VALUE
    
    """
    return call("addFolderByUserId", SID, userId, parentFileExplorerItemId, folderName, room_id, isOwner, externalFilesid, externalType)
    
def addFolderSelf(SID, parentFileExplorerItemId, fileName, room_id, isOwner):

    """
    Add a folder by the current user - similar to RTMP Call
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    parentFileExplorerItemId
    parent folder id
    
    String
    fileName
    the file name
    
    Long
    room_id
    the room id
    
    Boolean
    isOwner
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/addFolderSelf?SID=VALUE&parentFileExplorerItemId=VALUE&fileName=VALUE&room_id=VALUE&isOwner=VALUE
    
    """
    return call("addFolderSelf", SID, parentFileExplorerItemId, fileName, room_id, isOwner)
    
def deleteFileOrFolderByExternalIdAndType(SID, externalFilesid, externalType):

    """
    deletes a file by its external Id and type
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    externalFilesid
    the od of the file or folder
    
    String
    externalType
    the externalType
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/deleteFileOrFolderByExternalIdAndType?SID=VALUE&externalFilesid=VALUE&externalType=VALUE
    
    """
    return call("deleteFileOrFolderByExternalIdAndType", SID, externalFilesid, externalType)
    
def deleteFileOrFolder(SID, fileExplorerItemId):

    """
    deletes files or folders based on it id
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    fileExplorerItemId
    the id of the file or folder
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/deleteFileOrFolder?SID=VALUE&fileExplorerItemId=VALUE
    
    """
    return call("deleteFileOrFolder", SID, fileExplorerItemId)
    
def deleteFileOrFolderSelf(SID, fileExplorerItemId):

    """
    deletes files or folders based on it id
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    fileExplorerItemId
    the id of the file or folder
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/deleteFileOrFolderSelf?SID=VALUE&fileExplorerItemId=VALUE
    
    """
    return call("deleteFileOrFolderSelf", SID, fileExplorerItemId)
    
def getImportFileExtensions():

    """
    Get available import File Extension allowed during import
    
    Return Type: java.lang.String[]
    
    # Parameters:
    No Params
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/getImportFileExtensions
    
    """
    return call("getImportFileExtensions")
    
def getPresentationPreviewFileExplorer(SID, parentFolder):

    """
    Get a LibraryPresentation-Object for a certain file
    
    Return Type: org.apache.openmeetings.db.dto.file.LibraryPresentation
    
    # Parameters:
    String
    SID
    
    
    String
    parentFolder
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/getPresentationPreviewFileExplorer?SID=VALUE&parentFolder=VALUE
    
    """
    return call("getPresentationPreviewFileExplorer", SID, parentFolder)
    
def getFileExplorerByRoom(SID, room_id, owner_id):

    """
    Get a File Explorer Object by a given Room and owner id
    
    Return Type: org.apache.openmeetings.db.dto.file.FileExplorerObject
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    room_id
    Room id
    
    Long
    owner_id
    Owner id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/getFileExplorerByRoom?SID=VALUE&room_id=VALUE&owner_id=VALUE
    
    """
    return call("getFileExplorerByRoom", SID, room_id, owner_id)
    
def getFileExplorerByRoomSelf(SID, room_id):

    """
    Get a File Explorer Object by a given Room
    
    Return Type: org.apache.openmeetings.db.dto.file.FileExplorerObject
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    room_id
    Room Id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/getFileExplorerByRoomSelf?SID=VALUE&room_id=VALUE
    
    """
    return call("getFileExplorerByRoomSelf", SID, room_id)
    
def getFileExplorerByParent(SID, parentFileExplorerItemId, room_id, isOwner, owner_id):

    """
    Get FileExplorerItem list by parent folder
    
    Return Type: org.apache.openmeetings.db.entity.file.FileExplorerItem[]
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as logged in
    
    Long
    parentFileExplorerItemId
    the parent folder id
    
    Long
    room_id
    the room id
    
    Boolean
    isOwner
    true if its a private drive
    
    Long
    owner_id
    the owner id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/getFileExplorerByParent?SID=VALUE&parentFileExplorerItemId=VALUE&room_id=VALUE&isOwner=VALUE&owner_id=VALUE
    
    """
    return call("getFileExplorerByParent", SID, parentFileExplorerItemId, room_id, isOwner, owner_id)
    
def getFileExplorerByParentSelf(SID, parentFileExplorerItemId, room_id, isOwner):

    """
    Get FileExplorerItem[] by parent and owner id
    
    Return Type: org.apache.openmeetings.db.entity.file.FileExplorerItem[]
    
    # Parameters:
    String
    SID
    SID The SID of the User. This SID must be marked as logged in
    
    Long
    parentFileExplorerItemId
    the parent folder id
    
    Long
    room_id
    the room id
    
    Boolean
    isOwner
    true to request private drive
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/getFileExplorerByParentSelf?SID=VALUE&parentFileExplorerItemId=VALUE&room_id=VALUE&isOwner=VALUE
    
    """
    return call("getFileExplorerByParentSelf", SID, parentFileExplorerItemId, room_id, isOwner)
    
def updateFileOrFolderName(SID, fileExplorerItemId, fileName):

    """
    update a file or folder name
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    SID The SID of the User. This SID must be marked as logged in
    
    Long
    fileExplorerItemId
    file or folder id
    
    String
    fileName
    new file or folder name
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/updateFileOrFolderName?SID=VALUE&fileExplorerItemId=VALUE&fileName=VALUE
    
    """
    return call("updateFileOrFolderName", SID, fileExplorerItemId, fileName)
    
def updateFileOrFolderNameSelf(SID, fileExplorerItemId, fileName):

    """
    update a file or folder name
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    SID The SID of the User. This SID must be marked as logged in
    
    Long
    fileExplorerItemId
    file or folder id
    
    String
    fileName
    new file or folder name
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/updateFileOrFolderNameSelf?SID=VALUE&fileExplorerItemId=VALUE&fileName=VALUE
    
    """
    return call("updateFileOrFolderNameSelf", SID, fileExplorerItemId, fileName)
    
def moveFile(SID, fileExplorerItemId, newParentFileExplorerItemId, room_id, isOwner, moveToHome, owner_id):

    """
    move a file or folder
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    SID The SID of the User. This SID must be marked as logged in
    
    Long
    fileExplorerItemId
    current file or folder id to be moved
    
    Long
    newParentFileExplorerItemId
    new parent folder id
    
    Long
    room_id
    room id
    
    Boolean
    isOwner
    if true owner id will be set
    
    Boolean
    moveToHome
    if true move to private drive
    
    Long
    owner_id
    owner id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/moveFile?SID=VALUE&fileExplorerItemId=VALUE&newParentFileExplorerItemId=VALUE&room_id=VALUE&isOwner=VALUE&moveToHome=VALUE&owner_id=VALUE
    
    """
    return call("moveFile", SID, fileExplorerItemId, newParentFileExplorerItemId, room_id, isOwner, moveToHome, owner_id)
    
def moveFileSelf(SID, fileExplorerItemId, newParentFileExplorerItemId, room_id, isOwner, moveToHome):

    """
    move a file or folder
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    SID The SID of the User. This SID must be marked as logged in
    
    Long
    fileExplorerItemId
    current file or folder id to be moved
    
    Long
    newParentFileExplorerItemId
    new parent folder id
    
    Long
    room_id
    room id
    
    Boolean
    isOwner
    if true owner id will be set
    
    Boolean
    moveToHome
    move to private drive
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/FileService/moveFileSelf?SID=VALUE&fileExplorerItemId=VALUE&newParentFileExplorerItemId=VALUE&room_id=VALUE&isOwner=VALUE&moveToHome=VALUE
    
    """
    return call("moveFileSelf", SID, fileExplorerItemId, newParentFileExplorerItemId, room_id, isOwner, moveToHome)
    
