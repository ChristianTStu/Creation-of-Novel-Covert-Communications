# Data Hiding and Covert Communications with Python
## Description
This Python project combines steganography and a basic encryption methods to encode and decode messages within images.

## Table of Contents

    Installation
    Usage
    Cloning the Repo
    License

## Installation

Please ensure that you have the necessary libraries installed (like stegano) and that the file paths are accurate for your system. This project can be useful for secure communication or for learning about steganography and basic encryption techniques.

## Usage

File 1: (steganography.py):

This file contains functions related to steganography:

    encode_message(input_image_path, secret_message, output_image_path): This function encodes a secret_message within an input_image_path and saves the result in output_image_path.
    
    decode_message(encoded_image_path): This function extracts and returns the hidden message from an encoded image.
    
    add_noise(encoded_message): This function adds a pattern of noise bits to the encoded message.
    
    remove_noise(noisy_message): This function removes the previously added noise pattern from a noisy message.
    
In summary, steganography.py is responsible for:

    Encoding a secret message within an input image and saving the result in an output image.
    Extracting and returning the hidden message from an encoded image.
    Adding a pattern of noise bits to the encoded message to increase security.
    Removing the previously added noise pattern from a noisy message during the decoding process.

File 2: (cryptography.py):

This file involves a basic encryption technique:

    original_message: This variable contains the initial message you want to encrypt. In this case, it's set to "secret".

    crypto_char_bank: This is a list of characters that form the basis for the encryption. It appears to be the alphabet from 'a' to 'z'.

    original_message_index: This list will be used to store the index positions of characters from original_message in the crypto_char_bank.

    cipher_number_sequence: This is a list of numbers that will be used in the encryption process.

    cipher_message_index: This list will store the calculated indices after applying the cipher.

    cipher_message_list: This list will hold the actual characters from crypto_char_bank after applying the cipher.


In summary, cryptography.py is responsible for:

    Defining an original message, a character bank, and a cipher sequence for encryption.
    Converting characters from the original message to their respective indices in the character bank.
    Applying a fixed sequence of numbers to the indices for encryption.
    Converting the modified indices back to characters to form the final encrypted message.

File 3: (main.py):

This file orchestrates the process of encoding a message within an image.
    
    # Imports:
    
    from steganography import ...: This line imports the functions encode_message, decode_message, add_noise, and remove_noise from the file steganography.py. These functions are used for encoding and decoding messages within images, as well as adding and removing noise.

    from cryptography import cipher_message: This line imports the variable cipher_message from the file cryptography.py. This variable contains the result of the encryption process.
    
    # Encoding:
    
    input_image: This variable contains the path to the original image (test_original.png) where the secret message will be hidden.

    secret_message: This variable contains the result of the encryption process, which will be encoded into the image. It comes from the cipher_message variable in cryptography.py.

    output_image: This variable contains the path where the modified image will be saved after encoding.

    encode_message(input_image, secret_message, output_image): This function call uses the imported encode_message function from steganography.py. It takes the input image path, secret message, and output image path as arguments to perform the encoding process.
    
    # Decoding:
    
    encoded_image: This variable contains the path to the modified image (test_modified.png) from which the hidden message will be extracted.

    encoded_message: This variable will store the extracted message.

    decode_message(encoded_image): This function call uses the imported decode_message function from steganography.py. It takes the path of the encoded image as an argument to extract the hidden message.
    
    # Adding and Removing Noise:
    
    noisy_message: This variable stores the message after adding a pattern of noise bits. It is obtained by calling the add_noise function from steganography.py.

    cleaned_message: This variable stores the message after removing the previously added noise pattern. It is obtained by calling the remove_noise function from steganography.py.

    decoded_message: This variable contains the final cleaned message, which is obtained by joining the characters in cleaned_message.
    
In summary, main.py is responsible for:

    Importing necessary functions and variables from steganography.py and cryptography.py.
    Encoding the secret message into an image.
    Decoding the message from the modified image.
    Adding noise to the decoded message and removing it during decoding.
    Printing the final decoded message to the console.
    

File 4: (decipher.py):

This file is used for decoding a message:

    # Imports:
    
    from steganography import ...: This line imports the decode_message function from steganography.py. This function is used to extract the hidden message from an image.
    
    #Image Containing Hidden Text:
    
    encoded_image: This variable contains the path to the modified image (test_modified.png) from which the hidden message will be extracted.

    encoded_message: This variable will store the extracted message.

    decode_message(encoded_image): This line calls the decode_message function from steganography.py. It takes the path of the encoded image as an argument to extract the hidden message.
    
    # Deciphering
        
    crypto_char_bank: This is the list of characters that serve as the basis for decryption, similar to what we saw in cryptography.py.

    encoded_message_index: This list will store the index positions of characters from the extracted message in crypto_char_bank.

    cipher_number_sequence: This is the list of numbers that were used in the encryption process.

    decipher_message_index: This list will store the calculated indices after applying the reverse of the cipher.

    decipher_message_list: This list will hold the actual characters from crypto_char_bank after applying the decryption.
    
    index_identification(encoded_message): This function takes encoded_message as input. It iterates through each character in the message and checks if it exists in crypto_char_bank. If it does, it appends the index of that character in crypto_char_bank to encoded_message_index.
    
    cipher_calculation(encoded_message_index): This function takes encoded_message_index as input. It uses a zip loop to pair each element in encoded_message_index with a corresponding element from cipher_number_sequence. It then subtracts them and appends the result to decipher_message_index.
    
    cipher_message_complete(decipher_message_index): This function takes decipher_message_index as input. It iterates through each number in decipher_message_index, retrieves the corresponding character from crypto_char_bank, and appends it to decipher_message_list.
    
    deciphered_message: This variable contains the final message after decryption, obtained by joining the characters in decipher_message_list.

    print("Decoded Message:", deciphered_message): This line prints the decoded message to the console.
    
In summary, decipher.py is responsible for:

    Importing the decode_message function from steganography.py.
    Extracting the encoded message from a modified image.
    Identifying the indices of characters in the extracted message within the character bank.
    Applying the reverse of the cipher to calculate the indices for decryption.
    Converting the modified indices back to characters to form the final decrypted message.
    Printing the final decoded message to the console.

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
