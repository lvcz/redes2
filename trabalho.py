import socket
import os
import sys
import pickle
import time
import thread


PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

peers = list()


def cliente(host):
    dest = (host, PORT)
    first = True
    tcp.connect(dest)
    try:
        while True:        
            lpeers = tcp.recv(1024)        
            recpeers = pickle.loads(lpeers)
            if first:
                meu_host = recpeers[-1]
                print meu_host
                first = False
            print recpeers
    except:
        tcp.close()
        if recpeers[0] == meu_host:
            servidor(meu_host[0])
        else:
            cliente(recpeers[0])

def servidor(host):
    orig = (host, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    print 'Servidor'
    try:
        while True:
            con, cliente = tcp.accept()
            thread.start_new_thread(conectado, tuple([con, cliente]))
    finally:
        tcp.close()


def conectado(con, cliente):
    global peers
    while True:
        print 'Conectado por', cliente
        peers.append(cliente)
        print peers                
        while True:
            try:
                jpeers = pickle.dumps(peers)
                con.sendall(jpeers)                
                time.sleep(2)
            except:
                peers.remove(cliente)
                print 'Finalizando conexao do cliente', cliente
                con.close()
                thread.exit()               
                break








if len(sys.argv) != 3:
    print 'usage: python program.py <-s>(Servidor) <-c> (cliente) <IP>(meu ip se for -s) (ip Servidor)'
elif sys.argv[1] =='-s':
    servidor(sys.argv[2])
elif sys.argv[1] == '-c':
    cliente(sys.argv[2])
    
