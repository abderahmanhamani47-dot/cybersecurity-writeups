import socket 
import math
import re


PORT=52002
HOST='challenge01.root-me.org'

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
data=client.recv(1024).decode('utf-8')
numbers=re.findall(r'\d+', data)
n1=numbers[1]
n2=numbers[2]
calcul_final=math.sqrt(int(n1))*int(n2)
result = round(calcul_final, 2)
client.sendall(str(result).encode('utf-8'))
flag=client.recv(1024).decode('utf-8')
print(flag)
