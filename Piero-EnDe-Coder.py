import random
import base64

def xor_encrypt(text: str, key: int) -> str:
    """Encrypts or decrypts text using a single-character XOR key."""
    return ''.join(chr(ord(c) ^ key) for c in text)

def vigenere_cipher(text: str, key: str, encrypt=True) -> str:
    """Encrypts or decrypts text using the Vigenère cipher."""
    result = []
    key_length = len(key)
    
    for i, c in enumerate(text):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            key_char = ord(key[i % key_length].upper()) - ord('A')
            shift = key_char if encrypt else -key_char
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)  # Keep symbols and spaces unchanged

    return ''.join(result)

def vigenere_encode(text: str, key: str) -> str:
    """Applies Vigenère cipher first, then XOR encryption, then encodes in Base64."""
    xor_key = random.randint(1, 255)  # Generate a random XOR key
    vigenere_text = vigenere_cipher(text, key, encrypt=True)
    encrypted_text = xor_encrypt(vigenere_text, xor_key)

    # Encode to Base64 to avoid non-printable characters messing things up
    encoded_message = base64.urlsafe_b64encode((chr(xor_key) + encrypted_text).encode()).decode()
    
    return encoded_message

def vigenere_decode(text: str, key: str) -> str:
    """Decodes Base64, applies XOR decryption first, then Vigenère decryption."""
    if not text:
        return "Error: Encrypted text is empty."
    
    try:
        # Decode from Base64 first
        decoded_text = base64.urlsafe_b64decode(text).decode()
    except Exception:
        return "Error: Invalid encrypted text format."

    xor_key = ord(decoded_text[0])  # Extract the XOR key
    encrypted_text = decoded_text[1:]  # Remove the first character (XOR key)

    decrypted_text = xor_encrypt(encrypted_text, xor_key)  
    original_text = vigenere_cipher(decrypted_text, key, encrypt=False)  

    return original_text

def print_menu():
    """Displays a simple, user-friendly menu."""
    print("\n*****************************")
    print("      PIERO ENDE-CODER       ")
    print("*****************************")
    print("Instructions:")
    print("  - This tool encrypts and decrypts messages using the Vigenère Cipher")
    print("    combined with XOR encryption.")
    print("  - You will need to enter a **secret key** for encryption and decryption.")
    print("\nChoose an option:")
    print("  [1] Encrypt a message")
    print("  [2] Decrypt a message")
    print("  [3] Exit")
    print("*****************************")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            print("\nEncryption Mode:")
            key = input("Enter the secret key: ").strip()
            text = input("Enter the text to encrypt: ").strip()
            encoded_text = vigenere_encode(text, key)
            
            print("\nEncryption Successful!")
            print("Encrypted Message:")
            print(encoded_text)

        elif choice == "2":
            print("\nDecryption Mode:")
            key = input("Enter the secret key: ").strip()
            text = input("Enter the encrypted text: ").strip()
            decoded_text = vigenere_decode(text, key)
            
            print("\nDecryption Successful!")
            print("Decrypted Message:")
            print(decoded_text)

        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break  # Exit the loop safely

        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")

        input("\nPress Enter to continue...")  # Pause before repeating
