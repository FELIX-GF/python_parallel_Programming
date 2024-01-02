
#1.Acessing Host name and IP address
import socket
host_name = socket.gethostname()
# accessing host name.
print("Host name: %s"%host_name)
# accessing host app address
print ("IP address: %s" %socket.gethostbyname(host_name))

