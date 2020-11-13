# Python Program to Get IP Address 
import socket 
hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname) 
print("Your Computer Name is: " + hostname) 
print("Your Computer IP Address is: " + IPAddr) 



# local ip
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("Your Local IP Is: " +local_ip)




# ip lookup for links
import socket
print (socket.gethostbyname("www.google.com"))



# another way to get your local ip
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()



# another way but this took 30 minutes to write
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# same as the above but it is a Version that will also work on LANs without an internet connection
import socket
print((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])


# i wont stop will I, This should work on any LAN that allows UDP broadcast and doesn't require access to an address on the LAN or internet.
import socket
def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]

print (getNetworkIp())
