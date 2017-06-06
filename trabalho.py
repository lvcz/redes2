import socket
import os
import sys
import pickle
import time
import thread


PORT = 5000

peers = list()


def cliente(host,port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host, int(port))
    first = True
    tcp.connect(dest)
    try:
        while True:        
            lpeers = tcp.recv(1024)        
            recpeers = pickle.loads(lpeers)
            if first:
                meu_host = recpeers[-1]                
                first = False
            #print recpeers
            print meu_host
    except:
        tcp.close()
       # if recpeers[0] == meu_host:
       #     servidor(meu_host[1])
       # else:
       #     cliente(recpeers[0],)

def servidor(port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    orig = ('',int(port))
    tcp.bind(orig)
    tcp.listen(1)
    print 'Servidor'
    try:
        while True:
            con, host = tcp.accept()
            #thread.start_new_thread(cliente, tuple([host[0], host[1]+1]))
            thread.start_new_thread(conectado, tuple([con, host]))
    finally:
        tcp.close()


def conectado(con, host):
    global peers
    while True:
        print 'Conectado por', host
        peers.append(host)
        #print peers                
        while True:
            try:
                jpeers = pickle.dumps(peers)
                con.sendall(jpeers)                
                time.sleep(2)
            except:
                peers.remove(host)
                print 'Finalizando conexao do cliente', host
                con.close()
                thread.exit()         
                break





thread.start_new_thread(servidor,tuple([sys.argv[1]]))
if len(sys.argv) == 4:
    thread.start_new_thread(cliente,tuple([sys.argv[2],sys.argv[3]]))

while True:
    pass

