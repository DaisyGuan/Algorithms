import socket

class UDPServer(object):
    def __init__(self,host,port):
        self._host = host
        self._port = port

    def __enter__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self._host,self._port))
        self._sock = sock
        return sock
   def __exit__(self,*exc_info):
        if exc_info[0]:
            import traceback
            traceback.print_exception(*exc_info)
        self._sock.close()

if __name__ == '__main__':
    host = 'localhost'
    port = 5566
    with UDPServer(host,port) as s:
        while True:
            msg, addr = s.recvfrom(1024)
            s.sendto(msg, addr)


#ViaSocketServer
>>> import SocketServer
>>> bh = SocketServer.BaseRequestHandler
>>> class handler(bh):
...   def handle(self):
...     m,s = self.request
...     s.sendto(m,self.client_address)
...     print self.client_address
...
>>> host = ('localhost',5566)
>>> s = SocketServer.UDPServer(
...   host, handler)
>>> s.serve_forever()
