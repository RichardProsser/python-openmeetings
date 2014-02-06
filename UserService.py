"""
Generated Python API code, for UserService
"""

from . import call

def getSession():

    """
    load this session id before doing anything else Returns an Object of Type
     Sessiondata, this contains a sessionId, use that sessionId in all Methods
    
    Return Type: org.apache.openmeetings.db.entity.server.Sessiondata
    
    # Parameters:
    No Params
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/getSession
    
    """
    return call("getSession")
    
def loginUser(SID, username, userpass):

    """
    Auth function, use the SID you get by getSession, return positive means
     logged-in, if negative its an ErrorCode, you have to invoke the Method
     getErrorByCode to get the Text-Description of that ErrorCode
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    - The SID from getSession
    
    String
    username
    - Username from OpenMeetings, the user has to have Admin-rights
    
    String
    userpass
    - Userpass from OpenMeetings
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/loginUser?SID=VALUE&username=VALUE&userpass=VALUE
    
    """
    return call("loginUser", SID, username, userpass)
    
def getErrorByCode(SID, errorid, langId):

    """
    loads an Error-Object. If a Method returns a negative Result, its an
     Error-id, it needs a language_id to specify in which language you want to
     display/read the error-message. English has the Language-ID one, for
     different one see the list of languages
    
    Return Type: org.apache.openmeetings.db.dto.basic.ErrorResult
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    long
    errorid
    the error id (negative Value here!)
    
    long
    langId
    The id of the language
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/getErrorByCode?SID=VALUE&errorid=VALUE&langId=VALUE
    
    """
    return call("getErrorByCode", SID, errorid, langId)
    
def addNewUser(SID, username, userpass, lastname, firstname, email, additionalname, street, zip, fax, states_id, town, language_id, baseURL):

    """
    Adds a new Usre like through the Frontend, but also does activates the
     Account To do SSO see the methods to create a hash and use those ones!
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    userpass
    any userpass
    
    String
    lastname
    any lastname
    
    String
    firstname
    any firstname
    
    String
    email
    any email
    
    String
    additionalname
    any additionalname
    
    String
    street
    any street
    
    String
    zip
    any zip
    
    String
    fax
    any fax
    
    long
    states_id
    a valid states_id
    
    String
    town
    any town
    
    long
    language_id
    the language_id
    
    String
    baseURL
    the baseURL is needed to send the Initial Email correctly to
                that User, otherwise the Link in the EMail that the new User
                will reveive is not valid
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/addNewUser?SID=VALUE&username=VALUE&userpass=VALUE&lastname=VALUE&firstname=VALUE&email=VALUE&additionalname=VALUE&street=VALUE&zip=VALUE&fax=VALUE&states_id=VALUE&town=VALUE&language_id=VALUE&baseURL=VALUE
    
    """
    return call("addNewUser", SID, username, userpass, lastname, firstname, email, additionalname, street, zip, fax, states_id, town, language_id, baseURL)
    
def addNewUserWithTimeZone(SID, username, userpass, lastname, firstname, email, additionalname, street, zip, fax, states_id, town, language_id, baseURL, jNameTimeZone):

    """
    Adds a new User like through the Frontend, but also does activates the
     Account
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    userpass
    any userpass
    
    String
    lastname
    any lastname
    
    String
    firstname
    any firstname
    
    String
    email
    any email
    
    String
    additionalname
    any additionalname
    
    String
    street
    any street
    
    String
    zip
    any zip
    
    String
    fax
    any fax
    
    long
    states_id
    a valid states_id
    
    String
    town
    any town
    
    long
    language_id
    the language_id
    
    String
    baseURL
    the baseURL is needed to send the Initial Email correctly to
                that User, otherwise the Link in the EMail that the new User
                will reveive is not valid
    
    String
    jNameTimeZone
    the name of the timezone for the user
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/addNewUserWithTimeZone?SID=VALUE&username=VALUE&userpass=VALUE&lastname=VALUE&firstname=VALUE&email=VALUE&additionalname=VALUE&street=VALUE&zip=VALUE&fax=VALUE&states_id=VALUE&town=VALUE&language_id=VALUE&baseURL=VALUE&jNameTimeZone=VALUE
    
    """
    return call("addNewUserWithTimeZone", SID, username, userpass, lastname, firstname, email, additionalname, street, zip, fax, states_id, town, language_id, baseURL, jNameTimeZone)
    
def addNewUserWithExternalType(SID, username, userpass, lastname, firstname, email, additionalname, street, zip, fax, states_id, town, language_id, jNameTimeZone, externalUserId, externalUserType):

    """
    Adds a new User like through the Frontend, but also does activates the
     Account, sends NO email (no matter what you configured) and sets the
     users external user id and type
     
     Use the methods to create a hash for SSO, creating users is not required
     for SSO
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    userpass
    any userpass
    
    String
    lastname
    any lastname
    
    String
    firstname
    any firstname
    
    String
    email
    any email
    
    String
    additionalname
    any additionalname
    
    String
    street
    any street
    
    String
    zip
    any zip
    
    String
    fax
    any fax
    
    long
    states_id
    a valid states_id
    
    String
    town
    any town
    
    long
    language_id
    the language_id
    
    String
    jNameTimeZone
    the name of the timezone for the user
    
    String
    externalUserId
    externalUserId
    
    String
    externalUserType
    externalUserType
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/addNewUserWithExternalType?SID=VALUE&username=VALUE&userpass=VALUE&lastname=VALUE&firstname=VALUE&email=VALUE&additionalname=VALUE&street=VALUE&zip=VALUE&fax=VALUE&states_id=VALUE&town=VALUE&language_id=VALUE&jNameTimeZone=VALUE&externalUserId=VALUE&externalUserType=VALUE
    
    """
    return call("addNewUserWithExternalType", SID, username, userpass, lastname, firstname, email, additionalname, street, zip, fax, states_id, town, language_id, jNameTimeZone, externalUserId, externalUserType)
    
def deleteUserById(SID, userId):

    """
    Delete a certain user by its id
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    Long
    userId
    the openmeetings user id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/deleteUserById?SID=VALUE&userId=VALUE
    
    """
    return call("deleteUserById", SID, userId)
    
def deleteUserByExternalUserIdAndType(SID, externalUserId, externalUserType):

    """
    Delete a certain user by its external user id
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    externalUserId
    externalUserId
    
    String
    externalUserType
    externalUserId
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/deleteUserByExternalUserIdAndType?SID=VALUE&externalUserId=VALUE&externalUserType=VALUE
    
    """
    return call("deleteUserByExternalUserIdAndType", SID, externalUserId, externalUserType)
    
def setUserObject(SID, username, firstname, lastname, profilePictureUrl, email):

    """
    deprecated use setUserObjectAndGenerateRoomHash
     
     Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID + a RoomId to enter any Room.
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any profilePictureUrl
    
    String
    email
    any email
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObject?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE
    
    """
    return call("setUserObject", SID, username, firstname, lastname, profilePictureUrl, email)
    
def setUserObjectWithExternalUser(SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType):

    """
    deprecated use setUserObjectAndGenerateRoomHash
     
     Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID + a RoomId to enter any Room.
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any profilePictureUrl
    
    String
    email
    any email
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObjectWithExternalUser?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE&externalUserId=VALUE&externalUserType=VALUE
    
    """
    return call("setUserObjectWithExternalUser", SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType)
    
def setUserObjectAndGenerateRoomHash(SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt):

    """
    Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID + a RoomId to enter any Room. ...
     Session-Hashs are deleted 15 minutes after the creation if not used.
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any profilePictureUrl
    
    String
    email
    any email
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    Long
    room_id
    the room id the user should be logged in
    
    int
    becomeModeratorAsInt
    0 means no Moderator, 1 means Moderator
    
    int
    showAudioVideoTestAsInt
    0 means don't show Audio/Video Test, 1 means show Audio/Video
                Test Application before the user is logged into the room
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObjectAndGenerateRoomHash?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE&externalUserId=VALUE&externalUserType=VALUE&room_id=VALUE&becomeModeratorAsInt=VALUE&showAudioVideoTestAsInt=VALUE
    
    """
    return call("setUserObjectAndGenerateRoomHash", SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt)
    
def setUserObjectAndGenerateRoomHashByURL(SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt):

    """
    Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID + a RoomId to enter any Room.
     
     ++ the user can press f5 to reload the page / use the link several times,
     the SOAP Gateway does remember the IP of the user and the will only the
     first user that enters the room allow to re-enter. ... Session-Hashs are
     deleted 15 minutes after the creation if not used.
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any profilePictureUrl
    
    String
    email
    any email any email
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    Long
    room_id
    the room id the user should be logged in
    
    int
    becomeModeratorAsInt
    0 means no Moderator, 1 means Moderator
    
    int
    showAudioVideoTestAsInt
    0 means don't show Audio/Video Test, 1 means show Audio/Video
                Test Application before the user is logged into the room
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObjectAndGenerateRoomHashByURL?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE&externalUserId=VALUE&externalUserType=VALUE&room_id=VALUE&becomeModeratorAsInt=VALUE&showAudioVideoTestAsInt=VALUE
    
    """
    return call("setUserObjectAndGenerateRoomHashByURL", SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt)
    
def setUserObjectAndGenerateRoomHashByURLAndRecFlag(SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt, allowRecording):

    """
    Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID + a RoomId to enter any Room.
     
     ++ the user can press f5 to reload the page / use the link several times,
     the SOAP Gateway does remember the IP of the user and the will only the
     first user that enters the room allow to re-enter. ... Session-Hashs are
     deleted 15 minutes after the creation if not used.
     
     ++ sets the flag if the user can do recording in the conference room
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any profilePictureUrl
    
    String
    email
    any email
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    Long
    room_id
    the room id the user should be logged in
    
    int
    becomeModeratorAsInt
    0 means no Moderator, 1 means Moderator
    
    int
    showAudioVideoTestAsInt
    0 means don't show Audio/Video Test, 1 means show Audio/Video
                Test Application before the user is logged into the room
    
    int
    allowRecording
    0 means don't allow Recording, 1 means allow Recording
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObjectAndGenerateRoomHashByURLAndRecFlag?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE&externalUserId=VALUE&externalUserType=VALUE&room_id=VALUE&becomeModeratorAsInt=VALUE&showAudioVideoTestAsInt=VALUE&allowRecording=VALUE
    
    """
    return call("setUserObjectAndGenerateRoomHashByURLAndRecFlag", SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt, allowRecording)
    
def setUserObjectMainLandingZone(SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType):

    """
    Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID and directly login into the dashboard
     
     ++ the user can press f5 to reload the page / use the link several times,
     the SOAP Gateway does remember the IP of the user and the will only the
     first user that enters the room allow to re-enter. ... Session-Hashs are
     deleted 15 minutes after the creation if not used.
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any absolute profilePictureUrl
    
    String
    email
    any email
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObjectMainLandingZone?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE&externalUserId=VALUE&externalUserType=VALUE
    
    """
    return call("setUserObjectMainLandingZone", SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType)
    
def setUserAndNickName(SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt, showNickNameDialogAsInt):

    """
    Description: sets the SessionObject for a certain SID, after setting this
     Session-Object you can use the SID + a RoomId to enter any Room.
     
     ++ the user can press f5 to reload the page / use the link several times,
     the SOAP Gateway does remember the IP of the user and the will only the
     first user that enters the room allow to re-enter. ... Session-Hashs are
     deleted 15 minutes after the creation if not used.
     
     ++ Additionally you can set a param showNickNameDialogAsInt, the effect
     if that param is 1 is, that the user gets a popup where he can enter his
     nickname right before he enters the conference room. All nicknames and
     emails users enter are logged in the conferencelog table.
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    profilePictureUrl
    any profilePictureUrl
    
    String
    email
    any email
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    Long
    room_id
    the room id the user should be logged in
    
    int
    becomeModeratorAsInt
    0 means no Moderator, 1 means Moderator
    
    int
    showAudioVideoTestAsInt
    0 means don't show Audio/Video Test, 1 means show Audio/Video
                Test Application before the user is logged into the room
    
    int
    showNickNameDialogAsInt
    0 means do not show the popup to enter a nichname, 1 means
                that there is a popup to enter the nickname for the conference
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserAndNickName?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&profilePictureUrl=VALUE&email=VALUE&externalUserId=VALUE&externalUserType=VALUE&room_id=VALUE&becomeModeratorAsInt=VALUE&showAudioVideoTestAsInt=VALUE&showNickNameDialogAsInt=VALUE
    
    """
    return call("setUserAndNickName", SID, username, firstname, lastname, profilePictureUrl, email, externalUserId, externalUserType, room_id, becomeModeratorAsInt, showAudioVideoTestAsInt, showNickNameDialogAsInt)
    
def setUserObjectAndGenerateRecordingHashByURL(SID, username, firstname, lastname, externalUserId, externalUserType, recording_id):

    """
    Use this method to access a Recording instead of Room
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    username
    any username
    
    String
    firstname
    any firstname
    
    String
    lastname
    any lastname
    
    String
    externalUserId
    if you have any external user Id you may set it here
    
    String
    externalUserType
    you can specify your system-name here, for example "moodle"
    
    Long
    recording_id
    the id of the recording, get a List of all Recordings with
                RoomService::getFlvRecordingByExternalRoomType
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/setUserObjectAndGenerateRecordingHashByURL?SID=VALUE&username=VALUE&firstname=VALUE&lastname=VALUE&externalUserId=VALUE&externalUserType=VALUE&recording_id=VALUE
    
    """
    return call("setUserObjectAndGenerateRecordingHashByURL", SID, username, firstname, lastname, externalUserId, externalUserType, recording_id)
    
def addUserToOrganisation(SID, user_id, organisation_id, insertedby):

    """
    Add a user to a certain organization
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    Long
    user_id
    the user id
    
    Long
    organisation_id
    the organization id
    
    Long
    insertedby
    user id of the operating user
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/addUserToOrganisation?SID=VALUE&user_id=VALUE&organisation_id=VALUE&insertedby=VALUE
    
    """
    return call("addUserToOrganisation", SID, user_id, organisation_id, insertedby)
    
def getUsersByOrganisation(SID, organisation_id, start, max, orderby, asc):

    """
    Search users and return them
    
    Return Type: org.apache.openmeetings.db.dto.basic.SearchResult
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    long
    organisation_id
    the organization id
    
    int
    start
    first record
    
    int
    max
    max records
    
    String
    orderby
    orderby clause
    
    boolean
    asc
    asc or desc
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/getUsersByOrganisation?SID=VALUE&organisation_id=VALUE&start=VALUE&max=VALUE&orderby=VALUE&asc=VALUE
    
    """
    return call("getUsersByOrganisation", SID, organisation_id, start, max, orderby, asc)
    
def kickUserByPublicSID(SID, publicSID):

    """
    Kick a user by its public SID
    
    Return Type: java.lang.Boolean
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    publicSID
    the publicSID (you can get it from the call to get users in a
                room)
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/kickUserByPublicSID?SID=VALUE&publicSID=VALUE
    
    """
    return call("kickUserByPublicSID", SID, publicSID)
    
def addOrganisation(SID, name):

    """
    add a new organisation
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID from getSession
    
    String
    name
    the name of the org
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/UserService/addOrganisation?SID=VALUE&name=VALUE
    
    """
    return call("addOrganisation", SID, name)
    
