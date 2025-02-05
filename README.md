Here is a well-structured README.md file for your Python encryption and decryption tool, Piero EnDe-Coder. This document includes details on how the program works, how to use it, and technical specifications.


---

Piero EnDe-Coder

A powerful encryption and decryption tool that combines the Vigenère cipher, XOR encryption, and Base64 encoding to secure messages. This tool allows users to encode and decode messages using a secret key, ensuring an extra layer of security.

Features

✔ Uses Vigenère cipher for initial encryption
✔ Applies XOR encryption with a randomly generated key
✔ Encodes results in Base64 for safe storage and transmission
✔ Supports decryption with the correct key
✔ Interactive menu-based CLI


---

Table of Contents

How It Works

Installation

Usage

Encryption & Decryption Process

Example Usage

Technical Details

License



---

How It Works

Piero EnDe-Coder follows a three-layered encryption process:

1. Vigenère Cipher: Encrypts the text using a key-based shifting method.


2. XOR Encryption: Applies XOR transformation with a randomly generated key.


3. Base64 Encoding: Encodes the final result into Base64 for secure transfer.



For decryption, the process is reversed:

1. Base64 Decoding → XOR Decryption → Vigenère Decryption.




---

Installation

No external dependencies are required. Simply clone this repository and run the script.

git clone https://github.com/yourusername/Piero-EnDe-Coder.git
cd Piero-EnDe-Coder
python Piero-EnDe-Coder.py


---

Usage

Running the Program

Run the script using:

python Piero-EnDe-Coder.py

You'll see a menu like this:

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

Encrypt a Message

1. Select Option 1.


2. Enter a secret key (used for encryption and decryption).


3. Enter the text to encrypt.


4. Get the encrypted message.



Decrypt a Message

1. Select Option 2.


2. Enter the same secret key used for encryption.


3. Enter the encrypted text.


4. Get the decrypted message.



Exit

Select Option 3 to exit the program.



---

Encryption & Decryption Process


---

Example Usage

Encryption Example:

Enter the secret key: secret123
Enter the text to encrypt: Hello World

Output (Encrypted Text):

UGFr... (Base64 Encoded String)

Decryption Example:

Enter the secret key: secret123
Enter the encrypted text: UGFr...

Output (Decrypted Text):

Hello World


---

Technical Details

Programming Language: Python 3

Encryption Methods:

Vigenère Cipher (Key-based shift cipher)

XOR Cipher (Bitwise transformation)

Base64 Encoding (Safe text encoding)



Functions Overview:


---

License

This project is open-source and free to use.
Licensed under the MIT License.


---

Now you’re ready to submit your project to GitHub! Let me know if you need modifications.

