import socket 
import json
host = "127.0.0.1"
porta = 8888 
a = input('A: ')
b = input('B: ')
op = input('Operação (+, -, * , /): ')
dados = { "a": a, "b": b, "op" : op }
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, porta))
mensagem = json.dumps(dados)
s.send(mensagem.encode()) 
print ('Mensagem enviada.. Aguardando resposta...') 
resposta = s.recv(1024) 
resposta = json.loads(resposta.decode())
print ('Resposta: ')
print (resposta['resposta'])
print ('Resultado: ')
print (resposta['resultado'])
s.close()