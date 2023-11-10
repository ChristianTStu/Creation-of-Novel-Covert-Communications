import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Server's IP address and port number for the socket connection
host = "127.0.0.1"
port = 1337

# Encryption key for AES. In a real application, this should be securely generated and stored.
key = b"Sixteen byte key"

def encrypt(data, key, iv):
    # Pad the data to ensure it fits the block size for AES (16 bytes)
    data += " " * (16 - len(data) % 16)
    # Create a Cipher object for AES encryption in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Encrypt the data and finalize the encryption process
    return encryptor.update(bytes(data, "utf-8")) + encryptor.finalize()

# The message to be encrypted and sent
message = "Hello"

# Create a socket object using IPv4 and TCP protocols
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server at the specified host and port
    s.connect((host, port))
    # Generate a random Initialization Vector (IV) for encryption
    iv = os.urandom(16)
    # Send the IV to the server
    s.send(iv)
    # Send the length of the original message (useful for trimming padding during decryption)
    s.send(bytes([len(message)]))
    # Encrypt the message
    encrypted = encrypt(message, key, iv)
    # Print the encrypted message in hexadecimal format for verification
    print("Sending %s" % encrypted.hex())
    # Send the encrypted message to the server
    s.sendall(encrypted)