# Creation of Novel Covert Communications
## Description
This Python project demonstrates the use of encryption, decryption, and network traffic analysis to facilitate secure and covert communications. It combines socket programming, AES encryption, and entropy analysis to encrypt, transmit, receive, and analyze potentially encrypted data.

## Table of Contents

- Installation
- Usage
- Cloning the Repo
- License

## Installation

Please ensure that you have Python installed along with necessary libraries like `cryptography`, `scapy`, `pandas`, and `socket`. This project can be useful for understanding secure communication, encryption, and network packet analysis.

## Usage

### File 1: Encryption Script (encryption.py)

This file contains the code for encrypting a message and sending it over a network:

- `encrypt(data, key, iv)`: Encrypts the data using AES in CBC mode.
- The script establishes a socket connection and sends the encrypted data to a specified server.

### File 2: Decryption Script (decryption.py)

This file involves receiving and decrypting the message:

- `decrypt(data, key, iv)`: Decrypts the received data using the same key and IV.
- The script listens for incoming encrypted messages and decrypts them upon receipt.

### File 3: Entropy Analysis Script (entropy_analysis.py)

This file is used for analyzing network packets to detect encrypted data:

- `calcEntropy(data)`: Calculates the entropy of the data to identify randomness.
- `processPayloads(p)`: Analyzes packets captured in a .pcap file to detect potential encryption.
- Uses `scapy` to sniff packets and `pandas` for data analysis.

## Clone the repository

## Clone the repository
git clone [https://github.com/ChristianTStu/UoA-Python-Projects.git](https://github.com/ChristianTStu/UoA-Python-Projects.git)

## License

MIT License

Copyright (c) 2023 Christian Stuart

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

