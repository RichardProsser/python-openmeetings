"""
Generated Python API code, for JabberService
"""

from . import call

def getAvailableRooms(SID):

    """
    Get List<RoomDTO> of all rooms available to the user.
     No admin rights are necessary for this call
    
    Return Type: java.util.List
    
    # Parameters:
    String
    SID
    The SID from UserService.getSession
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/JabberService/getAvailableRooms?SID=VALUE
    
    """
    return call("getAvailableRooms", SID)
    
def getUserCount(SID, roomId):

    """
    Returns the count of users currently in the Room with given id
     No admin rights are necessary for this call
    
    Return Type: int
    
    # Parameters:
    String
    SID
    The SID from UserService.getSession
    
    Long
    roomId
    id of the room to get users
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/JabberService/getUserCount?SID=VALUE&roomId=VALUE
    
    """
    return call("getUserCount", SID, roomId)
    
def getInvitationHash(SID, username, room_id):

    """
    Get invitation hash for the room with given id
     No admin rights are necessary for this call
    
    Return Type: java.lang.String
    
    # Parameters:
    String
    SID
    The SID from UserService.getSession
    
    String
    username
    The name of invited user, will be displayed in the rooms user list
    
    Long
    room_id
    id of the room to get users
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/JabberService/getInvitationHash?SID=VALUE&username=VALUE&room_id=VALUE
    
    """
    return call("getInvitationHash", SID, username, room_id)
    
