from steganography import decode_message

# Pull Cyprtographic Message out of Image
encoded_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_modified.png"
encoded_message = decode_message(encoded_image)


# Decipher Hidden Message
crypto_char_bank = ['a', 'b', 'c', 'd', 'e', 'f', 
                    'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 
                    's', 't', 'u', 'v', 'w', 'x', 
                    'y', 'z']
encoded_message_index = []
cipher_number_sequence =  [0, 1, 1, 2, 3, 5]
decipher_message_index = []
decipher_message_list = []

def index_identification(encoded_message):
    for char in encoded_message:
        if char in crypto_char_bank:
            encoded_message_index.append(crypto_char_bank.index(char))

def cipher_calculation(encoded_message_index):
    global cipher_number_sequence
    for encoded_message_index, cipher_number_sequence in zip(encoded_message_index, cipher_number_sequence):
        decipher_message_index.append(encoded_message_index - cipher_number_sequence)

def cipher_message_complete(cipher_message_index):
    for num in cipher_message_index:
        decipher_message_list.append(crypto_char_bank[num])

index_identification(encoded_message)
cipher_calculation(encoded_message_index)
cipher_message_complete(decipher_message_index)

deciphered_message = ''.join(decipher_message_list)

print("Decoded Message:", deciphered_message)