from PIL import Image
import os

# Simple key for value modification
KEY = 50

def encrypt_image(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert("RGB")
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply simple math operation to pixel
            r = (r + KEY) % 256
            g = (g + KEY) % 256
            b = (b + KEY) % 256

            # Swap pixel position (horizontal mirror)
            swap_x = width - 1 - x
            pixels[swap_x, y] = (r, g, b)

    image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert("RGB")
    pixels = image.load()

    width, height = image.size

    # Create a blank image for output
    decrypted = Image.new("RGB", (width, height))
    decrypted_pixels = decrypted.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[width - 1 - x, y]

            # Reverse the math operation
            r = (r - KEY) % 256
            g = (g - KEY) % 256
            b = (b - KEY) % 256

            decrypted_pixels[x, y] = (r, g, b)

    decrypted.save(output_path)
    print(f"Decrypted image saved to {output_path}")

# === Example Usage ===
if __name__ == "__main__":
    input_image = "your_image.jpg"           # Replace with your image path
    encrypted_image = "encrypted_image.jpg"
    decrypted_image = "decrypted_image.jpg"

    encrypt_image(input_image, encrypted_image)
    decrypt_image(encrypted_image, decrypted_image)
