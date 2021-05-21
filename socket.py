import socket
import time
import threading
ip = '192.168.100.201'
port = 1883
port2 = 3008
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server2  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
     
    server.bind((ip, port))
    # server2.bind((ip, port2))
    server.listen(1)
    # server2.listen()
    print('aguardando conexao')
    # (conn , ender) = server.accept()
    # (conn2 , ender2) = server2.accept()
    # response_proto = ender2
    # response_status = '200'
    # response_status_text = 'OK' # this can be random

    #     # sending all this stuff
    # server2.send('%s %s %s' % (response_proto, response_status, \
    #                                                     response_status_text))
    # print(ender2)
    i = 0
    while True:
        (conn , ender) = server.accept()
        # print(conn)
        msg = conn.recv(50000)
        msg = conn.recv(50000)
        print(msg)
        # resposta = msg.decode()
        # separa_dados = resposta.split('&')
        # print(separa_dados)
        # time.sleep(2)
        # i = i+1
        # print(i)
        # (conn2 , ender2) = server2.accept()
        # data, adress = server2.recvfrom(4000)
        # server2.sendto(data,adress)

        # msg2 = conn2.recv(1024)
        # if msg2 == b'':
        #     pass
        # # msg2 = conn2.recv(1024)
        # else:
        #     resposta2 = msg2.decode()
        #     separa_dados2 = resposta2.split('&')
        #     print(separa_dados2)
        #     # server2.send(ender2[0])
        #     # pass
        # # print(msg2)
        
        
    server.close()
except Exception as erro:
    print(erro)
    server.close()
