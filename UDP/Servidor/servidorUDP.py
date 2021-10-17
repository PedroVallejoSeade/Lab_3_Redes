import socket
import threading


def manejadorCliente(servidor, addr):
    with open("ArchivosEnvio/100MB.txt", "r") as f:
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
        else:
            print(f"[+] {numConexiones} no es un numero valido de conexiones")

    numConexionesReq = int(numConexiones)
    print(
        f'[+] Se necesitan {numConexiones} para empezar la transferencia de archivos')

    # TODO Se necesita hacer la parte de escoger un archivo

    # TODO Se necesita hacer la parte de hacer el hashing del archivo

    hilos = []

    while(numConexionesAct < numConexionesReq):
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        print(data)
        numConexionesAct += 1
        print(f"[+] Inicializacion con el cliente {numConexionesAct} exitosa")

        data = '[-] Inicializacion con el servidor exitosa'
        data = data.encode("utf-8")
        server.sendto(data, addr)

        hilo = threading.Thread(target=manejadorCliente, args=(server, addr))
        hilos.append(hilo)

    i = 0
    while (i < numConexionesAct):
        hilos[i].start()
        i += 1

    # with open("ArchivosEnvio/100MB.txt", "r") as f:
    #     while True:
    #         data = f.read(1024)
    #         data = data.encode('utf-8')

    #         if not data:
    #             server.sendto(data, addr)
    #             break

    #         server.sendto(data, addr)
