import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
s.connect((host,port))
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data)
    print s.recv(1024)

s.send('exit')
print s.recv(1024)
s.close()