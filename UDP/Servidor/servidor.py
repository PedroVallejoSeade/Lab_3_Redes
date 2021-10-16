import socket

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4455

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((host, port))

    # while True:
    #     data, addr = server.recvfrom(1024)
    #     data = data.decode("utf-8")

    #     if data == "!EXIT":
    #         print("Client disconnected")
    #         break

    #     print(f"Client: {data}")

    #     data = data.upper()
    #     data = data.encode("utf-8")
    #     server.sendto(data, addr)

    data, addr = server.recvfrom(1024)
    data = data.decode("utf-8")
    print(data)

    data = '[-] Conexion con el servidor exitosa'
    data = data.encode("utf-8")
    server.sendto(data, addr)

    with open("ArchivosEnvio/100MB.txt", "r") as f:
        while True:
            data = f.read(1024)
            data = data.encode('utf-8')
            print('ACAAA')

            if not data:
                server.sendto(data, addr)
                break

            server.sendto(data, addr)

    server.close()
