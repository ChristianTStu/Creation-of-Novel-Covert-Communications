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
