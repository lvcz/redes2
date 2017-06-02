import socket
import os
import sys
from threading import Thread



class Servidor(Thread):
   def __init__(self,HOST,PORT):
      Thread.__init__(self);
      self.HOST=HOST
      self.PORT=PORT
   def run(self):
      tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      orig = (self.HOST, self.PORT)
      tcp.bind(orig)
      tcp.listen(1)
      while True:
        con, cliente = tcp.accept()
        pid = os.fork()
        if pid == 0:
            tcp.close()
            print 'Conectado por', cliente
            while True:
                msg = con.recv(1024)
                if not msg: break
                print cliente, msg
            print 'Finalizando conexao do cliente', cliente
            con.close()
            sys.exit(0)
        else:
            con.close()




class cliente(Thread):
   def __init__(self,HOST,PORT):
      Thread.__init__(self)
      self.HOST=HOST
      self.PORT=PORT

   def run (self):
      tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      dest = (self.HOST, self.PORT)
      tcp.connect(dest)      
      msg = raw_input()
      while True:
         tcp.send (msg)
         msg = raw_input()
      tcp.close()





