import signal
import difflib
import filecmp
import socket

from cmd import *
import cgrader

def compile(filep):
    res = subprocess_cmd('gcc main.c -o main')

    if res==0:
        return (True,"berhasil")
    else:
        return (False, res)

#print(compile("dd")[1])
#print (subprocess_cmd('./main < a.in >a.out'))
#print (filecmp.cmp('a.in','a.out',False))
status, msg = cgrader.compile("main.c")
#print(status)
#print(msg)

a = cgrader.runTestCase("/home/nobby/Documents/POJ/testcase/",msg)
print (a)

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# host = "127.0.0.1"
# port = 2567
#
# serversocket.bind((host,port))
#
# serversocket.listen(5)
#
# while(True):
#     clsocket,addr = serversocket.accept()
#     msg = clsocket.recv(64)
#     print(msg)
