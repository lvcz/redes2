# Redes 2 – Trabalho PEER TO PEER
 
 
## GRR20103241- Leonardo Vinícius Carvalho Zanella
## GRR20103669 - Márcio Andreatti
 
# Execução:
 
Para executar com 4 peers:
```
  python peer.py <numero peer 1> <ip> <numero porta 1><numero peer 2> <ip> <numero porta 2> <numero peer 3> <ip> <numero porta 3> <numero peer 4> <ip> <porta 4>
  python peer.py <numero peer 2> <ip> <numero porta 2><numero peer 3> <ip> <numero porta 3> <numero peer 4> <ip> <numero porta 4> <numero peer 0> <ip> <porta 0>
  python peer.py <numero peer 3> <ip> <numero porta 3><numero peer 4> <ip> <numero porta 4> <numero peer 0> <ip> <numero porta 0> <numero peer 1> <ip> <porta 1>
  python peer.py <numero peer 4> <ip> <numero porta 4><numero peer 0> <ip> <numero porta 0> <numero peer 1> <ip> <numero porta 1> <numero peer 2> <ip> <porta 2>
 ```
Para executar com 3 peers:
 ```
python peer.py <numero peer 1> <ip> <numero porta 1><numero peer 2> <ip> <numero porta 2> <numero peer 3> <ip> <numero porta 3> 
python peer.py <numero peer 2> <ip> <numero porta 2><numero peer 3> <ip> <numero porta 3> <numero peer 1> <ip> <numero porta 1> 
python peer.py <numero peer 3> <ip> <numero porta 3><numero peer 1> <ip> <numero porta 1> <numero peer 2> <ip> <numero porta 2> 
 ```
 
O trabalho foi realizado com no mínimo 3 e no máximo 4 peers fixos, pois assim ficou melhor a implementação e entendimento do trabalho e threads para instanciar clientes e servidores.
	Cada execução possui o ip e porta dos peers, onde sera aberta a quantidade ideal de threads clientes e  servidores para correta execução conforme execução com 4 ou 3 peers, as quais ficaram esperando os demais peers se conectarem aos em execução, após a conexão é estabelecido a comunicação entre todos, assim o heartbeat é transmitido para todos peer conectados, o qual vai dizer que o mesmo esta ativo ou não, e  o líder com menor índice é eleito, ou seja decidimos qual o peer de memor indice na execução quando atribuímos o id aos mesmos. 
	Foi implementado uma lista com os peers onde contem id, ip e status, quando for verificado que o peer com menor id desconectou, a lista é atualizada e o mesmo retirado, então é realizada uma nova eleição para decidir um novo lider.
 
Definição de funções:
 
- Peer: <br>
recebe como parâmetro object, atribui a um peer id, ip, porta e ativo..
- Envia_heartbit: <br>
recebe como parâmetro peer e id, vai passar aos demais peers o seu hartbit.
- Elege_lider: <br>
recebe como parâmetro  ,após todas as conexões vai verificar o menor id ou após a desconexão do atual lider
- Alguem_desconectado: <br>
não recebe nenhum parametro, verifica se ainda falta alguém a se conectar e começar o envio dos heratbits.
- Ativa_peer: <br>
recebe como parametro peer, muda o status do peer na lista.
- Ativa_todos: <br>
não recebe nenhum parâmetro, verifica se todos os peer estão ativos para começar o envio das meensagens.
- Cliente: <br>
não recebe nenhum parâmetro,instancia uma thread para o cliente se conectar a todos os servidores e transmitir.
- Envia: <br>
recebe como parâmetro peer e mensagem, recebe um peer e uma mensagem que serão codificadas para envio ao servidor pelo cliente.
- Servidor: <br>
recebe como parâmetro peer, instancia uma thread para o servidor ficar escultando ate todos clientes se conectarem.
 
	
 
 
 
