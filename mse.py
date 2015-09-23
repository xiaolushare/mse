import json
import urllib2

mseServers=[
            '1.2.3.4',
            '5.6.7.8',
            '9.10.11.12'
           ]

def getClients(server, user, password):
 passwordManager = urllib2.HTTPPasswordMgrWithDefaultRealm()
 passwordManager.add_password(None,"https://"+server+"/",user,password)

 authHandler = urllib2.HTTPBasicAuthHandler(passwordManager)
 opener = urllib2.build_opener(authHandler)
 urllib2.install_opener(opener)

 request = urllib2.Request("https://"+server+"/api/contextaware/v1/location/clie                                                                             nts",headers={'Accept' : 'application/json'})
 pageHandle = urllib2.urlopen(request)
 page= json.load(pageHandle)

 entries=page['Locations']['entries']

 while page['Locations']['totalPages'] != page['Locations']['currentPage']:
  request = urllib2.Request(page['Locations']['nextResourceURI'],headers={'Accep                                                                             t' : 'application/json'})
  pageHandle = urllib2.urlopen(request)
  page= json.load(pageHandle)
  entries=entries+page['Locations']['entries']

 return entries

def getClient(server, user, password, client):
 passwordManager = urllib2.HTTPPasswordMgrWithDefaultRealm()
 passwordManager.add_password(None,"https://"+server+"/",user,password)

 authHandler = urllib2.HTTPBasicAuthHandler(passwordManager)
 opener = urllib2.build_opener(authHandler)
 urllib2.install_opener(opener)

 request = urllib2.Request("https://"+server+"/api/contextaware/v1/location/clie                                                                             nts/"+client,headers={'Accept' : 'application/json'})
 pageHandle = urllib2.urlopen(request)
 return json.load(pageHandle)['WirelessClientLocation']

def getAllClients(user, password):
 clients=[]
 for server in mseServers:
  for client in getClients(server, user, password):
   clients.append(WirelessClientLocation(client,server))
 return clients

class MapInformation:
 def __init__(self,json):
  self.imageName=         json['Image']['imageName']
  self.floorRefId=        json['floorRefId']
  self.offsetX=           json['Dimension']['offsetX']
  self.offsetY=           json['Dimension']['offsetY']
  self.height=            json['Dimension']['height']
  self.width=             json['Dimension']['width']
  self.length=            json['Dimension']['length']
  self.unit=              json['Dimension']['unit']
  self.mapHierarchyString=json['mapHierarchyString']

class MapCoordinatePair:
 def __init__(self,json):
  self.y=json['y']
  self.x=json['x']
  self.unit=json['unit']

class WirelessClientStatistics:
 def __init__(self,json):
  self.currentServerTime= json['currentServerTime']
  self.lastLocatedTime=   json['lastLocatedTime']
  self.firstLocatedTime=  json['firstLocatedTime']

class WirelessClientLocation:
 def __init__(self,json,server):
  self.mseServer=                                server
  self.userName=                                 json.get('userName','N/A')
  self.macAddress=                               json['macAddress']
  self.isGuestUser=                              json['isGuestUser']
  self.Statistics=      WirelessClientStatistics(json['Statistics'])
  self.currentlyTracked=                         json['currentlyTracked']
  self.ssId=                                     json.get('ssId','N/A')
  self.dot11Status=                              json['dot11Status']
  self.band=                                     json['band']
  self.MapCoordinate=          MapCoordinatePair(json['MapCoordinate'])
  self.apMacAddress=                             json.get('apMacAddress','N/A')
  self.confidenceFactor=                         json['confidenceFactor']
  self.ipAddress=                                json.get('ipAddress','N/A')
  self.MapInfo=                   MapInformation(json['MapInfo'])
