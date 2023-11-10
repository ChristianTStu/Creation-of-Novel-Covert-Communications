import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

host = "127.0.0.1"
port = 1337

key = b"Sixteen byte key"

def decrypt(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        iv = conn.recv(16)
        length = conn.recv(1)  # Assumes short messages
        data = conn.recv(1024)
        while True:
            d = conn.recv(1024)
            if not d:
                break
            data += d
        decrypted_message = decrypt(data, key, iv).decode("utf-8")
        print("Received: %s" % decrypted_message[:ord(length)])
