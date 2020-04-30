import socket
import sys
from time import perf_counter

s = socket.socket()
host = socket.gethostname()
port = 8080

s.bind((host, port))
s.listen(1)
print("Waiting for 2 connections...")
connection_1, addr_1 = s.accept()
print("Client_1 has connected...")
connection_1.send("Welcome to the chat game".encode())
print("Waiting for 1 connection...")
connection_2, addr1 = s.accept()
print("Client_2 has connected...")
connection_2.send("Welcome to the chat game".encode())
a = []
while True:

    recv_message = connection_1.recv(1024)
    tstart = perf_counter()
    print("Player_1: ", recv_message.decode())
    client_1_msg = str(recv_message.decode())
    connection_2.send(recv_message)

    recv_message = connection_2.recv(1024)
    print("Player_2: ", recv_message.decode())
    client_2_msg = str(recv_message.decode())
    connection_1.send(recv_message)

    a.append(client_1_msg)
    a.append(client_2_msg)
    tend = perf_counter()
    tcalc = tend - tstart
    if ((client_1_msg[- 2:] == client_2_msg[:2]) or (client_2_msg[:2] == client_2_msg[-2:])) and (tcalc < 15):
        continue
    else:
        if tcalc >= 15:
            print("time is up")
        else:
            print("There is a fail")
        s.close()
        sys.exit()
