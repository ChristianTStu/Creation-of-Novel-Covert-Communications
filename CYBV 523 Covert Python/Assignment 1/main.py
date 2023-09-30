from steganography import encode_message, decode_message, add_noise, remove_noise
from cryptography import cipher_message

# Encoding
input_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_original.png"
secret_message = cipher_message
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