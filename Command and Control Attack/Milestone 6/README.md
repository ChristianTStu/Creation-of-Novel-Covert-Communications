# README: Encrypted Communication and Traffic Detection

## Introduction
This project consists of three Python scripts designed to demonstrate encrypted communication between a client and server, and the detection of encrypted traffic using network packet analysis. The scripts are:
1. `EncryptedChannelServerV2.py` - The server script that listens for incoming encrypted messages, decrypts, and displays them.
2. `EncryptedChannelClientV2.py` - The client script that sends an encrypted message to the server.
3. `DetectEncryptedTrafficV2.py` - A script that analyzes network traffic to detect potentially encrypted data.

## Requirements
- Python 3.x
- Libraries: `cryptography`, `socket`, `scapy`, `pandas`, `scipy`

## Installation Instructions
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using pip:
   ```bash
   pip install cryptography scapy pandas scipy
   ```

## Build Instructions
No specific build process is required as the project consists of Python scripts.

## Run Instructions
### Running the Encrypted Communication Server and Client
1. **Start the Server:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `EncryptedChannelServerV2.py`.
   - Run the script:
     ```bash
     python EncryptedChannelServerV2.py
     ```
   - The server will start and wait for incoming connections.

2. **Run the Client:**
   - Open another terminal or command prompt.
   - Navigate to the directory containing `EncryptedChannelClientV2.py`.
   - Run the script:
     ```bash
     python EncryptedChannelClientV2.py
     ```
   - The client will connect to the server, send an encrypted message, and the server will display the decrypted message.

### Running the Traffic Detection Script
1. **Capture Network Traffic:**
   - Use a tool like Wireshark to capture network traffic while the server and client are communicating. Save the capture file (e.g., `EncryptedChannel.pcapng`).

2. **Analyze the Traffic:**
   - Ensure `DetectEncryptedTrafficV2.py` is in the same directory as your capture file, or modify the script to point to the correct file path.
   - Run the script:
     ```bash
     python DetectEncryptedTrafficV2.py
     ```
   - The script will analyze the captured traffic and report any potentially encrypted data packets.

## Notes
- The encryption key is hardcoded in the scripts for demonstration purposes. In a real-world application, use a securely generated and stored key.
- The server and client scripts are configured to run on `localhost` (127.0.0.1) for testing. Modify the `host` variable for different network setups.
- The traffic detection script is configured for a specific file path. Adjust the file path in the `sniff` function call to match your environment.

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

