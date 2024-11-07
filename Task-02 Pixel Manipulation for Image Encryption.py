from PIL import Image
import numpy as np

# Load and validate image
def load_image(path):
    try:
        image = Image.open(path)
        return image
    except FileNotFoundError:
        print("Error: Image path not found.")
        return None
    except IOError:
        print("Error: File is not a valid image.")
        return None

# Get encryption key from user
def get_key():
    try:
        key = int(input("Enter an encryption key (integer): "))
        return key
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None

# Encrypt using a pixel shift
def encrypt_image(image, key):
    encrypted_image = image.copy()
    pixels = encrypted_image.load()
    for i in range(encrypted_image.width):
        for j in range(encrypted_image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return encrypted_image

# Decrypt by reversing the shift
def decrypt_image(image, key):
    decrypted_image = image.copy()
    pixels = decrypted_image.load()
    for i in range(decrypted_image.width):
        for j in range(decrypted_image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    return decrypted_image

# Main function
def main():
    path = input("Enter image path: ")
    image = load_image(path)
    if image is None:
        return

    key = get_key()
    if key is None:
        return

    # Encrypt and save
    encrypted_image = encrypt_image(image, key)
    encrypted_image.show()
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

    # Decrypt and save
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image.show()
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

main()
