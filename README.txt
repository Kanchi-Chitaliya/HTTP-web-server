Please check HTTP-webserver file to check the specifications implemented
Libraries Imported:
socket
threading
sys
os
logging
signal
time
To Run: Enter 127.0.0.1:5044(say)/foo2.jpg
Implemented OOP: All functions are defined in the classes
Used Logging and created a file named "loggers.log"
Implemented POST Method
Client file to check multithreading and pipelining
Version used:python 3.6.2 (implemented on shell)
Conf filename:"ws.conf"
name of root directory:Document_root_directory
Steps:
1) Call class Server from the main function. In server pass the required parameters
2)Create socket and bind to the client.Set a timeout to keep listening. Alos check for error if socket is not created.
3)Create and start thread
4)function for keyboard interrupt : Press Ctrl+C for Interrupt
5)Check if the conf file exists in the current directory
6)Receive request from the client
7)Check HTTP version. Check received Method. Check received for valid port numbers (Between 1024-65535)
8)If the received method is GET, check if file name is given in the request. If not, show Default file
9) Else pick the file extension from the request and match it with the keys in the conf file.
10)Errors Handled:
404: not found -File not present in the dictionary
400: Bad request
501:Not implemented
500: Any other error: Internal Server Error

Client program
created 2 threads
First: to send requests of 100 different files
Second: to send requests of 1 file 100 times


 

