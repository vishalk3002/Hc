def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'encrypt':
        result = caesar_encrypt(message, shift)
    else:
        result = caesar_decrypt(message, shift)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
