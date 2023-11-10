import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

host = "127.0.0.1"
port = 1337

key = b"Sixteen byte key"

def encrypt(data, key, iv):
    # Pad data as needed
    data += " " * (16 - len(data) % 16)
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(bytes(data, "utf-8")) + encryptor.finalize()

message = "Hello"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    iv = os.urandom(16)
    s.send(iv)
    s.send(bytes([len(message)]))
    encrypted = encrypt(message, key, iv)
    print("Sending %s" % encrypted.hex())
    s.sendall(encrypted)
