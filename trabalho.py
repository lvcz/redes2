import socket
import os
import sys
import pickle
import time

#HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

peers = list()


def cliente(host):
    dest = (host, PORT)
    tcp.connect(dest)
    jpeers = tcp.recv(1024)
    print jpeers
    recpeers = pickle.loads(jpeers)
    while True:
        #tcp.send (msg)
        lpeers = tcp.recv(1024)
        if lpeers != jpeers:
            jpeers = lpeers
            recpeers = pickle.loads(jpeers)
        #print jpeers
        
    tcp.close()
    if recpeers[0] == HOST:
        servidor()
    else:
        cliente(msg[0])

def servidor(host):
    orig = (host, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    print 'Servidor'
    while True:
        con, cliente = tcp.accept()
        pid = os.fork()
        if pid == 0:
            tcp.close()
            print 'Conectado por', cliente
            peers.append(cliente)
            print peers
            jpeers = pickle.dumps(peers)
            print jpeers
            while True:
                con.sendall(jpeers)
                time.sleep(15)
                #print cliente, msg
            print 'Finalizando conexao do cliente', cliente
            con.close()
            sys.exit(0)
        else:
            con.close()


if len(sys.argv) != 3:
    print 'usage: python program.py <-s>(Servidor) <-c> (cliente) <IP>(meu ip se for -s) (ip Servidor)'
elif sys.argv[1] =='-s':
    servidor(sys.argv[2])
elif sys.argv[1] == '-c':
    cliente(sys.argv[2])
    
