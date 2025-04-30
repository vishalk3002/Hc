#Note: Install pillow module -> pip install pillow 
from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixels = image.load()

        for i in range(image.size[0]):  # Width
            for j in range(image.size[1]):  # Height
                r, g, b = pixels[i, j]
                # Apply XOR with the key to each color channel
                pixels[i, j] = (
                    r ^ key,
                    g ^ key,
                    b ^ key
                )

        image.save(output_path)
        print(f"Image saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        key = int(input("Enter an encryption key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter an integer between 0 and 255.")
        return

    encrypt_decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
