import socket
import threading
import os
import hashlib


def manejadorCliente(servidor, addr, nomArchivo):
    with open(nomArchivo, "r") as f:
        while True:
            data = f.read(1024)
            data = data.encode('utf-8')

            if not data:
                servidor.sendto(data, addr)
                break

            server.sendto(data, addr)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4455

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((host, port))
    print('[+] Servidor UDP inicializado')

    numConexionesAct = 0
    numConexionesReq = 0
    numConexionesVal = False

    while(not numConexionesVal):
        numConexiones = input("[+] Ingrese el numero de clientes (1-25):")
        if(int(numConexiones) >= 1 and int(numConexiones) <= 25):
            numConexionesVal = True
            print(f'[+] Se escogio total de {numConexiones} conexiones')
        else:
            print(f"[+] {numConexiones} no es un numero valido de conexiones")

    numConexionesReq = int(numConexiones)

    archivoValido = False
    nomArchivo = ""
    tamArchivo = 0
    while (not archivoValido):
        archivo = input("[+] Escoja entre el archivo 1(100MB) o 2(250MB):")
        if(int(archivo) == 2):
            nomArchivo = "ArchivosEnvio/250MB.txt"
            tamArchivo = os.path.getsize(nomArchivo)
            archivoValido = True
        elif(int(archivo) == 1):
            nomArchivo = "ArchivosEnvio/100MB.txt"
            tamArchivo = os.path.getsize(nomArchivo)
            archivoValido = True
        else:
            print("El archivo escogido no es valido")
        print(f'[+] Se escogio el archivo: {nomArchivo}')

    print(
        f'[+] Se necesitan {numConexiones} conexiones para empezar la transferencia de archivos')

    md5 = hashlib.md5()
    with open(nomArchivo, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            md5.update(data)
    hashServidor = md5.hexdigest()

    hilos = []

    while(numConexionesAct < numConexionesReq):
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        print(data)
        numConexionesAct += 1

        data = f'{numConexionesAct}_{numConexionesReq}_{nomArchivo}_{tamArchivo}_{hashServidor}'
        data = data.encode("utf-8")
        server.sendto(data, addr)

        data = '[-] Inicializacion con el servidor exitosa'
        data = data.encode("utf-8")
        server.sendto(data, addr)

        hilo = threading.Thread(target=manejadorCliente,
                                args=(server, addr, nomArchivo))
        hilos.append(hilo)

        print(f"[+] Inicializacion con el cliente {numConexionesAct} exitosa")
        if(numConexionesReq - numConexionesAct == 0):
            print(
                f'[+] Comienza la transferencia de archivos')
        else:
            print(
                f'[+] Se necesitan {numConexionesReq-numConexionesAct} conexiones para empezar la transferencia de archivos')

    i = 0
    while (i < numConexionesAct):
        hilos[i].start()
        i += 1
