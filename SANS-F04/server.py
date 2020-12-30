import socket
import hashlib
from threading import *


# variables set, v is used as counter for passcheck func,
server = '127.0.0.1'
port = 8154
# setup of socket listener on server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server,port))
listen = s.listen(0)
print 'Server listening for connections'
# class created to handle each client session in a thread
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.passw=None
        self.result=None
        self.sock = socket
        self.addr = address
        self.start()
    # function to check password
    def passcheck(self,passw):
        passw=passw.strip('\n')
        passw=list(passw)
        v=1
        result=''
        # dictionary of correct password hashes and location
        dict={1:'5206560a306a2e085a437fd258eb57ce',2:'dd7536794b63bf90eccfd37f9b147d7f',3:'8d9c307cb7f3c4a32822a51922d1ceaa',4:'b9ece18c950afbfa6b0fdbfa4ff731d3'}
        #loop runs turning each entered password into hash comparing to dictionary of password

        for i in passw:
            i=hashlib.md5(i)
            if i.hexdigest()==dict[v] and len(passw)<5:
                # had issues with format specifier in print getting assigned to variables
                # this way it works just have to set var and print
                result+='Processing %s: ' %(v)
                #print 'v value is:',v
                #could be potential issue with it saying it worked on early exit
                failed=0
            else:
                result='Unexpected Command Value\n'
                #print v
                failed=1
                break
            if v < 5:
                v+=1
                print 'v value is:',v
            else:
                break
        if failed==0 and len(passw) == 4:
            failed=0
        else:
            failed=1
        print 'v value is:',v
        self.passw=result
        self.result=failed
    def run(self):
        while 1:
            self.sock.send("ICS Super Controller v1.3\nPlease Supply initialisation command. Commands are limited to size(4)\n")
            passw=self.sock.recv(1024).decode()
            print(self.passcheck(passw))
            self.sock.send(self.passw)
            print 'self result',self.result
            # if correct password welcome message if not error and exit
            if self.result == 0:
                self.sock.send(b'Welcome Flag: 0xB33F\n')
            elif self.result == 1:
                self.sock.send(b'Error wrong password enter again\n')
#main loop runs accepts connect and sends to client class
while 1:
    clientsocket,address = s.accept()
    client(clientsocket,address)
