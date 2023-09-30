import random
from stegano import lsb

original_message = "secret"
crypto_char_bank = ['a', 'b', 'c', 'd', 'e', 'f', 
                    'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 
                    's', 't', 'u', 'v', 'w', 'x', 
                    'y', 'z']
original_message_index = []
cipher_number_sequence =  [0, 1, 1, 2, 3, 5]
cipher_message_index = []
cipher_message_list = []

def index_identification(original_message):
    for char in original_message:
        if char in crypto_char_bank:
            original_message_index.append(crypto_char_bank.index(char))

def cipher_calculation(original_message_index):
    global cipher_number_sequence
    for original_message_index, cipher_number_sequence in zip(original_message_index, cipher_number_sequence):
        cipher_message_index.append(original_message_index + cipher_number_sequence)

def cipher_message_complete(cipher_message_index):
    for num in cipher_message_index:
        cipher_message_list.append(crypto_char_bank[num])
        

def encode_message(input_image_path, secret_message, output_image_path):
    secret = lsb.hide(input_image_path, secret_message)
    secret.save(output_image_path)


def decode_message(encoded_image_path):
    return lsb.reveal(encoded_image_path)


def add_noise(encoded_message):
    noise_pattern = [0, 1, 0, 1, 0, 1, 0]  # Define a pattern of noise bits
    noisy_message = [chr(ord(m) ^ n) for m, n in zip(encoded_message, noise_pattern)]
    return noisy_message


def remove_noise(noisy_message):
    noise_pattern = [0, 1, 0, 1, 0, 1, 0]  # Same pattern as used for adding noise
    cleaned_message = [chr(ord(m) ^ n) for m, n in zip(noisy_message, noise_pattern)]
    return cleaned_message


cipher_message = ''.join(cipher_message_list)

# Encoding
input_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_original.png"
secret_message = "Secret"
output_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_modified.png"
encode_message(input_image, secret_message, output_image)

# Decoding
encoded_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_modified.png"
encoded_message = decode_message(encoded_image)

# Add noise
noisy_message = add_noise(encoded_message)

# Remove noise during decoding
cleaned_message = remove_noise(noisy_message)
decoded_message = ''.join(cleaned_message)

print("Decoded Message:", decoded_message)