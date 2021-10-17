import socket

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4455
    addr = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data = '[-] Inicializacion UDP con cliente exitosa'
    data = data.encode('utf8')
    client.sendto(data, addr)

    data, addr = client.recvfrom(1024)
    data = data.decode('utf8')
    print(data)

    with open(f"ArchivosRecibidos/Prueba2.txt", "w") as f:
        while True:
            data, addr = client.recvfrom(1024)

            if not data:
                break

            data = data.decode('utf8')
            f.write(data)

    client.close()
