#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))

protocollo=["SYN","SYN + ACK", "ACK + data", "ACK for Data"]
step=0
dati=""
while True:
    dati =str(step)+" - " + protocollo[step] 
    print("Invio: '%s'" % dati)
    
    dati = dati.encode()

    sock_service.send(dati)

    dati = sock_service.recv(2048)

    if not dati:
        print("Server non risponde. Exit")
        break
    
    dati = dati.decode()

    print("ricevuto: '%s'" % dati)
    step=int(dati.split("-")[0])
    step+=1
    if step>3:
        break

sock_service.close()