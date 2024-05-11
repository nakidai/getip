import socket
import ssl


get_string = "GET / HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n"


def getip(server: str = "ifconfig.me", is_ssl: bool = True) -> str:
    context = ssl.create_default_context()

    data = ""
    with socket.create_connection((server, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=server) as ssock:
            ssock.send(get_string.format(server).encode("UTF-8"))
            while len(d := ssock.recv(4096)) > 0:
                data += d.decode("UTF-8")

    return data[data.rfind("\r\n\r\n") + 4:]
