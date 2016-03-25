import socket


target_host = "www.google.com"
target_port = 80

host_ip = socket.gethostbyname(target_host)
# Create the CP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the host and port
    client.connect((host_ip, target_port))
except socket.error:
    print("Failed to connect")

# This is the HTTP command for fetching the main page 
message = "GET / HTTP/1.1\r\n\r\n"

try:    
    client.send(bytes(message, "UTF-8"))
    response = client.recv(4096)    
except socket.error:
    print("Failed to send message")
finally:
    print(response)
    client.close()