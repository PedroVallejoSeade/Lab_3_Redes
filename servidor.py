import socket
import threading
import os

IP = socket.gethostbyname(socket.gethostname())
PUERTO = 8888
DIRECCION = (IP, PUERTO)
TAMANIO = 1024
FORMATO = "utf-8"


def manejarCliente(conn, addr, NOM_ARCHIVO, TAM_ARCHIVO):
    print("[+] Nueva conexion {addr} conectado")

    data = f"{NOM_ARCHIVO}_{TAM_ARCHIVO}"
    conn.send(data.encode(FORMATO))
    mensaje = conn.recv(TAMANIO).decode(FORMATO)
    print("[-] El cliente responde: " + mensaje)

    with open(NOM_ARCHIVO, "r") as f:
        while True:
            data = f.read(TAMANIO)

            if not data:
                break

            conn.send(data.encode(FORMATO))
            mensaje = conn.recv(TAMANIO).decode(FORMATO)
    conn.close()


def main():
    numValidoConexiones = False
    while(not numValidoConexiones):
        numConexiones = input("Numero de conexiones (1-25):")
        if(int(numConexiones) >= 1 and int(numConexiones) <= 25):
            numValidoConexiones = True
        else:
            print(f"{numConexiones} no es un numero valido de conexiones")

    archivoValido = False
    while(not archivoValido):
        archivo = input("Escoja entre el archivo 1(100MB) o 2(250MB):")
        if(int(archivo) == 2):
            NOM_ARCHIVO = "250MB.txt"
            TAM_ARCHIVO = os.path.getsize(NOM_ARCHIVO)
            archivoValido = True
        elif(int(archivo) == 1):
            NOM_ARCHIVO = "100MB.txt"
            TAM_ARCHIVO = os.path.getsize(NOM_ARCHIVO)
            archivoValido = True
        else:
            print("El archivo escogido no es valido")

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(DIRECCION)
    servidor.listen()
    print("[+] Servidor escuchando ....")

    while True:
        conn, addr = servidor.accept()
        print(f"[+] Cliente conectado desde {addr[0]}:{addr[1]}")
        print(f"{NOM_ARCHIVO}_{TAM_ARCHIVO}")
        thread = threading.Thread(target=manejarCliente, args=(
            conn, addr, NOM_ARCHIVO, TAM_ARCHIVO))
        thread.start()
        print(f"[+] Conexiones activas: {threading.active_count()-1}")

    servidor.close()


if __name__ == "__main__":
    main()
