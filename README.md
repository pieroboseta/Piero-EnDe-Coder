# Piero EnDe-Coder

A powerful encryption and decryption tool that combines the **Vigenère cipher**, **XOR encryption**, and **Base64 encoding** to secure messages. This tool allows users to encode and decode messages using a secret key, ensuring an extra layer of security.

## Features

✔ Uses **Vigenère cipher** for initial encryption  
✔ Applies **XOR encryption** with a randomly generated key  
✔ Encodes results in **Base64** for safe storage and transmission  
✔ Supports **decryption** with the correct key  
✔ Interactive **menu-based** CLI  

---

## Table of Contents

- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Encryption & Decryption Process](#encryption--decryption-process)
- [Example Usage](#example-usage)
- [Technical Details](#technical-details)
- [License](#license)

---

## How It Works

Piero EnDe-Coder follows a **three-layered encryption process**:

1. **Vigenère Cipher**: Encrypts the text using a key-based shifting method.
2. **XOR Encryption**: Applies XOR transformation with a randomly generated key.
3. **Base64 Encoding**: Encodes the final result into Base64 for secure transfer.

For decryption, the process is reversed:

1. **Base64 Decoding** → **XOR Decryption** → **Vigenère Decryption**.

---

## Installation

No external dependencies are required. Simply clone this repository and run the script.

```bash
git clone https://github.com/yourusername/Piero-EnDe-Coder.git
cd Piero-EnDe-Coder
python Piero-EnDe-Coder.py