# 🔒 Piero EnDe-Coder  

### **Ultimate Encryption & Decryption Tool**  

Piero EnDe-Coder is a powerful text encryption tool that enhances security through a multi-layered approach, combining:  
✅ **Vigenère Cipher** for letter-shifting encryption  
✅ **XOR Encryption** for additional obfuscation  
✅ **Random Shuffling** to prevent pattern detection  
✅ **Random Padding** to make brute-force attacks nearly impossible  

---

## **🛠 Features**  
| Feature | Description |
|---------|------------|
| **Vigenère Cipher** | Uses a key-based substitution cipher to shift letters securely. |
| **XOR Encryption** | Adds a secondary layer of scrambling using a randomly generated XOR key. |
| **Random Shuffling** | The final encoded message is shuffled to make it unpredictable. |
| **Random Padding** | Adds meaningless random text before and after the message to obfuscate patterns. |

---

## **📖 How It Works**  

### 🔹 **Encoding Process**  
1. User inputs a **secret key** and the **text to encrypt**.  
2. Text is first **encrypted using the Vigenère cipher**.  
3. Then, an additional **XOR encryption layer** is applied.  
4. The message is **padded with random characters** and **shuffled**.  
5. Finally, the XOR key is **appended to the encoded message** for decryption.  

### 🔹 **Decoding Process**  
1. The XOR key is **extracted from the encoded text**.  
2. The message is **unshuffled** and **decrypted using XOR**.  
3. The **Vigenère decryption** restores the original text.  
4. The **random padding** is removed, revealing the original message.  

---

## **📌 Usage Guide**  

### **🔹 Encoding a Message**
1. Run the program.
2. Select **"1"** for encoding.
3. Enter a **secure key** (e.g., `Secret123`).
4. Input the **message to encrypt**.
5. The program will return a **highly secure encoded text**.

### **🔹 Decoding a Message**
1. Run the program.
2. Select **"2"** for decoding.
3. Enter the **same key** used for encoding.
4. Input the **encoded text**.
5. The program will return the **original decrypted message**.

---

## **🖥 Example Usage**
```bash
Choose an option (1: Encode, 2: Decode): 1
Enter the key: Secret123
Enter the text: Hello, world!
Encoded Text: Xy3F#*vN9aB7r$%L0!...
