import socket
import threading
import sys
import os
import logging
import signal
import time
class Server():
    def __init__(self): 
        self.host = '' 
        self.port = 5044
        self.threads=[]
        self.create_socket()
    def create_socket(self):
        while(1):
            try:
                signal.signal(signal.SIGINT, self.sigint_handler)
                sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create an INET, STREAMing socket
                sock.bind((self.host,self.port))#bind the socket to a host, and a port
                sock.listen(5)#queue up as many as 5 connect requests
                sock.settimeout(5)
                print ('Serving HTTP on port %s ...' % self.port)
                logging.info("Socket is created")
                self.sock=sock
                self.accept_req()#call accept_req()
            except socket.error as message: 
                if sock: 
                    sock.close() 
                print ("Could not open socket: " + str(message) )
                #logging.info("Could not open socket")
        self.conn.close()        
    def accept_req(self):
        while 1:
            conn,addr=self.sock.accept()#accept Request
            if conn:
                thr_multiple=Multiple(conn,addr)
                thr_multiple.setDaemon(True)    #create thread and start it
                thr_multiple.start()
                self.threads.append(thr_multiple)       #append the threads
                
            for elements in self.threads:       
                elements.join()
        self.conn.close()
    def sigint_handler(self,signal, frame):     #function for keyboard interrupt 
        print ("Interrupted")
        logging.error("Keyboard Interrrupted")
        sys.exit(0)

class Multiple(threading.Thread):
    def __init__(self,conn,addr):
        threading.Thread.__init__(self)
        print ("client connected at ",conn)
        self.conn = conn 
        self.addr = addr 
        self.size = 65535
    
    def run(self):
        os.chdir("C:\\Users\\kanchi\\Desktop\\pa2\\Programming_Assignment2")
        try:
            if os.path.isfile("ws.conf"):
                request=self.conn.recv(65535)
                print(request.decode())#receive request from the client
                if request:
                    logging.info('The request is obtained ')
                    a1=request.decode()
                    a=a1.split("/")
                    q=a1.split(" ")
                    try :
                        a[2]=="1.1" or a[2]=="1.0"          #check version of HTTP
                        if a[0]=="GET ":
                            y=open("ws.conf","r")
                            yum=y.read()
                            for l in yum:
                                yum1=yum.split()
                            os.chdir(yum1[3])
                            split=q[1][1:]
                            given_cwd=yum1[3]+"\\"+split #concat directory
                            if int(yum1[1])>1024 and int(yum1[1])<65535: #check port number
                                given_file=q[1].split("/")[-1]
                                if given_file=="":      #if no filename,implement default case
                                    os.chdir("C:\\Users\\kanchi\\Desktop\\pa2\\Programming_Assignment2")
                                    y=open("ws.conf","r")
                                    yy=y.read()
                                    for lh in yy:
                                        y1=yy.split()           #pick root directory from conf file
                                    if os.path.isfile(y1[5]):   #check if the file exists
                                        x1=open(y1[5],"rb")
                                        x2=x1.read()
                                        sz=os.path.getsize(y1[5])
                                        ze="HTTP/1.1 200 OK\nContent-Type:text/html\nContent-Length:"+str(sz)+"\n\n"
                                        self.conn.send(ze.encode() +x2)
                                        self.conn.close()
                                    else:
                                        logging.error("Default file does not exist in current directory")
                                elif given_file.find(".")==-1: #if no extension is given
                                    logging.error("no extension")
                                    zem="HTTP/1.1 501 Not implemented\nContent-Type: text/html\n\n<html><body>501 Not implemented <error type><requested data></body></html>"
                                    self.conn.send(zem.encode())
                                    self.conn.close()
                                    
                                elif os.path.isfile(given_cwd):
                                
                                    if a[1]!="HTTP": #if filename is present go to the directory
                                        
                                        os.chdir("C:\\Users\\kanchi\\Desktop\\pa2\\Programming_Assignment2")  
                                        k=q[1].split(".")
                                        k="."+str(k[1]) 
                                        w=q[1].split("/")[-1]
                                        fh=open("ws.conf","r")
                                        file_type={}            #create dictionary to find extension in the conf file
                                        for line in fh:
                                            (content_type,s)=line.split()
                                            file_type[content_type]=s           
                                        if k in file_type.keys():
                                            try:
                                                fh=open(given_cwd,'rb')
                                                http_response=fh.read()
                                                get_size=os.path.getsize(given_cwd)
                                                z="HTTP/1.1 200 OK\nContent-Type:"+file_type[k]+"\n"+"Content-Length:"+str(get_size)+"\n\n"
                                                self.conn.send(z.encode() +http_response)
                                                self.conn.close() 
                                            except:
                                                logging.error("File type not found")
                                        else:
                                            logging.error("invalid extension")
                                            zx="HTTP/1.1 501 NOT Implemented\nContent-Type: text/html\n\n<html><body>501 Implemented<<error type>>:<<requested data>></body></html>"
                                            self.conn.send(zx.encode())
                                            self.conn.close() 
                                else:
                                    logging.error("404 not found :file not present in the directory")
                                    zx="HTTP/1.1 404 NOT FOUND\nContent-Type: text/html\n\n<html><body>404 NOT FOUND REASON:File Does not exist:<<request method>></body></html>"
                                    self.conn.send(zx.encode())
                                    self.conn.close() 
                            else:
                                logging.error("use port number between 1024 and 65535") 
                        elif a[0]=="POST ":
                            logging.info("implement post method")
                            req=a1.split("\n")
                            abc=req[12].split("=")
                            zs="HTTP/1.1 200 0K\nContent-Type:text/html\n\n<h1>POST DATA</h><pre><html><body>NAME: "+abc[1]+"</body></html></pre>"
                            self.conn.send(zs.encode())
                            self.conn.close()
                        else:
                            logging.error("Error 400:Bad Request") 
                            zer="HTTP/1.1 400 BAD REQUEST\nContent-Type: text/html\n\n<html><body>400 BAD REQUEST REASON:Invalid Method:<<request method>></body></html>"
                            self.conn.send(zer.encode())
                            self.conn.close()  
                        
                    except:
                            logging.error("invalid http version")
                            
            else:
                logging.error("conf file not found")
                sys.exit()  
        except:
            logging.error("Internal Server Error") 
            zer="HTTP/1.1 500 Internal Server Error\nContent-Type: text/html\n\n<html><body>500 Internal Server Error:Cannot allocate memory<<request method>></body></html>"
            self.conn.send(zer.encode())
            self.conn.close()       

if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", filename="loggers.log",level=logging.DEBUG)
    server=Server()
    



