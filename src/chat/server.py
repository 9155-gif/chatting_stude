import socket
from threading import Thread

class ChatServer:
    def __init__(self, port) -> None:
        self.host = "0.0.0.0"
        self.port = port




        self.client_sockets = []

        self.s = socket.socket()

        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.s.bind((self.host, self.port))
        self.s.listen()
        print(f'[*] {self.host}:{self.port}주소에서 통신 대기중...')
    def communication_with_client(self, cs):
        while True:
            try:  
                message = cs.recv(1024).decode()
            except Exception as e:
                print(f"[!] 에러발생: {e}")
                break
            else:   
                for client_socket in self.client_sockets:
                    if cs != client_socket:
                        client_socket.send(message.encode())

    def serve(self):  
        while True:
            client_socket, client_address = self.s.accept()
            print(f'[*]연결완료: {client_address}')
            self.client_sockets.append(client_socket)
            t = Thread(target=self.communication_with_client, args=[client_socket], daemon=True)
            t.start()
            
        for cs in client_sockets:
            cs.close()

        s.close



