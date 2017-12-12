>>> import socket
>>> import time
>>> sock = socket.socket(
...   socket.AF_INET,
...   socket.SOCK_DGRAM)
>>> host = ('localhost',5566)
>>> while True:
...   sock.sendto("Hello\n",host)
...   time.sleep(5)
...
