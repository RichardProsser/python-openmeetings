"""
Generated Python API code, for ServerService
"""

from . import call

def getServers(SID, start, max):

    """
    Method to retrieve the list of the servers participating in cluster
    
    Return Type: org.apache.openmeetings.db.entity.server.Server[]
    
    # Parameters:
    String
    SID
    - session id to identify the user making request
    
    int
    start
    - server index to start with
    
    int
    max
    - Maximum server count
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/ServerService/getServers?SID=VALUE&start=VALUE&max=VALUE
    
    """
    return call("getServers", SID, start, max)
    
def getServerCount(SID):

    """
    Method to retrieve the total count of the servers participating in
     cluster
    
    Return Type: int
    
    # Parameters:
    String
    SID
    - session id to identify the user making request
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/ServerService/getServerCount?SID=VALUE
    
    """
    return call("getServerCount", SID)
    
def saveServer(SID, id, name, address, port, user, pass, webapp, protocol, active, comment):

    """
    Method to add/update server
    
    Return Type: long
    
    # Parameters:
    String
    SID
    - session id to identify the user making request
    
    long
    id
    - the id of the server to save
    
    String
    name
    - the name of the server to save
    
    String
    address
    - the address(DNS name or IP) of the server to save
    
    int
    port
    - the http port of the slave
    
    String
    user
    - REST user to access the slave
    
    String
    pass
    - REST pass to access the slave
    
    String
    webapp
    - webapp name of the OpenMeetings instance
    
    String
    protocol
    - protocol to access the OpenMeetings instance
    
    Boolean
    active
    - if the server currently participates in the cluster or not
    
    String
    comment
    - comment for the server
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/ServerService/saveServer?SID=VALUE&id=VALUE&name=VALUE&address=VALUE&port=VALUE&user=VALUE&pass=VALUE&webapp=VALUE&protocol=VALUE&active=VALUE&comment=VALUE
    
    """
    return call("saveServer", SID, id, name, address, port, user, pass, webapp, protocol, active, comment)
    
def deleteServer(SID, id):

    """
    Method to delete server
    
    Return Type: boolean
    
    # Parameters:
    String
    SID
    - session id to identify the user making request
    
    long
    id
    - the id of the server to delete
    
    
    # Sample Call/URL:
    http://localhost:5080/openmeetings/services/ServerService/deleteServer?SID=VALUE&id=VALUE
    
    """
    return call("deleteServer", SID, id)
    
