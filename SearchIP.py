import socket
socket.getaddrinfo('localhost', 8080)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print ("El nombre de tu pc es: " + hostname)
print("La IP de tu pc es: " + ip)
