from stegano import lsb


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


# Encoding
input_image = "C:/Users/chris/Desktop/images/image.png"
secret_message = "Secret"
output_image = "C:/Users/chris/Desktop/images/new_image.png"
encode_message(input_image, secret_message, output_image)

# Decoding
encoded_image = "C:/Users/chris/Desktop/images/new_image.png"
encoded_message = decode_message(encoded_image)

# Add noise
noisy_message = add_noise(encoded_message)

# Remove noise during decoding
cleaned_message = remove_noise(noisy_message)
decoded_message = ''.join(cleaned_message)

print("Decoded Message:", decoded_message)