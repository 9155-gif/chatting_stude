import socket
from threading import Thread

class ChatClient:
     def __init__(self, host, port, name="익명") -> None:
          self.host = host
          self.port = port
          self.name = name
          

          self.s = socket.socket()
          print(f'[*] {host}:{port} 로 연결 시도중...')



          self.s.connect((host, port))
          print('[*]연결완료')

     def communication_with_server(self):              
        while True:
                message = self.s.recv(1024).decode()
                print(message)

     def connect(self):
        t = Thread(target=self.communication_with_server, daemon=True)
        t.start()

        while True:
             message = input()
             message = f"{self.name}: {message}"
             self.s.send(message.encode())

        self.s.close()


print(__name__)