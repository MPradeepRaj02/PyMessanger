import socket

HEADER = 64
PORT = 4312
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "Server IP"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(m,user):
    msg = f'{user} sends => {m}'
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def connection():
    stay = True
    user = input('Your Name : ')
    while stay:
        config = input(f'{user} want to send message ? (y/n)\n>> ')
        if config == 'n':
            stay = False
            send(DISCONNECT_MESSAGE,user)
        else:
            m = input('Enter the message\n>> ')
            send(m,user)
            
connection()
