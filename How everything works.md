**PIERO ENDE-CODER: DETAILED ANALYSIS**

## Overview
Piero EnDe-Coder is an encryption system that combines **Vigenère Cipher**, **XOR Encryption**, and **Base64 Encoding** to secure text messages. This system uses a multi-layer approach where each method builds upon the previous one to enhance security. Below is a step-by-step breakdown of how each encoding method works, complete with visual examples to make it easy to understand.

## Encryption Process Breakdown

### **1. Vigenère Cipher**
The Vigenère cipher is a method of encrypting text by using a repeating key to shift the characters.

#### **How It Works (Step-by-Step Explanation)**
1. Write down your **plaintext** message.
2. Write your **key** repeatedly underneath the message so that each letter is aligned.
3. Shift each letter in the plaintext forward by the corresponding letter in the key (where A=0, B=1, ..., Z=25).

#### **Formula**
\[ C_i = (P_i + K_i) \mod 26 \]
where \( P_i \) is the plaintext character, \( K_i \) is the key character shift, and \( C_i \) is the encrypted character.

#### **Example Calculation in Table Format**
| Plaintext  | H  | E  | L  | L  | O  |
|-----------|----|----|----|----|----|
| Key       | K  | E  | Y  | K  | E  |
| Shift     | +10| +4 | +24| +10| +4 |
| Ciphertext| R  | I  | J  | V  | S  |

Thus, "HELLO" encrypts to "RIJVS" using the key "KEYKE".

### **2. XOR Encryption**
XOR encryption is a binary operation that flips bits using a key. Each character is XORed with a random single-byte key.

#### **Formula**
\[ C_i = P_i \oplus K \]
where \( \oplus \) is the XOR operation.

#### **Example Calculation in Table Format**
| Plaintext (ASCII) | H    | E    | L    | L    | O    |
|------------------|------|------|------|------|------|
| Binary          | 01001000 | 01000101 | 01001100 | 01001100 | 01001111 |
| XOR Key (26)   | 00011010 | 00011010 | 00011010 | 00011010 | 00011010 |
| Ciphertext     | 01010010 | 01011111 | 01010110 | 01010110 | 01010101 |
| Encrypted Text | R    | _    | V    | V    | U    |

Thus, "HELLO" encrypts to "R_VVU" using an XOR key of 26.

### **3. Base64 Encoding**
Base64 is not encryption but a way to ensure data is printable and safe for transmission.

#### **Formula**
Base64 encoding splits binary data into **6-bit groups**, then maps them to the Base64 character set.

#### **Example Calculation in Table Format**
| Binary Input        | 01010010 | 01011111 | 01010110 | 01010110 | 01010101 |
|--------------------|----------|----------|----------|----------|----------|
| Base64 Characters | U        | l        | 9        | W        | VlU=     |

Thus, "R_VVU" is encoded as "Ul9WVlU=".

## Decryption Process Breakdown
1. **Base64 Decoding** → Extracts XOR key and message.
2. **XOR Decryption** → Reverses XOR operation.
3. **Vigenère Decryption** → Reverses character shifting.

## Security Analysis
| Method        | Strengths                                              | Weaknesses                                           |
|--------------|------------------------------------------------------|-----------------------------------------------------|
| Vigenère     | Harder to brute-force than simple substitution.       | Repeating key patterns can be cracked via frequency analysis. |
| XOR          | Adds randomness and obfuscation.                      | Single-byte key makes brute-force feasible.       |
| Base64       | Ensures readability.                                  | Not a form of encryption; can be reversed easily. |

### **Time to Crack by Brute Force**
| Attack Type        | Estimated Time |
|-------------------|---------------|
| XOR (255 keys)   | Instantly (~1 sec) |
| Vigenère (10-char key) | 10^14 guesses (~centuries) |
| Layered Attack   | Requires both steps above, reducing efficiency. |

### **Probability of Cracking Based on Key Length**
| Key Length (Characters) | Possible Combinations | Estimated Time to Crack |
|------------------------|----------------------|-----------------------|
| 5                      | ~10^7                | Minutes to Hours       |
| 10                     | ~10^14               | Centuries              |
| 15                     | ~10^21               | Millions of Years      |

## Conclusion
Piero EnDe-Coder provides a moderate level of security. While XOR alone is weak, layering it with Vigenère strengthens protection. However, if an attacker identifies key patterns, the encryption can be vulnerable to cryptanalysis.

For improved security, consider:
- Increasing Vigenère key length.
- Using a stronger random key for XOR.
- Applying additional hashing or cryptographic methods.

By explaining each step with clear examples and table-based visuals, even those without coding experience can understand how the encryption process works and its level of security.

