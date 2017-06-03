import socket
import os
import sys
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

peers = []


def cliente(host):
    dest = (host, PORT)
    tcp.connect(dest)    
    while True:
      #tcp.send (msg)
      peers = tcp.recv(1024)      
    tcp.close()
    if peers[0] == HOST:
        servidor()
    else:
        cliente(msg[0])

def servidor():
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    while True:
        con, cliente = tcp.accept()
        pid = os.fork()
        if pid == 0:
            tcp.close()
            print 'Conectado por', cliente
            peers.append(cliente)
            while True:
                con.sendall(peers)
                #print cliente, msg
            print 'Finalizando conexao do cliente', cliente
            con.close()
            sys.exit(0)
        else:
            con.close()


if len(sys.argv) == 1:
    servidor()
else:
    cliente(sys.argv[1])
    
