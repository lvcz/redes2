#Trabalho de Redes de computadores 2 -UFPR
#Autores:
#Leonardo Vinicius Carvalho Zanella GRR20103241
#Marcio Andreatti GRR20103669

import socket
import os
import sys
import pickle
import time
import thread


class Peer(object):
    """Definicao do objeto Peer"""
    def __init__(self, id,ip,porta,ativo):
        self.id = id
        self.ip = ip
        self.porta = porta
        self.ativo = ativo
        

peers = list()


#envia heartbeats
def envia_heartbeat(peer,id):
    data = envia(peer,'3'+str(id))
    if not data:
        for p in peers:
            if p.id == peer.id:
                print 'peer inativo ', peer.id
                p.ativo = False


def elege_lider():
    for p in peers:
        if p.ativo:
            return p.id

#retorna se existe algum peer inativo na lista
def alguem_desconectado():
    return any(p.ativo == False for p in peers)

# ativa o peer na lista
def ativa_peer(peer):
    for p in peers:
        if peer == p :
            p.ativo = True

#Assim que o peer 0 recebeu a confirmacao de todos envia mensagem para os peers confirmando que estam ativos para eleicao do lider
def ativa_todos():
    for p in peers:
        p.ativo = True

def cliente():
    #enquanto nao estiver todos conectados
    print 'aguardando todos os peers'
    while alguem_desconectado():
        # peer de id 0 cuida verifica se os outros peers estao conectados
        if peer0.id == 0:
            for p in peers:
                #pega os peers inativos e envia mensagem
                if not p.ativo:                   
                    msg = envia(p,'1')
                    #se recebe mensagem de retorno ativa o peer no array
                    if msg:
                        ativa_peer(p)
                        print 'peer conectado:', p.id
            if not alguem_desconectado():
                #se todos os peers estao conectados envia mensagem para os peers ativarem suas listas
                for p in peers:
                    envia(p,'ativos')
    print'todos os peers estao conectados'
    lider = -1
    while True:
        #guarda o valor do ultimo lider
        ultimo_lider = lider
        #elege o novo lider
        lider = elege_lider()
        if ultimo_lider != lider:
            #se o lider mudar envia mensagem avisando que o lider mudou
            for p in peers:
                envia (p,'4'+str(lider))
        for p in peers:
            #envia heartbeats para os peers ativos
            if p != peer0 and p.ativo:
                envia_heartbeat(p,peer0.id)
        time.sleep(3)


#funcao que envia mensagem para o peer solicitado
def envia(peer,mensagem):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (peer.ip, peer.porta)
    
    try:
        tcp.connect(dest)
    except:
        return None
    try:
        tcp.sendall(mensagem)
        confirm = tcp.recv(1024)
    finally:
        tcp.close()
        if confirm:
            return confirm
        else:
            return None


# Funcao que abre socket e fica escutando  na porta do peer0
def servidor(peer):
    global peers
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    orig = (peer.ip,peer.porta)
    tcp.bind(orig)
    tcp.listen(1)
    while True:
        con, host = tcp.accept()
        try:
            msg = con.recv(1024)
            #flag 1 indica a primeira conexao
            if msg == '1':
                con.sendall('ok')
            #se recebe ativos ativa todos os peers 
            if msg == 'ativos':
                ativa_todos()
            #flag 3 indica heartbeart
            if msg[:1] == '3':
                con.sendall('ok')
                print 'Heartbeat do id:',msg[1:]
            #se recebe uma mensagem com flag 4 indica uma troca de lider
            if msg[:1] =='4':
                print 'Lider Alterado, novo lider: ', msg[1:]


           
        finally:
            con.close()


#main
if len(sys.argv) < 10:
    print 'usage: python trabalho <meu id> <meu ip> <minha porta> <numero peer 2> <ip> <numero porta 2> <numero peer 3> <ip> <numero porta 3> <numero peer 4> <ip> <porta 4>'
else:
    peer0 = Peer(int(sys.argv[1]),sys.argv[2],int(sys.argv[3]),True)
    peers.append(peer0)
    peer1 = Peer(int(sys.argv[4]),sys.argv[5],int(sys.argv[6]),False)
    peers.append(peer1)
    peer2 = Peer(int(sys.argv[7]),sys.argv[8],int(sys.argv[9]),False)
    peers.append(peer2)
#como o quarto peer e opcional esse if trata disso
if len(sys.argv) == 13:
    peer3 = Peer(int(sys.argv[10]),sys.argv[11],int(sys.argv[12]),False)
    peers.append(peer3)

#ordena a lsita de peers por id
peers.sort(key=lambda x: x.id, reverse=False)


print '----------------------------------------------------------------------------'
print 'Inciando a execucao do programa como o peer de id:' , peer0.id
print '----------------------------------------------------------------------------'

#inicia as threads de servidor e cliente
thread.start_new_thread(servidor,tuple([peer0]))
thread.start_new_thread(cliente,tuple())



while True:
    pass

