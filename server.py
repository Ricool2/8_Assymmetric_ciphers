#
#
import socket
import pickle
import random

def encrypt(m, k):
    return ''.join([chr((ord(x) + k) % 65536) for x in m])

def decrypt(m, k):
    return ''.join([chr((ord(x) - k) % 65536) for x in m])

HOST = 'localhost'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

b = random.randint(1, 1000)
msg = conn.recv(1024)
(p, g, A) = pickle.loads(msg)

while True:
    msg = conn.recv(1024)
    if not msg:
        break
    
    msg = pickle.loads(msg)
    b = random.randint(1, 1000)
    B = g ** b % p
    k = A ** b % p
    print(k)
    conn.send(pickle.dumps((B, encrypt(msg, k))))

conn.close()
