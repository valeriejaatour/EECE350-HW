import socket
import datetime

client = "localhost"
port = 7
buffer = 4096


mysocket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

address = (client,port)
mysocket1.bind(address)

while True:
    tuple = mysocket1.recvfrom(buffer)
    if (tuple[0] == str.encode("Hello")):                                 
      now = datetime.datetime.now()        
      print("date and time:", now)
      mysocket1.sendto(str.encode("Hello"),tuple[1])