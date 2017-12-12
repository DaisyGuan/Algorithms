>>> import socket
>>> import time
>>> sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> sock.bind(('',0))
>>> sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
>>> while True:
...   m = '{0}\n'.format(time.time())
...   sock.sendto(m,('<broadcast>',5566))
...   time.sleep(5)
...
