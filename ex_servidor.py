import socket
import json
HOST = ''	    # Em branco para todas interfaces
PORTA = 8888	# > 1023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()
print("Running... Press Control-C to exit")
try:
  while (True):
    conn, addr = s.accept()
    print ("Concectado " + addr[0] + ":" + str(addr[1]))
    dados = conn.recv(1024) 
    print ("Mensagem recebida: " + dados.decode())
    dados = json.loads(dados.decode())
    print ("Calculo : " + dados['a'] + ' ' + dados['op'] + ' ' + dados['b'])
    resultado = 0
    erro = False
    if dados['op'] == "+":
        resultado = int(dados['a']) + int(dados['b'])
    else: 
        if dados['op'] == "-":
            resultado = int(dados['a']) + int(dados['b'])
        else: 
            if dados['op'] == "*":
                resultado = int(dados['a']) + int(dados['b'])
            else: 
                if dados['op'] == "/":
                    resultado = int(dados['a']) + int(dados['b'])
                else:
                    print("Operação Inválida")
                    erro = True
    if not erro:
        print ("Resultado : " + str(resultado))
        resposta = { "resposta": "OK", "resultado": resultado}
    else:
        resposta = { "resposta": "ERRO", "resultado": 0}
    resposta_json = json.dumps(resposta)
    conn.send(resposta_json.encode())
    conn.close() 
except KeyboardInterrupt:
  s.close()