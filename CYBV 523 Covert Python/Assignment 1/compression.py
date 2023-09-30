import imageio.v2 as imageio


def compress_to_size(input_path, output_path, target_size_kb):
    image = imageio.imread(input_path)
    imageio.imsave(output_path, image, quality=target_size_kb)


# Example usage
input_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_original.png"
output_image = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_modified.png"
target_size_kb = 266  # Set your target size in kilobytes

# Compress the image to a specific size
compress_to_size(input_image, output_image, target_size_kb)
