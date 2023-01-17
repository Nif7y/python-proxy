""" Exists only to test the Proxy.py module

    Run this with the command 'python Client.py' and it will
    download www.testingmcafeesites.com/testcat_ac.html from
    its hosted server. Change the URL on line 28 if needed
"""

import socket

# 1MB buffer size
BUFFER_SIZE = 1048576
#create the server details
serverName = 'localhost'
serverPort = 8080

#create the client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try to connect to the server
print('attempting to connect to server')
try:
    clientSocket.connect((serverName,serverPort))
    print('connection successful')
except:
    print('could not connect to proxy')

#create the request to send to proxy
request = 'GET http://www.testingmcafeesites.com/testcat_ac.html HTTP/1.1'
#encode request as bytes object
request_as_bytes = str.encode(request)

print('attempting to send request')
try:
    clientSocket.send(request_as_bytes)
except:
    print('failed to send')

#receive results from request
try:
    result = (clientSocket.recv(BUFFER_SIZE)).decode('utf-8')
except:
    print('received no response from server')

print('Result of request - ' + '\n' + result)
clientSocket.close()