import socket
import base64
import zlib
HOST='challenge01.root-me.org'
PORT=52022
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while True:

    data=client.recv(1024).decode('utf-8')
    if not data:
        break
    print(data)
    if "flag" in data.lower():
        print("FLAG :", data)
        break
    
    
    data_isole=data.split("'")[1]
    
    data_decode=base64.b64decode(data_isole)
    data_decompress=zlib.decompress(data_decode).decode('utf-8')
    client.sendall((data_decompress + "\n").encode('utf-8'))
    
    print(repr(data_decompress))
    
