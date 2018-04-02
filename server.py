# -*- coding: utf-8 -*-
import socket
import threading
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)

def tcplink(sock,addr):
    print ('accept new connection from %s:%s' %addr)
    sock.send('welcome')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        sock.send('Hello,%s!' %data)
    sock.close()
    print 'Connection from %s:%s closed' %addr

while True:
    # 接受一个新连接:
    sock,addr=s.accept()
    # 创建新线程来处理TCP连接:
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()




