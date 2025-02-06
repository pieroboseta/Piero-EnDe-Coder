# 🔐 Piero EnDe-Coder

A powerful encryption and decryption tool that combines the **Vigenère cipher**, **XOR encryption**, and **Base64 encoding** to secure messages. This tool allows users to encode and decode messages using a secret key, ensuring an extra layer of security.

## ⚙️ Features

✔ Uses **Vigenère cipher** for initial encryption  
✔ Applies **XOR encryption** with a randomly generated key  
✔ Encodes results in **Base64** for safe storage and transmission  
✔ Supports **decryption** with the correct key  
✔ Interactive **menu-based** CLI  

---

## 📚 Table of Contents

- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Encryption & Decryption Process](#encryption--decryption-process)
- [Example Usage](#example-usage)
- [Technical Details](#technical-details)
- [License](#license)

---

## 💡 How It Works

Piero EnDe-Coder follows a **three-layered encryption process**:

1. **Vigenère Cipher**: Encrypts the text using a key-based shifting method.
2. **XOR Encryption**: Applies XOR transformation with a randomly generated key.
3. **Base64 Encoding**: Encodes the final result into Base64 for secure transfer.

For decryption, the process is reversed:

1. **Base64 Decoding** → **XOR Decryption** → **Vigenère Decryption**.

---

## 🛠️ Installation

No external dependencies are required. Simply clone this repository and run the script.

```bash
git clone https://github.com/yourusername/Piero-EnDe-Coder.git
cd Piero-EnDe-Coder
python Piero-EnDe-Coder.py
```

---

## 💖 Support This Project

If you find this project helpful, consider supporting its development! Your donation helps keep the project alive and improve it further.

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/pieroboseta?country.x=AL&locale.x=en_US)

Every contribution is greatly appreciated! Thank you for your support. 🙌

---

## 👨‍💻 Usage

### Running the Program

Run the script using:

```bash
python Piero-EnDe-Coder.py
```

You'll see a menu like this:

```plaintext
*****************************
      PIERO ENDE-CODER       
*****************************
Instructions:
  - This tool encrypts and decrypts messages using the Vigenère Cipher
    combined with XOR encryption.
  - You will need to enter a **secret key** for encryption and decryption.

Choose an option:
  [1] Encrypt a message
  [2] Decrypt a message
  [3] Exit
*****************************
```

### Encrypt a Message

1. Select **Option 1**.
2. Enter a **secret key** (used for encryption and decryption).
3. Enter the text to encrypt.
4. Receive the **encrypted message**.

### Decrypt a Message

1. Select **Option 2**.
2. Enter the **same secret key** used for encryption.
3. Enter the **encrypted text**.
4. Receive the **decrypted message**.

### Exit

- Select **Option 3** to exit the program.

---

## 📌 Encryption & Decryption Process

| Step | Encryption                                   | Decryption                                   |
|------|----------------------------------------------|----------------------------------------------|
| 1    | **Vigenère Cipher** shifts text with key     | **Reverse Vigenère Cipher** restores text    |
| 2    | **XOR Encryption** scrambles data with key   | **XOR Decryption** reverses the transformation |
| 3    | **Base64 Encoding** makes text safe for storage | **Base64 Decoding** restores encrypted text |

---

## 🧩Example Usage

### Encryption Example:

```
Enter the secret key: secret123
Enter the text to encrypt: Hello World
```

**Output (Encrypted Text):**

```
UGFr... (Base64 Encoded String)
```

### Decryption Example:

```
Enter the secret key: secret123
Enter the encrypted text: UGFr...
```

**Output (Decrypted Text):**

```
Hello World
```

---

## 🧐 Technical Details

- **Programming Language**: Python 3  
- **Encryption Methods**:
  - Vigenère Cipher (Key-based shift cipher)
  - XOR Cipher (Bitwise transformation)
  - Base64 Encoding (Safe text encoding)

### 🔎 Functions Overview:

| Function                         | Purpose                                         |
|----------------------------------|-------------------------------------------------|
| `xor_encrypt(text, key)`         | Applies XOR encryption to text                  |
| `vigenere_cipher(text, key, encrypt=True)` | Encrypts/decrypts using the Vigenère cipher |
| `vigenere_encode(text, key)`     | Encrypts using Vigenère, XOR, and Base64        |
| `vigenere_decode(text, key)`     | Decrypts by reversing Base64, XOR, and Vigenère |
| `print_menu()`                   | Displays the main menu                          |
| `main()`                         | Runs the interactive command-line interface     |

---

## 📝 License

This project is **open-source** and free to use.  
Licensed under the [MIT License](LICENSE).

---
