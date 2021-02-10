#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

def ricevi_comandi(sock_listen):#in questa funzione inserisco il ciclo in loop che attende dati dal client e che invia la risposta
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nAspetto di ricevere i dati ")

        while True:
            dati = sock_service.recv(2048)

            if not dati:
                print("Fine dati dal client. Reset")
                break
            
            dati = dati.decode()
            print("Ricevuto: '%s'" % dati)
            if dati=='0':
                print("Chiudo la connessione con " + str(addr_client))
                break
            
            risultato=0
            oper,n1,n2= dati.split(";")
            if oper=="piu":
                risultato=int(n1)+int(n2)

            if oper=="meno":
                risultato=int(n1)-int(n2)

            if oper=="per":
                risultato=int(n1)*int(n2)

            if oper=="diviso":
                risultato=int(n1)/int(n2)
            
            dati = f"Risposta a : {str(addr_client)}. Il risultato dell'operazione({n1} {oper} {n2}) è :{risultato} "

            dati = dati.encode()

            sock_service.send(dati)

        sock_service.close()

def avvia_server(indirizzo,porta):#In questa funzione inserisco tutti i comandi relativi alla creazione e avvio del server
    sock_listen = socket.socket()

    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

    sock_listen.listen(5)

    print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))

    ricevi_comandi(sock_listen)


if __name__=='__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)