#This module handles the networking. You’ll need the built-in socket module here.
#Function: check_port(ip, port)
#Logic: Attempt to connect to the IP/Port. Use a short timeout (e.g., 0.5 seconds).
#Return: Return True if the port is open, and False if it’s closed or timed out.


import socket
def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.settimeout(0.5) 
    
    # Get the status code directly
    # 0 means the connection was successful
    status_code = sock.connect_ex((ip, port))
    
    sock.close()
    
    # Return True ONLY if the status is exactly 0
    if status_code == 0:
        return True
    else:
        return False
