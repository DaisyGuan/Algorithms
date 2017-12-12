>>> import SocketServer
>>> bh = SocketServer.BaseRequestHandler
>>> class handler(bh):
...   def handle(self):
...     data = self.request.recv(1024)
...     print self.client_address
...     self.request.sendall(data)
...
>>> host = ('localhost',5566)
>>> s = SocketServer.TCPServer(
...   host, handler)
>>> s.serve_forever()
