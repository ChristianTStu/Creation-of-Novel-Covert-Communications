import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Server's IP address and port number for the socket connection
host = "127.0.0.1"
port = 1337

# Encryption key for AES. In a real application, this should be securely generated and stored.
key = b"Sixteen byte key"

def decrypt(data, key, iv):
    # Initialize the AES cipher in CBC mode for decryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Decrypt the data and finalize the decryption process
    return decryptor.update(data) + decryptor.finalize()

# Create a socket object using IPv4 and TCP protocols
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the specified host and port
    s.bind((host, port))
    # Listen for incoming connections
    s.listen()
    # Accept a connection; conn is a new socket object for sending/receiving data
    conn, addr = s.accept()
    with conn:
        # Receive the initialization vector (IV) from the client
        iv = conn.recv(16)
        # Receive the length of the original message (assuming it's a short message)
        length = conn.recv(1)
        # Receive the encrypted data in chunks
        data = conn.recv(1024)
        while True:
            d = conn.recv(1024)
            if not d:
                break
            data += d
        # Decrypt the received data and decode it from bytes to string
        decrypted_message = decrypt(data, key, iv).decode("utf-8")
        # Print the decrypted message, trimmed to the original message length
        print("Received: %s" % decrypted_message[:ord(length)])
