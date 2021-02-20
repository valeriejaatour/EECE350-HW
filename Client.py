import socket
import time

server = "localhost"
port = 7
request_string = str.encode("Hello")
buffer = 4096


mysocket2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

y=0
address = (server,port)


for x in range(5):
	t1 = (time.time()*1000000)    
	mysocket2.sendto(request_string,address) 
	msg = mysocket2.recvfrom(buffer)
	t2 = (time.time()*1000000)
	t = t2-t1
	y = y + t
	print("RTT number:" + str(t) + "us")

res = y/5
print("RTT avg:" + str(res) + "us")

mysocket2.close