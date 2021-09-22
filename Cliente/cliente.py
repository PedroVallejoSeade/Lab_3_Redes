import socket
import logging
from datetime import datetime
import hashlib

IP = socket.gethostbyname(socket.gethostname())
PUERTO = 8888
DIRECCION = (IP, PUERTO)
TAMANIO = 1024
FORMATO = "utf-8"


def main():
    dateTimeObj = datetime.now()
    logging.basicConfig(
        filename=f"Logs/{dateTimeObj.year}-{dateTimeObj.month}-{dateTimeObj.day}-{dateTimeObj.hour}-{dateTimeObj.minute}-{dateTimeObj.second}.log", level=logging.INFO)

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(DIRECCION)

    data = cliente.recv(TAMANIO).decode('utf-8')
    item = data.split("_")
    NOM_ARCHIVO = item[0]
    TAM_ARCHIVO = int(item[1])
    ID = item[2]
    NUM_CONEXIONES = item[3]
    hashServidor = item[4]
    print(hashServidor)

    print("[+] Nombre y tamanio del archivo recivido del servidor")
    cliente.send("Nombre y tamanio del archivo recivido".encode(FORMATO))

    with open(f"ArchivosRecibidos/{ID}-Prueba-{NUM_CONEXIONES}", "w") as f:
        while True:
            data = cliente.recv(TAMANIO).decode(FORMATO)

            if not data:
                break

            f.write(data)
            cliente.send("Archivo recivido".encode(FORMATO))

    ## HASHING ##
    BUF_SIZE = 1024  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()

    with open(f"ArchivosRecibidos/{ID}-Prueba-{NUM_CONEXIONES}", 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)

    hashCliente = md5.hexdigest()
    print(hashCliente)

    if(hashCliente == hashServidor):
        print(
            "[+] Se comparo los hashing del servidor y del cliente y el archivo llego correctamente")
        # cliente.send('ENVIO EXITOSO'.encode(FORMATO))
    else:
        print("[+] Se comparo los hashing del servidor y del cliente y el archivo NO llego correctamente")
        # cliente.send('ENVIO FALLIDO'.encode(FORMATO))

    ## HASHING ##

    cliente.close()


if __name__ == "__main__":
    main()
