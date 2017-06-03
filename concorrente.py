import socket
import os
import sys
from threading import Thread

def conectado(con, cliente):
    print 'Conectado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()
    thread.exit()

def Servidor(HOST,PORT):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    orig = (HOST, PORT)

    tcp.bind(orig)
    tcp.listen(999)

    while True:
        con, cliente = tcp.accept()
        thread.start_new_thread(conectado, tuple([con, cliente]))
    tcp.close()


def Cliente (self):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (self.HOST, self.PORT)
    tcp.connect(dest)      
    while True:
        tcp.send (msg)
        msg = raw_input()
    tcp.close()


    Servidor('',5000)



