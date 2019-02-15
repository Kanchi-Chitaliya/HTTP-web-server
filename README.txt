author:Kanchi Chitaliya
IdentityKey:kach6618
purpose:Programming Assignment 3
Filename:README.txt

Libraries Imported:
socket
threading
sys
os
dns.resolver
signal
time
beautifulsoup
To Run: Enter ngn.cs.colorado.edu (say)
Implemented Link Prefetching: Caching all the content on a given page. Used Beautiful soup to fetch all links on a webpage

Implemented Content Blocking: Blocked pokemon related any data in url or content
				Handled CNAMES using dns resolver
				Send header 403 Forbidden website

Version used:python 3.6.2 

Steps
1)Use sys.argv to accept all the arguments. The first argument is for port number and second for timeout.

2) If no arguments are provided use default port number 80 and for timer use max age from header.

3) Check for valid port number and valid number of arguments.

4)Call class main from the main function.pass the required parameters

5)Create socket and bind to the client.

6)Create and start thread

7)function for keyboard interrupt : Press Ctrl+C for Interrupt

8)block content related to pokemon

9)handle cnames using dns.resolver

10)pick path from request and make required directories after checking if the directory is not present

11)pick max age time and compare with user provided time.Compare the last modified file date and current time.

12) If the time has expired, delete cache because the cache has expired. Check for conditions in cache-control and max-age

13)Check for revalidate in header

14) get ETag from the response. Receive 304 Not Modified and carry out required steps.

15) Prefetched data to save all the folders and related data from the website.

16)Errors Handled:
400: Bad request
501:Not implemented (for methods like=CONNECT, POST,HEAD, PUT, OPTIONS, DELETE, PATCH )




 

