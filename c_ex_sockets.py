#Create a connection that doesn't get any info yet, just like dialing the phone. Methods are Socket, Connect, Send and Receive
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # No idea what this does, but keep it this way. This is like the file handler
mysock.connect(('data.pr4e.org',80)) # This connects to the Host, first paramenter on the Port second paramenter. This opens a connection. This is like the open file

# For Web Comms, the protocol is HTTP, the language into which the connection create above communicates
# Create the GET, this the message to be sent via the connection opened above
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # Encode converts from unicode to UTF-8 which is the language needed by the HTTP
# Send this cmd to the server
mysock.send(cmd)

# We loop through the connection in order to receive all the info from the server, this can take more than one receiving stance that is why we use the while loop
while True:
    # Save into data a receive of up to 512 lines
    data = mysock.recv(512)
    # If the data is smaller than one, then we break the connection to the server, since that is the end of it
    if (len(data) < 1):
        break
    # If data was in place, then we decode the message sent by the server
    print(data.decode()) # Decode from UTF-8 back into Unicode to read and print
# We close the connection
mysock.close()