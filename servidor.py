import socket
import threading
import os

IP = socket.gethostbyname(socket.gethostname())
PUERTO = 8888
DIRECCION = (IP, PUERTO)
TAMANIO = 1024
FORMATO = "utf-8"
NOM_ARCHIVO = "100MB.txt"
TAM_ARCHIVO = os.path.getsize(NOM_ARCHIVO)


def manejarCliente(conn, addr):
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
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(DIRECCION)
    servidor.listen()
    print("[+] Servidor escuchando ....")

    # conn, addr = servidor.accept()
    # print(f"[+] Cliente conectado desde {addr[0]}:{addr[1]}")

    # data = f"{NOM_ARCHIVO}_{TAM_ARCHIVO}"
    # conn.send(data.encode(FORMATO))
    # mensaje = conn.recv(TAMANIO).decode(FORMATO)
    # print("El cliente responde:" + mensaje)

    # with open(NOM_ARCHIVO, "r") as f:
    #     while True:
    #         data = f.read(TAMANIO)

    #         if not data:
    #             break

    #         conn.send(data.encode(FORMATO))
    #         mensaje = conn.recv(TAMANIO).decode(FORMATO)

    # conn.close()
    # servidor.close()

    while True:
        conn, addr = servidor.accept()
        print(f"[+] Cliente conectado desde {addr[0]}:{addr[1]}")
        thread = threading.Thread(target=manejarCliente, args=(conn, addr))
        thread.start()
        print(f"[+] Conexiones activas: {threading.active_count()-1}")

    servidor.close()


if __name__ == "__main__":
    main()
