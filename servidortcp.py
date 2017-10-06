# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets
import os

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para "ouvir" conexoes
print "Servidor TCP esperando conexoes na porta %d ..." % (serverPort)
while 1:
    connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
    sentence = connectionSocket.recv(1024) # recebe dados do cliente
    if sentence.find('obter')>=0:
        dividido = sentence.split(' ')
        abrir = open(dividido[1])
        if abrir >=0:
            arquivo = abrir.read()
            print "Cliente %s enviou: %s, transformando em: %s" % (addr, sentence, arquivo)

            connectionSocket.send(arquivo) # envia para o cliente o texto transformado
        else:
            connectionSocket.send('arquivo nao existe') # envia para o cliente o texto transformado
    else:
        dividido = sentence.split(' ')
        print(os.system(dividido[1]))
        connectionSocket.send('comando executado com sucesso') # envia para o cliente o texto transformado
        connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor
