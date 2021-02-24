#!/usr/bin/env python3

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
a
def invia_comandi(sock_service):#Chiedo i dati al client in un ciclo e poi li invio al server
    while True:
        try:
            n1 = input("Inserisci il primo numero: ")
            n2 = input("Inserisci il secondo numero: ")
            oper = input("Inserisci l'operazione da effettuare(piu / meno / per / diviso): ")
            dati=f"{oper};{n1};{n2}"

        except EOFError:
            print("\nOkay. Exit")
            break
        if not dati:
            print("Non puoi inviare una stringa vuota!")
            continue
        if dati == '0':
            print("Chiudo la connessione con il server!")
            break
        
        dati = dati.encode()

        sock_service.send(dati)

        dati = sock_service.recv(2048)

        if not dati:
            print("Server non risponde. Exit")
            break
        
        dati = dati.decode()

        print("Ricevuto dal server:")
        print(dati + '\n')

        sock_service.close()

def connessione_server(address,port):#in questa funzione inserisco tutti i comandi riguardanti la connessione al server

    sock_service = socket.socket()

    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS,SERVER_PORT)