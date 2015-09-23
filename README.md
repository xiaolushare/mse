# mse
Python module to interface with Cisco MSE

##Functions:
###getClient(string server, string user, string password, string client)
 *Returns a single WirelessClientLocation based on the search 'client'.*

###getClients(string server, string user, string password)
 *Returns a list of WirelessClientLocation from list of server.*

###getAllClients(string user, string password)
 *Returns a list of WirelessClientLocation from list of servers.*
 
##TODO:
  *Combine getClients and getAllClients, let it accept either a single string or list of strings of server addresses.*
