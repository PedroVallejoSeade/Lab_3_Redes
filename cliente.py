import socket

IP = socket.gethostbyname(socket.gethostname())
PUERTO = 8888
DIRECCION = (IP, PUERTO)
TAMANIO = 1024
FORMATO = "utf-8"


def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(DIRECCION)

    data = cliente.recv(TAMANIO).decode('utf-8')
    item = data.split("_")
    NOM_ARCHIVO = item[0]
    TAM_ARCHIVO = int(item[1])
    ID = item[2]

    print("[+] Nombre y tamanio del archivo recivido del servidor")
    cliente.send("Nombre y tamanio del archivo recivido".encode(FORMATO))

    with open(f"recv_{NOM_ARCHIVO}_{ID}", "w") as f:
        while True:
            data = cliente.recv(TAMANIO).decode(FORMATO)

            if not data:
                break

            f.write(data)
            cliente.send("Archivo recivido".encode(FORMATO))

    cliente.close()


if __name__ == "__main__":
    main()
