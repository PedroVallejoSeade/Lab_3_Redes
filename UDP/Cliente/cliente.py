import socket
from datetime import datetime
import logging
import os
import hashlib

if __name__ == '__main__':
    dateTimeObj = datetime.now()
    logging.basicConfig(
        filename=f"Logs/{dateTimeObj.year}-{dateTimeObj.month}-{dateTimeObj.day}-{dateTimeObj.hour}-{dateTimeObj.minute}-{dateTimeObj.second}.log", level=logging.INFO)

    host = socket.gethostbyname(socket.gethostname())
    port = 4455
    addr = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data = '[-] Conexion UDP con cliente exitosa'
    data = data.encode('utf8')
    client.sendto(data, addr)

    data, addr = client.recvfrom(1024)
    data = data.decode('utf8')
    item = data.split("_")
    numCliente = item[0]
    cantConexiones = item[1]
    nomArchivo = item[2].split("/")[1]
    tamArchivo = item[3]
    hashServidor = item[4]

    data, addr = client.recvfrom(1024)
    data = data.decode('utf8')
    print(data)

    print(
        f'[+] El servidor asigno el numero de cliente {numCliente} de un total de {cantConexiones} clientes')
    print(
        f'[+] Se recibira el archivo "{nomArchivo}" que tiene un tamanio de {tamArchivo} bytes')
    print(
        f'[+] Se recibe el siguiente valor de hash del servidor: {hashServidor}')
    logging.info(f'Numero de cliente asignado: {numCliente}')
    logging.info(f'Numero total de clientes: {cantConexiones}')
    logging.info(f'El nombre del archivo a recibir es: {nomArchivo}')
    logging.info(f'El tamanio del archivo a recibir es de: {tamArchivo} bytes')

    numPaquetesRecibidos = 0
    tiempoTranferenciaI = datetime.now()
    with open(f"ArchivosRecibidos/{numCliente}–Prueba-{cantConexiones}.txt", "w") as f:
        while True:
            data, addr = client.recvfrom(1024)
            if(numPaquetesRecibidos == 0):
                tiempoTranferenciaI = datetime.now()
                print('[+] Comienza la transferencia del archivo')

            if not data:
                break

            data = data.decode('utf8')
            f.write(data)
            numPaquetesRecibidos += 1
    tiempoTranferenciaF = datetime.now()
    print('[+] Termina la transferencia del archivo')
    tiempoTranferencia = tiempoTranferenciaF-tiempoTranferenciaI
    tamArchivoRecibido = os.path.getsize(
        f"ArchivosRecibidos/{numCliente}–Prueba-{cantConexiones}.txt")

    md5 = hashlib.md5()
    with open(f"ArchivosRecibidos/{numCliente}–Prueba-{cantConexiones}.txt", 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            md5.update(data)
    hashCliente = md5.hexdigest()
    entregaArchivoExitosa = True if hashCliente == hashServidor else False
    print(
        f'[+] Se genero el siguiente valor de hash localmente: {hashCliente}')

    data = f'{numCliente}_{entregaArchivoExitosa}'
    data = data.encode('utf8')
    client.sendto(data, addr)
    client.close()

    logging.info(
        f'Al comparar los hash del archivo enviado y el archivo recivido, se concluye que se recibio el archivo correctamente: {entregaArchivoExitosa}')
    logging.info(
        f'El tiempo de transferencia fue: {tiempoTranferencia}')
    logging.info(
        f'Numero de paquetes recibidos: {numPaquetesRecibidos}')
    logging.info(
        f'Numero de bytes recibidos: {tamArchivoRecibido}')
