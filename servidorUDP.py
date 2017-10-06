# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets UDP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets
import time

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print "Servidor UDP esperando conexoes na porta %d ..." % (serverPort)
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    if message.find('data')>=0:
        data = str(time.ctime())
        print "Cliente %s enviou: %s, transformando em: %s" % (clientAddress, message, data)
        serverSocket.sendto(data, clientAddress) # envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor
