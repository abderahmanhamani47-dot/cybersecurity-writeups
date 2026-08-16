import socket 
import codecs
PORT=52021
HOST='challenge01.root-me.org'
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
data=client.recv(1024).decode('utf-8')

data_isole=data.split("'")[1]

data_decode=codecs.decode(data_isole, 'rot13')

client.sendall((data_decode+ "\n").encode('utf-8'))
flag=client.recv(1024).decode('utf-8')
print(flag)
