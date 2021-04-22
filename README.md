# Ping-Program

UDP Ping Client and Server Python Program

Ping Client utilizes UDP sockets to send a message containing 2 2-byte integers encoded in network-byte order (Big Endian). 
First byte represents message type: 1 for Ping Request, 2 for Ping Response.  
Second byte is a unique integer value representing the ping's sequence number.  
Records time between message request and response in order to calculate Round Trip Time Delay, Packet Loss %, and Min/Max RTT of all acknowledged Ping Packets.

Ping Server utilizes UDP sockets to read for client pings on loop and respond to them in the sequence they arrive.
