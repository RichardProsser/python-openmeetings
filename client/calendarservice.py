"""
Generated Python API code, for CalendarService
"""

from . import call

def getAppointmentByRange(SID, starttime, endtime):

    """
    Load appointments by a start / end range for the current SID
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Date
    starttime
    start time, yyyy-mm-dd
    
    Date
    endtime
    end time, yyyy-mm-dd
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getAppointmentByRange?SID=VALUE&starttime=VALUE&endtime=VALUE
    
    """
    return call("getAppointmentByRange", SID, starttime, endtime)
    
def getAppointmentByRangeForUserId(SID, userId, starttime, endtime):

    """
    Load appointments by a start / end range for the userId
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    long
    userId
    the userId the calendar events should be loaded
    
    Date
    starttime
    start time, yyyy-mm-dd
    
    Date
    endtime
    end time, yyyy-mm-dd
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getAppointmentByRangeForUserId?SID=VALUE&userId=VALUE&starttime=VALUE&endtime=VALUE
    
    """
    return call("getAppointmentByRangeForUserId", SID, userId, starttime, endtime)
    
def getNextAppointment(SID):

    """
    Get the next Calendar event for the current user of the SID
    
    Return Type: org.apache.openmeetings.db.entity.calendar.Appointment
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getNextAppointment?SID=VALUE
    
    """
    return call("getNextAppointment", SID)
    
def getNextAppointmentForUserId(SID, userId):

    """
    Get the next Calendar event for userId
    
    Return Type: org.apache.openmeetings.db.entity.calendar.Appointment
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getNextAppointmentForUserId?SID=VALUE&userId=VALUE
    
    """
    return call("getNextAppointmentForUserId", SID, userId)
    
def searchAppointmentByName(SID, appointmentName):

    """
    Search a calendar event for the current SID
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    appointmentName
    the search string
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/searchAppointmentByName?SID=VALUE&appointmentName=VALUE
    
    """
    return call("searchAppointmentByName", SID, appointmentName)
    
def saveAppointment(SID, appointmentName, appointmentLocation, appointmentDescription, appointmentstart, appointmentend, isDaily, isWeekly, isMonthly, isYearly, categoryId, remind, mmClient, roomType, baseUrl, languageId, isPasswordProtected, password, roomId):

    """
    Save an appointment
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    String
    appointmentName
    name of the calendar event
    
    String
    appointmentLocation
    location info text of the calendar event
    
    String
    appointmentDescription
    description test of the calendar event
    
    Calendar
    appointmentstart
    start as Date yyyy-mm-ddThh:mm:ss
    
    Calendar
    appointmentend
    end as Date yyyy-mm-ddThh:mm:ss
    
    Boolean
    isDaily
    if the calendar event should be repeated daily (not
                implemented)
    
    Boolean
    isWeekly
    if the calendar event should be repeated weekly (not
                implemented)
    
    Boolean
    isMonthly
    if the calendar event should be repeated monthly (not
                implemented)
    
    Boolean
    isYearly
    if the calendar event should be repeated yearly (not
                implemented)
    
    Long
    categoryId
    the category id of the calendar event
    
    Long
    remind
    the reminder type of the calendar event
    
    String
    mmClient
    List of clients, comma separated string, 
                sample: 1,firstname,lastname,hans.tier@gmail.com,1,Etc/GMT+1
                to add multiple clients you can use the same GET parameter in
                the URL multiple times, for example:
                &mmClient=1,firstname,lastname,hans
                .tier@gmail.com,1,Etc/GMT+1&mmClient
                =2,firstname,lastname,hans.tier@gmail.com,1,Etc/GMT+1
    
    Long
    roomType
    the room type for the calendar event
    
    String
    baseUrl
    the base URL for the invitations
    
    Long
    languageId
    the language id of the calendar event, notification emails
                will be send in this language
    
    Boolean
    isPasswordProtected
    if the room is password protected
    
    String
    password
    the password for the room
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/saveAppointment?SID=VALUE&appointmentName=VALUE&appointmentLocation=VALUE&appointmentDescription=VALUE&appointmentstart=VALUE&appointmentend=VALUE&isDaily=VALUE&isWeekly=VALUE&isMonthly=VALUE&isYearly=VALUE&categoryId=VALUE&remind=VALUE&mmClient=VALUE&roomType=VALUE&baseUrl=VALUE&languageId=VALUE&isPasswordProtected=VALUE&password=VALUE&roomId=VALUE
    
    """
    return call("saveAppointment", SID, appointmentName, appointmentLocation, appointmentDescription, appointmentstart, appointmentend, isDaily, isWeekly, isMonthly, isYearly, categoryId, remind, mmClient, roomType, baseUrl, languageId, isPasswordProtected, password, roomId)
    
def updateAppointmentTimeOnly(SID, appointmentId, appointmentstart, appointmentend, baseurl, languageId):

    """
    Update an calendar event time only
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    appointmentId
    the calendar event that should be updated
    
    Date
    appointmentstart
    start yyyy-mm-dd
    
    Date
    appointmentend
    end yyyy-mm-dd
    
    String
    baseurl
    the base URL for the invitations that will be send by email
    
    Long
    languageId
    the language id
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/updateAppointmentTimeOnly?SID=VALUE&appointmentId=VALUE&appointmentstart=VALUE&appointmentend=VALUE&baseurl=VALUE&languageId=VALUE
    
    """
    return call("updateAppointmentTimeOnly", SID, appointmentId, appointmentstart, appointmentend, baseurl, languageId)
    
def updateAppointment(SID, appointmentId, appointmentName, appointmentLocation, appointmentDescription, appointmentstart, appointmentend, isDaily, isWeekly, isMonthly, isYearly, categoryId, remind, mmClient, roomType, baseurl, languageId, isPasswordProtected, password):

    """
    Save an appointment
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    The SID of the User. This SID must be marked as Loggedin
    
    Long
    appointmentId
    the id to update
    
    String
    appointmentName
    name of the calendar event
    
    String
    appointmentLocation
    location info text of the calendar event
    
    String
    appointmentDescription
    description test of the calendar event
    
    Calendar
    appointmentstart
    start as Date yyyy-mm-ddThh:mm:ss
    
    Calendar
    appointmentend
    end as Date yyyy-mm-ddThh:mm:ss
    
    Boolean
    isDaily
    if the calendar event should be repeated daily (not
                implemented)
    
    Boolean
    isWeekly
    if the calendar event should be repeated weekly (not
                implemented)
    
    Boolean
    isMonthly
    if the calendar event should be repeated monthly (not
                implemented)
    
    Boolean
    isYearly
    if the calendar event should be repeated yearly (not
                implemented)
    
    Long
    categoryId
    the category id of the calendar event
    
    Long
    remind
    the reminder type of the calendar event
    
    String
    mmClient
    List of clients, comma separated string, 
                sample: 1,firstname,lastname,hans.tier@gmail.com,1,Etc/GMT+1
                to add multiple clients you can use the same GET parameter in
                the URL multiple times, for example:
                &mmClient=1,firstname,lastname,hans
                .tier@gmail.com,1,Etc/GMT+1&mmClient
                =2,firstname,lastname,hans.tier@gmail.com,1,Etc/GMT+1
    
    Long
    roomType
    the room type for the calendar event
    
    String
    baseUrl
    the base URL for the invitations
    
    Long
    languageId
    the language id of the calendar event, notification emails
                will be send in this language
    
    Boolean
    isPasswordProtected
    if the room is password protected
    
    String
    password
    the password for the room
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/updateAppointment?SID=VALUE&appointmentId=VALUE&appointmentName=VALUE&appointmentLocation=VALUE&appointmentDescription=VALUE&appointmentstart=VALUE&appointmentend=VALUE&isDaily=VALUE&isWeekly=VALUE&isMonthly=VALUE&isYearly=VALUE&categoryId=VALUE&remind=VALUE&mmClient=VALUE&roomType=VALUE&baseurl=VALUE&languageId=VALUE&isPasswordProtected=VALUE&password=VALUE
    
    """
    return call("updateAppointment", SID, appointmentId, appointmentName, appointmentLocation, appointmentDescription, appointmentstart, appointmentend, isDaily, isWeekly, isMonthly, isYearly, categoryId, remind, mmClient, roomType, baseurl, languageId, isPasswordProtected, password)
    
def deleteAppointment(SID, appointmentId, language_id):

    """
    delete a calendar event
     
     If the given SID is from an Administrator or Web-Service user, the user
     can delete any appointment.
     If the SID is assigned to a simple user, he can only delete appointments
     where he is also the owner/creator of the appointment
    
    Return Type: java.lang.Long
    
    # Parameters:
    String
    SID
    an authenticated SID
    
    Long
    appointmentId
    the id to delete
    
    Long
    language_id
    the language id in which the notifications for the deleted
                appointment are send
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/deleteAppointment?SID=VALUE&appointmentId=VALUE&language_id=VALUE
    
    """
    return call("deleteAppointment", SID, appointmentId, language_id)
    
def getAppointmentByRoomId(SID, room_id):

    """
    Load a calendar event by its room id
    
    Return Type: org.apache.openmeetings.db.entity.calendar.Appointment
    
    # Parameters:
    String
    SID
    
    
    Long
    room_id
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getAppointmentByRoomId?SID=VALUE&room_id=VALUE
    
    """
    return call("getAppointmentByRoomId", SID, room_id)
    
def getAppointmentCategoryList(SID):

    """
    Get all categories of calendar events
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getAppointmentCategoryList?SID=VALUE
    
    """
    return call("getAppointmentCategoryList", SID)
    
def getAppointmentReminderTypList(SID):

    """
    Get all reminder types for calendar events
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/CalendarService/getAppointmentReminderTypList?SID=VALUE
    
    """
    return call("getAppointmentReminderTypList", SID)
    
