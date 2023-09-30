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

index_identification(original_message)
cipher_calculation(original_message_index)
cipher_message_complete(cipher_message_index)

cipher_message = ''.join(cipher_message_list)
