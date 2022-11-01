
import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect to the client
client.connect((target_host, target_port))

# send some data
client.sendto(b"This is a test data in udp", (target_host, target_port))
# receive some data
data, addr = client.recvfrom(4096)

print(data)
# now set a listener on port 80
# nc -ulp 80
