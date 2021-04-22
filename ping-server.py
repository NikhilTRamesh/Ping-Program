#Nikhil Ramesh
#31499350
#Section 02
#! /usr/bin/env python3
# Echo Server
import sys
import socket
import time
import struct
import random

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    unpacked = struct.unpack('!ii', data)
    print("Receive data from client " + address[0] + ", " + str(address[1]) + ": from Ping #" + str(unpacked[1]))

    # Echo back to client
    time.sleep(1)
    data = struct.pack('!ii',2,unpacked[1])
    picker = random.randint(0,10)
    if picker == 1 or picker == 6:
        print("Dropping packet")
    else:
        print("Sending data to   client " + address[0] + ", " + str(address[1]) + ": from Ping #" + str(unpacked[1]))
        serverSocket.sendto(data,address)
