"""
Generated Python API code, for RoomService
"""

from . import call

def getRoomsPublic(SID, roomtypes_id):

    """
    Returns an Object of Type RoomsList which contains a list of
     Room-Objects. Every Room-Object contains a Roomtype and all informations
     about that Room. The List of current-users in the room is Null if you get
     them via SOAP. The Roomtype can be 1 for conference rooms or 2 for
     audience rooms.
    
    Return Type: org.apache.openmeetings.db.entity.room.Room[]
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    roomtypes_id
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomsPublic?SID=VALUE&roomtypes_id=VALUE
    
    """
    return call("getRoomsPublic", SID, roomtypes_id)
    
def deleteFlvRecording(SID, flvRecordingId):

    """
    Deletes a flv recording
    
    Return Type: boolean
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    flvRecordingId
    the id of the recording
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/deleteFlvRecording?SID=VALUE&flvRecordingId=VALUE
    
    """
    return call("deleteFlvRecording", SID, flvRecordingId)
    
def getFlvRecordingByExternalUserId(SID, externalUserId, externalUserType):

    """
    Gets a list of flv recordings
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    externalUserId
    the externalUserId
    
    String
    externalUsertype
    the externalUserType
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getFlvRecordingByExternalUserId?SID=VALUE&externalUserId=VALUE&externalUserType=VALUE
    
    """
    return call("getFlvRecordingByExternalUserId", SID, externalUserId, externalUserType)
    
def getFlvRecordingByExternalRoomTypeAndCreator(SID, externalRoomType, insertedBy):

    """
    Gets a list of flv recordings
    
    Return Type: org.apache.openmeetings.db.dto.file.RecordingObject[]
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    externalRoomType
    externalRoomType specified when creating the room
    
    Long
    insertedBy
    the userId that created the recording
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getFlvRecordingByExternalRoomTypeAndCreator?SID=VALUE&externalRoomType=VALUE&insertedBy=VALUE
    
    """
    return call("getFlvRecordingByExternalRoomTypeAndCreator", SID, externalRoomType, insertedBy)
    
def getFlvRecordingByExternalRoomTypeByList(SID, externalRoomType):

    """
    Gets a list of flv recordings
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    externalRoomType
    externalRoomType specified when creating the room
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getFlvRecordingByExternalRoomTypeByList?SID=VALUE&externalRoomType=VALUE
    
    """
    return call("getFlvRecordingByExternalRoomTypeByList", SID, externalRoomType)
    
def getFlvRecordingByExternalRoomType(SID, externalRoomType):

    """
    Gets a list of flv recordings
    
    Return Type: org.apache.openmeetings.db.entity.record.FlvRecording[]
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    externalRoomType
    externalRoomType specified when creating the room
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getFlvRecordingByExternalRoomType?SID=VALUE&externalRoomType=VALUE
    
    """
    return call("getFlvRecordingByExternalRoomType", SID, externalRoomType)
    
def getFlvRecordingByRoomId(SID, roomId):

    """
    Get list of recordings
    
    Return Type: org.apache.openmeetings.db.entity.record.FlvRecording[]
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    roomId
    the room id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getFlvRecordingByRoomId?SID=VALUE&roomId=VALUE
    
    """
    return call("getFlvRecordingByRoomId", SID, roomId)
    
def getRoomTypes(SID):

    """
    List of available room types
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    - The SID of the User. This SID must be marked as Loggedin
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomTypes?SID=VALUE
    
    """
    return call("getRoomTypes", SID)
    
def getRoomCounters(SID, roomId):

    """
    Returns current users for rooms ids
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    - The SID of the User. This SID must be marked as Loggedin
    
    Integer
    roomId
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomCounters?SID=VALUE&roomId=VALUE
    
    """
    return call("getRoomCounters", SID, roomId)
    
def getRoomById(SID, rooms_id):

    """
    returns a conference room object
    
    Return Type: org.apache.openmeetings.db.entity.room.Room
    
    # Parameters:
    String
    SID
    - The SID of the User. This SID must be marked as Loggedin
    
    long
    rooms_id
    - the room id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomById?SID=VALUE&rooms_id=VALUE
    
    """
    return call("getRoomById", SID, rooms_id)
    
def getRoomWithClientObjectsById(SID, rooms_id):

    """
    Returns a object of type RoomReturn
    
    Return Type: org.apache.openmeetings.axis.services.RoomReturn
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    long
    rooms_id
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomWithClientObjectsById?SID=VALUE&rooms_id=VALUE
    
    """
    return call("getRoomWithClientObjectsById", SID, rooms_id)
    
def getRooms(SID, start, max, orderby, asc):

    """
    Returns a List of Objects of Rooms You can use "name" as value for
     orderby or rooms_id
    
    Return Type: org.apache.openmeetings.db.dto.room.RoomSearchResult
    
    # Parameters:
    String
    SID
    - The SID of the User. This SID must be marked as Loggedin
    
    int
    start
    - The id you want to start
    
    int
    max
    - The maximum you want to get
    
    String
    orderby
    - The column it will be ordered
    
    boolean
    asc
    - Asc or Desc sort ordering
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRooms?SID=VALUE&start=VALUE&max=VALUE&orderby=VALUE&asc=VALUE
    
    """
    return call("getRooms", SID, start, max, orderby, asc)
    
def getRoomsWithCurrentUsers(SID, start, max, orderby, asc):

    """
    Returns a List of Objects of Rooms You can use "name" as value for
     orderby or rooms_id. It also fills the attribute currentUsers in the
     Room-Object
    
    Return Type: org.apache.openmeetings.db.dto.room.RoomSearchResult
    
    # Parameters:
    String
    SID
    - The SID of the User. This SID must be marked as Loggedin
    
    int
    start
    - The id you want to start
    
    int
    max
    - The maximum you want to get
    
    String
    orderby
    - The column it will be ordered
    
    boolean
    asc
    - Asc or Desc sort ordering
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomsWithCurrentUsers?SID=VALUE&start=VALUE&max=VALUE&orderby=VALUE&asc=VALUE
    
    """
    return call("getRoomsWithCurrentUsers", SID, start, max, orderby, asc)
    
def addRoom(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, videoPodWidth, videoPodHeight, videoPodXPosition, videoPodYPosition, moderationPanelXPosition, showWhiteBoard, whiteBoardPanelXPosition, whiteBoardPanelYPosition, whiteBoardPanelHeight, whiteBoardPanelWidth, showFilesPanel, filesPanelXPosition, filesPanelYPosition, filesPanelHeight, filesPanelWidth):

    """
    TODO: Fix Organization Issue
     
     deprecated use addRoomWithModeration instead
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    
    
    Long
    roomtypes_id
    
    
    String
    comment
    
    
    Long
    numberOfPartizipants
    
    
    Boolean
    ispublic
    
    
    Integer
    videoPodWidth
    
    
    Integer
    videoPodHeight
    
    
    Integer
    videoPodXPosition
    
    
    Integer
    videoPodYPosition
    
    
    Integer
    moderationPanelXPosition
    
    
    Boolean
    showWhiteBoard
    
    
    Integer
    whiteBoardPanelXPosition
    
    
    Integer
    whiteBoardPanelYPosition
    
    
    Integer
    whiteBoardPanelHeight
    
    
    Integer
    whiteBoardPanelWidth
    
    
    Boolean
    showFilesPanel
    
    
    Integer
    filesPanelXPosition
    
    
    Integer
    filesPanelYPosition
    
    
    Integer
    filesPanelHeight
    
    
    Integer
    filesPanelWidth
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoom?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&videoPodWidth=VALUE&videoPodHeight=VALUE&videoPodXPosition=VALUE&videoPodYPosition=VALUE&moderationPanelXPosition=VALUE&showWhiteBoard=VALUE&whiteBoardPanelXPosition=VALUE&whiteBoardPanelYPosition=VALUE&whiteBoardPanelHeight=VALUE&whiteBoardPanelWidth=VALUE&showFilesPanel=VALUE&filesPanelXPosition=VALUE&filesPanelYPosition=VALUE&filesPanelHeight=VALUE&filesPanelWidth=VALUE
    
    """
    return call("addRoom", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, videoPodWidth, videoPodHeight, videoPodXPosition, videoPodYPosition, moderationPanelXPosition, showWhiteBoard, whiteBoardPanelXPosition, whiteBoardPanelYPosition, whiteBoardPanelHeight, whiteBoardPanelWidth, showFilesPanel, filesPanelXPosition, filesPanelYPosition, filesPanelHeight, filesPanelWidth)
    
def addRoomWithModeration(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom):

    """
    Create a conference room
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    Name of the Room
    
    Long
    roomtypes_id
    Type of that room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    any comment
    
    Long
    numberOfPartizipants
    the maximum users allowed in this room
    
    Boolean
    ispublic
    If this room is public (use true if you don't deal with
                different Organizations)
    
    Boolean
    appointment
    is it a Calendar Room (use false by default)
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time (use false by default)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait untill a Moderator arrives. Use the
                becomeModerator param in setUserObjectAndGenerateRoomHash to
                set a user as default Moderator
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModeration?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE
    
    """
    return call("addRoomWithModeration", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom)
    
def addRoomWithModerationAndQuestions(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions):

    """
    this SOAP Method has an additional param to enable or disable the buttons
     to apply for moderation this does only work in combination with the
     room-type restricted
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    Name of the Room
    
    Long
    roomtypes_id
    Type of that room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    any comment
    
    Long
    numberOfPartizipants
    the maximum users allowed in this room
    
    Boolean
    ispublic
    If this room is public (use true if you don't deal with
                different Organizations)
    
    Boolean
    appointment
    is it a Calendar Room (use false by default)
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time (use false by default)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait untill a Moderator arrives. Use the
                becomeModerator param in setUserObjectAndGenerateRoomHash to
                set a user as default Moderator
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationAndQuestions?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&allowUserQuestions=VALUE
    
    """
    return call("addRoomWithModerationAndQuestions", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions)
    
def addRoomWithModerationQuestionsAndAudioType(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions, isAudioOnly):

    """
    adds a new room with options for user questions and audio only
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    Name of the Room
    
    Long
    roomtypes_id
    Type of that room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    any comment
    
    Long
    numberOfPartizipants
    the maximum users allowed in this room
    
    Boolean
    ispublic
    If this room is public (use true if you don't deal with
                different Organizations)
    
    Boolean
    appointment
    is it a Calendar Room (use false by default)
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time (use false by default)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator param in setUserObjectAndGenerateRoomHash to
                set a user as default Moderator
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    Boolean
    isAudioOnly
    enable or disable the video / or audio-only
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationQuestionsAndAudioType?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&allowUserQuestions=VALUE&isAudioOnly=VALUE
    
    """
    return call("addRoomWithModerationQuestionsAndAudioType", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions, isAudioOnly)
    
def addRoomWithModerationQuestionsAudioTypeAndHideOptions(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions, isAudioOnly, hideTopBar, hideChat, hideActivitiesAndActions, hideFilesExplorer, hideActionsMenu, hideScreenSharing, hideWhiteboard):

    """
    adds a new room with options for user questions, audio only and hide
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    Name of the Room
    
    Long
    roomtypes_id
    Type of that room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    any comment
    
    Long
    numberOfPartizipants
    the maximum users allowed in this room
    
    Boolean
    ispublic
    If this room is public (use true if you don't deal with
                different Organizations)
    
    Boolean
    appointment
    is it a Calendar Room (use false by default)
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time (use false by default)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator param in setUserObjectAndGenerateRoomHash to
                set a user as default Moderator
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    Boolean
    isAudioOnly
    enable or disable the video / or audio-only
    
    Boolean
    hideTopBar
    hide or show TopBar
    
    Boolean
    hideChat
    hide or show Chat
    
    Boolean
    hideActivitiesAndActions
    hide or show Activities And Actions
    
    Boolean
    hideFilesExplorer
    hide or show Files Explorer
    
    Boolean
    hideActionsMenu
    hide or show Actions Menu
    
    Boolean
    hideScreenSharing
    hide or show Screen Sharing
    
    Boolean
    hideWhiteboard
    hide or show Whiteboard. If whitboard is hidden, video pods
                and scrollbar appear instead.
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationQuestionsAudioTypeAndHideOptions?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&allowUserQuestions=VALUE&isAudioOnly=VALUE&hideTopBar=VALUE&hideChat=VALUE&hideActivitiesAndActions=VALUE&hideFilesExplorer=VALUE&hideActionsMenu=VALUE&hideScreenSharing=VALUE&hideWhiteboard=VALUE
    
    """
    return call("addRoomWithModerationQuestionsAudioTypeAndHideOptions", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions, isAudioOnly, hideTopBar, hideChat, hideActivitiesAndActions, hideFilesExplorer, hideActionsMenu, hideScreenSharing, hideWhiteboard)
    
def getRoomIdByExternalId(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomId, externalRoomType):

    """
    Checks if a room with this exteralRoomId + externalRoomType does exist,
     if yes it returns the room id if not, it will create the room and then
     return the room id of the newly created room
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    Name of the room
    
    Long
    roomtypes_id
    Type of that room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    any comment
    
    Long
    numberOfPartizipants
    the maximum users allowed in this room
    
    Boolean
    ispublic
    If this room is public (use true if you don't deal with
                different Organizations)
    
    Boolean
    appointment
    is it a Calendar Room? (use false if not sure what that means)
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait untill a Moderator arrives. Use the
                becomeModerator param in setUserObjectAndGenerateRoomHash to
                set a user as default Moderator
    
    Long
    externalRoomId
    your external room id may set here
    
    String
    externalRoomType
    you can specify your system-name or type of room here, for
                example "moodle"
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomIdByExternalId?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&externalRoomId=VALUE&externalRoomType=VALUE
    
    """
    return call("getRoomIdByExternalId", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomId, externalRoomType)
    
def updateRoom(SID, rooms_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, videoPodWidth, videoPodHeight, videoPodXPosition, videoPodYPosition, moderationPanelXPosition, showWhiteBoard, whiteBoardPanelXPosition, whiteBoardPanelYPosition, whiteBoardPanelHeight, whiteBoardPanelWidth, showFilesPanel, filesPanelXPosition, filesPanelYPosition, filesPanelHeight, filesPanelWidth, appointment):

    """
    TODO: Fix Organization Issue deprecated use updateRoomWithModeration
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    rooms_id
    
    
    String
    name
    
    
    Long
    roomtypes_id
    
    
    String
    comment
    
    
    Long
    numberOfPartizipants
    
    
    Boolean
    ispublic
    
    
    Integer
    videoPodWidth
    
    
    Integer
    videoPodHeight
    
    
    Integer
    videoPodXPosition
    
    
    Integer
    videoPodYPosition
    
    
    Integer
    moderationPanelXPosition
    
    
    Boolean
    showWhiteBoard
    
    
    Integer
    whiteBoardPanelXPosition
    
    
    Integer
    whiteBoardPanelYPosition
    
    
    Integer
    whiteBoardPanelHeight
    
    
    Integer
    whiteBoardPanelWidth
    
    
    Boolean
    showFilesPanel
    
    
    Integer
    filesPanelXPosition
    
    
    Integer
    filesPanelYPosition
    
    
    Integer
    filesPanelHeight
    
    
    Integer
    filesPanelWidth
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/updateRoom?SID=VALUE&rooms_id=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&videoPodWidth=VALUE&videoPodHeight=VALUE&videoPodXPosition=VALUE&videoPodYPosition=VALUE&moderationPanelXPosition=VALUE&showWhiteBoard=VALUE&whiteBoardPanelXPosition=VALUE&whiteBoardPanelYPosition=VALUE&whiteBoardPanelHeight=VALUE&whiteBoardPanelWidth=VALUE&showFilesPanel=VALUE&filesPanelXPosition=VALUE&filesPanelYPosition=VALUE&filesPanelHeight=VALUE&filesPanelWidth=VALUE&appointment=VALUE
    
    """
    return call("updateRoom", SID, rooms_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, videoPodWidth, videoPodHeight, videoPodXPosition, videoPodYPosition, moderationPanelXPosition, showWhiteBoard, whiteBoardPanelXPosition, whiteBoardPanelYPosition, whiteBoardPanelHeight, whiteBoardPanelWidth, showFilesPanel, filesPanelXPosition, filesPanelYPosition, filesPanelHeight, filesPanelWidth, appointment)
    
def updateRoomWithModeration(SID, room_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom):

    """
    Updates a conference room by its room id
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    the room id to update
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/updateRoomWithModeration?SID=VALUE&room_id=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE
    
    """
    return call("updateRoomWithModeration", SID, room_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom)
    
def updateRoomWithModerationAndQuestions(SID, room_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions):

    """
    
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    the room id to update
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/updateRoomWithModerationAndQuestions?SID=VALUE&room_id=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&allowUserQuestions=VALUE
    
    """
    return call("updateRoomWithModerationAndQuestions", SID, room_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions)
    
def updateRoomWithModerationQuestionsAudioTypeAndHideOptions(SID, room_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions, isAudioOnly, hideTopBar, hideChat, hideActivitiesAndActions, hideFilesExplorer, hideActionsMenu, hideScreenSharing, hideWhiteboard):

    """
    update room with options for user questions, audio only and hide
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    the room id to update
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    number of participants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment (use false if not sure what that
                means)
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    Boolean
    isAudioOnly
    enable or disable the video / or audio-only
    
    Boolean
    hideTopBar
    hide or show TopBar
    
    Boolean
    hideChat
    hide or show Chat
    
    Boolean
    hideActivitiesAndActions
    hide or show Activities And Actions
    
    Boolean
    hideFilesExplorer
    hide or show Files Explorer
    
    Boolean
    hideActionsMenu
    hide or show Actions Menu
    
    Boolean
    hideScreenSharing
    hide or show Screen Sharing
    
    Boolean
    hideWhiteboard
    hide or show Whiteboard. If whitboard is hidden, video pods
                and scrollbar appear instead.
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/updateRoomWithModerationQuestionsAudioTypeAndHideOptions?SID=VALUE&room_id=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&allowUserQuestions=VALUE&isAudioOnly=VALUE&hideTopBar=VALUE&hideChat=VALUE&hideActivitiesAndActions=VALUE&hideFilesExplorer=VALUE&hideActionsMenu=VALUE&hideScreenSharing=VALUE&hideWhiteboard=VALUE
    
    """
    return call("updateRoomWithModerationQuestionsAudioTypeAndHideOptions", SID, room_id, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, allowUserQuestions, isAudioOnly, hideTopBar, hideChat, hideActivitiesAndActions, hideFilesExplorer, hideActionsMenu, hideScreenSharing, hideWhiteboard)
    
def deleteRoom(SID, rooms_id):

    """
    Delete a room by its room id
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    long
    rooms_id
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/deleteRoom?SID=VALUE&rooms_id=VALUE
    
    """
    return call("deleteRoom", SID, rooms_id)
    
def kickUser(SID_Admin, room_id):

    """
    kick all uses of a certain room
    
    Return Type: java.lang.Boolean
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
                _Admin
    
    Long
    room_id
    the room id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/kickUser?SID_Admin=VALUE&room_id=VALUE
    
    """
    return call("kickUser", SID_Admin, room_id)
    
def addRoomWithModerationAndExternalType(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType):

    """
    Add a new conference room with option to set the external room type, the
     external room type should be set if multiple applications use the same
     OpenMeetings instance
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    String
    externalRoomType
    the external room type (can be used to identify different
                external systems using same OpenMeetings instance)
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationAndExternalType?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&externalRoomType=VALUE
    
    """
    return call("addRoomWithModerationAndExternalType", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType)
    
def addRoomWithModerationExternalTypeAndAudioType(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, allowUserQuestions, isAudioOnly):

    """
    Adds a new room with options for audio only
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    String
    externalRoomType
    the external room type (can be used to identify different
                external systems using same OpenMeetings instance)
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    Boolean
    isAudioOnly
    enable or disable the video / or audio-only
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationExternalTypeAndAudioType?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&externalRoomType=VALUE&allowUserQuestions=VALUE&isAudioOnly=VALUE
    
    """
    return call("addRoomWithModerationExternalTypeAndAudioType", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, allowUserQuestions, isAudioOnly)
    
def addRoomWithModerationAndRecordingFlags(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, allowUserQuestions, isAudioOnly, waitForRecording, allowRecording):

    """
    Adds a new room with options for recording
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    String
    externalRoomType
    the external room type (can be used to identify different
                external systems using same OpenMeetings instance)
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    Boolean
    isAudioOnly
    enable or disable the video / or audio-only
    
    Boolean
    waitForRecording
    if the users in the room will get a notification that they
                should start recording before they do a conference
    
    Boolean
    allowRecording
    if the recording option is available or not
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationAndRecordingFlags?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&externalRoomType=VALUE&allowUserQuestions=VALUE&isAudioOnly=VALUE&waitForRecording=VALUE&allowRecording=VALUE
    
    """
    return call("addRoomWithModerationAndRecordingFlags", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, allowUserQuestions, isAudioOnly, waitForRecording, allowRecording)
    
def addRoomWithModerationExternalTypeAndTopBarOption(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, allowUserQuestions, isAudioOnly, waitForRecording, allowRecording, hideTopBar):

    """
    Add a conference room with options to disable the top menu bar in the
     conference room
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    String
    externalRoomType
    the external room type (can be used to identify different
                external systems using same OpenMeetings instance)
    
    Boolean
    allowUserQuestions
    enable or disable the button to allow users to apply for
                moderation
    
    Boolean
    isAudioOnly
    enable or disable the video / or audio-only
    
    Boolean
    waitForRecording
    if the users in the room will get a notification that they
                should start recording before they do a conference
    
    Boolean
    allowRecording
    if the recording option is available or not
    
    Boolean
    hideTopBar
    if the top bar in the conference room is visible or not
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationExternalTypeAndTopBarOption?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&externalRoomType=VALUE&allowUserQuestions=VALUE&isAudioOnly=VALUE&waitForRecording=VALUE&allowRecording=VALUE&hideTopBar=VALUE
    
    """
    return call("addRoomWithModerationExternalTypeAndTopBarOption", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, allowUserQuestions, isAudioOnly, waitForRecording, allowRecording, hideTopBar)
    
def getInvitationHash(SID, username, room_id, isPasswordProtected, invitationpass, valid, validFromDate, validFromTime, validToDate, validToTime):

    """
    Create a Invitation hash and optionally send it by mail the From to Date
     is as String as some SOAP libraries do not accept Date Objects in SOAP
     Calls Date is parsed as dd.mm.yyyy, time as hh:mm (don't forget the
     leading zero's)
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin a
                valid Session Token
    
    String
    username
    the username of the User that he will get
    
    Long
    room_id
    the conference room id of the invitation
    
    Boolean
    isPasswordProtected
    if the invitation is password protected
    
    String
    invitationpass
    the password for accessing the conference room via the
                invitation hash
    
    Integer
    valid
    the type of validation for the hash 1: endless, 2: from-to
                period, 3: one-time
    
    String
    validFromDate
    Date in Format of dd.mm.yyyy only of interest if valid is type
                2
    
    String
    validFromTime
    time in Format of hh:mm only of interest if valid is type 2
    
    String
    validToDate
    Date in Format of dd.mm.yyyy only of interest if valid is type
                2
    
    String
    validToTime
    time in Format of hh:mm only of interest if valid is type 2
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getInvitationHash?SID=VALUE&username=VALUE&room_id=VALUE&isPasswordProtected=VALUE&invitationpass=VALUE&valid=VALUE&validFromDate=VALUE&validFromTime=VALUE&validToDate=VALUE&validToTime=VALUE
    
    """
    return call("getInvitationHash", SID, username, room_id, isPasswordProtected, invitationpass, valid, validFromDate, validFromTime, validToDate, validToTime)
    
def sendInvitationHash(SID, username, message, baseurl, email, subject, room_id, conferencedomain, isPasswordProtected, invitationpass, valid, validFromDate, validFromTime, validToDate, validToTime, language_id, sendMail):

    """
    Create a Invitation hash and optionally send it by mail the From to Date
     is as String as some SOAP libraries do not accept Date Objects in SOAP
     Calls Date is parsed as dd.mm.yyyy, time as hh:mm (don't forget the
     leading zero's)
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin a
                valid Session Token
    
    String
    username
    the Username of the User that he will get
    
    String
    message
    the Message in the Email Body send with the invitation if
                sendMail is true
    
    String
    baseurl
    the baseURL for the Infivations link in the Mail Body if
                sendMail is true
    
    String
    email
    the Email to send the invitation to if sendMail is true
    
    String
    subject
    the subject of the Email send with the invitation if sendMail
                is true
    
    Long
    room_id
    the conference room id of the invitation
    
    String
    conferencedomain
    the domain of the room (keep empty)
    
    Boolean
    isPasswordProtected
    if the invitation is password protected
    
    String
    invitationpass
    the password for accessing the conference room via the
                invitation hash
    
    Integer
    valid
    the type of validation for the hash 1: endless, 2: from-to
                period, 3: one-time
    
    String
    validFromDate
    Date in Format of dd.mm.yyyy only of interest if valid is type
                2
    
    String
    validFromTime
    time in Format of hh:mm only of interest if valid is type 2
    
    String
    validToDate
    Date in Format of dd.mm.yyyy only of interest if valid is type
                2
    
    String
    validToTime
    time in Format of hh:mm only of interest if valid is type 2
    
    Long
    language_id
    the language id of the EMail that is send with the invitation
                if sendMail is true
    
    Boolean
    sendMail
    if sendMail is true then the RPC-Call will send the invitation
                to the email
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/sendInvitationHash?SID=VALUE&username=VALUE&message=VALUE&baseurl=VALUE&email=VALUE&subject=VALUE&room_id=VALUE&conferencedomain=VALUE&isPasswordProtected=VALUE&invitationpass=VALUE&valid=VALUE&validFromDate=VALUE&validFromTime=VALUE&validToDate=VALUE&validToTime=VALUE&language_id=VALUE&sendMail=VALUE
    
    """
    return call("sendInvitationHash", SID, username, message, baseurl, email, subject, room_id, conferencedomain, isPasswordProtected, invitationpass, valid, validFromDate, validFromTime, validToDate, validToTime, language_id, sendMail)
    
def sendInvitationHashWithDateObject(SID, username, message, baseurl, email, subject, room_id, conferencedomain, isPasswordProtected, invitationpass, valid, fromDate, toDate, language_id, sendMail):

    """
    Create a Invitation hash and optionally send it by mail the From to Date
     is as String as some SOAP libraries do not accept Date Objects in SOAP
     Calls Date is parsed as dd.mm.yyyy, time as hh:mm (don't forget the
     leading zero's)
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin a
                valid Session Token
    
    String
    username
    the Username of the User that he will get
    
    String
    message
    the Message in the Email Body send with the invitation if
                sendMail is true
    
    String
    baseurl
    the baseURL for the Infivations link in the Mail Body if
                sendMail is true
    
    String
    email
    the Email to send the invitation to if sendMail is true
    
    String
    subject
    the subject of the Email send with the invitation if sendMail
                is true
    
    Long
    room_id
    the conference room id of the invitation
    
    String
    conferencedomain
    the domain of the room (keep empty)
    
    Boolean
    isPasswordProtected
    if the invitation is password protected
    
    String
    invitationpass
    the password for accessing the conference room via the
                invitation hash
    
    Integer
    valid
    the type of validation for the hash 1: endless, 2: from-to
                period, 3: one-time
    
    Date
    fromDate
    Date as Date Object only of interest if valid is type 2
    
    Date
    toDate
    Date as Date Object only of interest if valid is type 2
    
    Long
    language_id
    the language id of the EMail that is send with the invitation
                if sendMail is true
    
    Boolean
    sendMail
    if sendMail is true then the RPC-Call will send the invitation
                to the email
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/sendInvitationHashWithDateObject?SID=VALUE&username=VALUE&message=VALUE&baseurl=VALUE&email=VALUE&subject=VALUE&room_id=VALUE&conferencedomain=VALUE&isPasswordProtected=VALUE&invitationpass=VALUE&valid=VALUE&fromDate=VALUE&toDate=VALUE&language_id=VALUE&sendMail=VALUE
    
    """
    return call("sendInvitationHashWithDateObject", SID, username, message, baseurl, email, subject, room_id, conferencedomain, isPasswordProtected, invitationpass, valid, fromDate, toDate, language_id, sendMail)
    
def getRoomsWithCurrentUsersByList(SID, start, max, orderby, asc):

    """
    Return a RoomReturn Object with information of the current users of a
     conference room
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    int
    start
    The id you want to start
    
    int
    max
    The maximum you want to get
    
    String
    orderby
    The column it will be ordered
    
    boolean
    asc
    Asc or Desc sort ordering
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomsWithCurrentUsersByList?SID=VALUE&start=VALUE&max=VALUE&orderby=VALUE&asc=VALUE
    
    """
    return call("getRoomsWithCurrentUsersByList", SID, start, max, orderby, asc)
    
def getRoomsWithCurrentUsersByListAndType(SID, start, max, orderby, asc, externalRoomType):

    """
    Return a RoomReturn Object with information of the current users of a
     conference room with option to search for special external room types
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    int
    start
    The id you want to start
    
    int
    max
    The maximum you want to get
    
    String
    orderby
    The column it will be ordered
    
    boolean
    asc
    Asc or Desc sort ordering
    
    String
    externalRoomType
    the external room type
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/getRoomsWithCurrentUsersByListAndType?SID=VALUE&start=VALUE&max=VALUE&orderby=VALUE&asc=VALUE&externalRoomType=VALUE
    
    """
    return call("getRoomsWithCurrentUsersByListAndType", SID, start, max, orderby, asc, externalRoomType)
    
def addRoomWithModerationAndExternalTypeAndStartEnd(SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, validFromDate, validFromTime, validToDate, validToTime, isPasswordProtected, password, reminderTypeId, redirectURL):

    """
    Adds a conference room that is only available for a period of time
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    name
    new name of the room
    
    Long
    roomtypes_id
    new type of room (1 = Conference, 2 = Audience, 3 =
                Restricted, 4 = Interview)
    
    String
    comment
    new comment
    
    Long
    numberOfPartizipants
    new numberOfParticipants
    
    Boolean
    ispublic
    is public
    
    Boolean
    appointment
    if the room is an appointment
    
    Boolean
    isDemoRoom
    is it a Demo Room with limited time? (use false if not sure
                what that means)
    
    Integer
    demoTime
    time in seconds after the user will be logged out (only
                enabled if isDemoRoom is true)
    
    Boolean
    isModeratedRoom
    Users have to wait until a Moderator arrives. Use the
                becomeModerator parameter in setUserObjectAndGenerateRoomHash
                to set a user as default Moderator
    
    String
    externalRoomType
    the external room type (can be used to identify different
                external systems using same OpenMeetings instance)
    
    String
    validFromDate
    valid from as Date format: dd.MM.yyyy
    
    String
    validFromTime
    valid to as time format: mm:hh
    
    String
    validToDate
    valid to Date format: dd.MM.yyyy
    
    String
    validToTime
    valid to time format: mm:hh
    
    Boolean
    isPasswordProtected
    If the links send via EMail to invited people is password
                protected
    
    String
    password
    Password for Invitations send via Mail
    
    Long
    reminderTypeId
    1=none, 2=simple mail, 3=ICAL
    
    String
    redirectURL
    URL Users will be lead to if the Conference Time is elapsed
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomWithModerationAndExternalTypeAndStartEnd?SID=VALUE&name=VALUE&roomtypes_id=VALUE&comment=VALUE&numberOfPartizipants=VALUE&ispublic=VALUE&appointment=VALUE&isDemoRoom=VALUE&demoTime=VALUE&isModeratedRoom=VALUE&externalRoomType=VALUE&validFromDate=VALUE&validFromTime=VALUE&validToDate=VALUE&validToTime=VALUE&isPasswordProtected=VALUE&password=VALUE&reminderTypeId=VALUE&redirectURL=VALUE
    
    """
    return call("addRoomWithModerationAndExternalTypeAndStartEnd", SID, name, roomtypes_id, comment, numberOfPartizipants, ispublic, appointment, isDemoRoom, demoTime, isModeratedRoom, externalRoomType, validFromDate, validFromTime, validToDate, validToTime, isPasswordProtected, password, reminderTypeId, redirectURL)
    
def addMeetingMemberRemindToRoom(SID, room_id, firstname, lastname, email, baseUrl, language_id):

    """
    Add a meeting member to a certain room. This is the same as adding an
     external user to a event in the calendar.
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    The Room Id the meeting member is going to be added
    
    String
    firstname
    The first name of the meeting member
    
    String
    lastname
    The last name of the meeting member
    
    String
    email
    The email of the Meeting member
    
    String
    baseUrl
    The baseUrl, this is important to send the correct link in the
                invitation to the meeting member
    
    Long
    language_id
    The ID of the language, for the email that is send to the
                meeting member
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addMeetingMemberRemindToRoom?SID=VALUE&room_id=VALUE&firstname=VALUE&lastname=VALUE&email=VALUE&baseUrl=VALUE&language_id=VALUE
    
    """
    return call("addMeetingMemberRemindToRoom", SID, room_id, firstname, lastname, email, baseUrl, language_id)
    
def addExternalMeetingMemberRemindToRoom(SID, room_id, firstname, lastname, email, baseUrl, language_id, jNameTimeZone, invitorName):

    """
    Add a meeting member to a certain room. This is the same as adding an
     external user to a event in the calendar. with a certain time zone
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    The Room Id the meeting member is going to be added
    
    String
    firstname
    The first name of the meeting member
    
    String
    lastname
    The last name of the meeting member
    
    String
    email
    The email of the Meeting member
    
    String
    baseUrl
    The baseUrl, this is important to send the correct link in the
                invitation to the meeting member
    
    Long
    language_id
    The ID of the language, for the email that is send to the
                meeting member
    
    String
    jNameTimeZone
    name of the timezone
    
    String
    invitorName
    name of invitation creators
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addExternalMeetingMemberRemindToRoom?SID=VALUE&room_id=VALUE&firstname=VALUE&lastname=VALUE&email=VALUE&baseUrl=VALUE&language_id=VALUE&jNameTimeZone=VALUE&invitorName=VALUE
    
    """
    return call("addExternalMeetingMemberRemindToRoom", SID, room_id, firstname, lastname, email, baseUrl, language_id, jNameTimeZone, invitorName)
    
def closeRoom(SID, room_id, status):

    """
    Method to remotely close or open rooms. If a room is closed all users
     inside the room and all users that try to enter it will be redirected to
     the redirectURL that is defined in the Room-Object.
     
     Returns positive value if authentication was successful.
    
    Return Type: int
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    the room id
    
    Boolean
    status
    false = close, true = open
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/closeRoom?SID=VALUE&room_id=VALUE&status=VALUE
    
    """
    return call("closeRoom", SID, room_id, status)
    
def modifyRoomParameter(SID, room_id, paramName, paramValue):

    """
    Method to update arbitrary room parameter.
    
    Return Type: int
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    room_id
    the room id
    
    String
    paramName
    
    
    Object
    paramValue
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/modifyRoomParameter?SID=VALUE&room_id=VALUE&paramName=VALUE&paramValue=VALUE
    
    """
    return call("modifyRoomParameter", SID, room_id, paramName, paramValue)
    
def addRoomToOrg(SID, rooms_id, organisation_id):

    """
    Adds a room to an organization
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    - The SID of the User. This SID must be marked as Loggedin
    
    Long
    rooms_id
    - Id of room to be added
    
    Long
    organisation_id
    - Id of organisation that the room is being paired with
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/RoomService/addRoomToOrg?SID=VALUE&rooms_id=VALUE&organisation_id=VALUE
    
    """
    return call("addRoomToOrg", SID, rooms_id, organisation_id)
    
