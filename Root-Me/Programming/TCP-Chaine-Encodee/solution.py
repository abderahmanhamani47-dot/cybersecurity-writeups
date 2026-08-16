import socket 
import base64


HOST='challenge01.root-me.org'
PORT=52023
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
data=client.recv(1024).decode('utf-8')

data_isole=data.split("'")[1]
print(data_isole)
data_encode=base64.b64decode(data_isole)

resultat_final=data_encode.decode('utf-8')
resultat_finale=resultat_final+'\n'
print(resultat_finale)
client.sendall(resultat_finale.encode('utf-8'))
print("done")
flag=client.recv(1024).decode('utf-8')
print(flag)
