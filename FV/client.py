import socket
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

entrada = ClientMultiSocket.recv(1024)

while entrada != "QUIT":
    entrada = input('>> ')
    ClientMultiSocket.send(str.encode(entrada)) # Envia comando ao server
    resposta = ClientMultiSocket.recv(1024).decode() # Recebe processamento do servidor
    print('Response from server:\n' + resposta)
    entrada = input('>> ')

# Processa QUIT
ClientMultiSocket.send(str.encode(entrada)) # Envia comando ao server
resposta = ClientMultiSocket.recv(1024).decode() # Recebe
print('Response from server:\n' + resposta)

ClientMultiSocket.close()