#Nikhil Ramesh
#31499350
#Section 02
#! /usr/bin/env python3
# Echo Client
import sys
import socket
import time
import struct

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = 10
#data = 'X' * count # Initialize data to be sent

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server
dropped = 0
trip_times = []
for i in range(1,count+1):
    data = struct.pack('!ii',1,i)
    print("Pinging   " + host + ", " + str(port))
    initial_time = time.time()
    clientsocket.sendto(data,(host, port))
    clientsocket.settimeout(2)
    try:
        dataEcho, address = clientsocket.recvfrom(count)
        ending_time = time.time()
        elapsed_time = ending_time - initial_time
        trip_times.append(elapsed_time)
        print("Ping message number " + str(i) + " RTT: " + str(elapsed_time) + " secs")
    except socket.error:
        dropped = dropped + 1
        print("Ping message number " + str(i) + " timed out")
#Receive the server response
#dataEcho, address = clientsocket.recvfrom(count)
#print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
print("Statistics: ")
avgtime = 0
mintime = 10000
maxtime = 0
sumtime = 0
packetloss = dropped/count * 100
for elem in trip_times:
    sumtime = elem + sumtime
    if elem < mintime:
        mintime = elem
    if elem > maxtime:
        maxtime = elem
avgtime = sumtime / (count - dropped)

print("Average RTT: " + str(avgtime) + "secs")
print("Max RTT: " + str(maxtime) + "secs")
print("Min RTT: " + str(mintime) + "secs")
print("Dropped " + str(packetloss) + "% of packets")
#Close the client socket
clientsocket.close()
