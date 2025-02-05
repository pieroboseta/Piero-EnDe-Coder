#include <iostream>
#include <string>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>

std::string generateRandomString(int length) {
    std::string characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    std::string result;
    for (int i = 0; i < length; ++i) {
        result += characters[rand() % characters.size()];
    }
    return result;
}

std::string xorEncrypt(const std::string &text, char key) {
    std::string encryptedText = text;
    for (char &c : encryptedText) {
        c ^= key;
    }
    return encryptedText;
}

std::string vigenereEncode(const std::string &text, const std::string &key) {
    std::string encodedText;
    int keyLength = key.length();
    int keyIndex = 0;
    char xorKey = rand() % 256;
    
    for (char c : text) {
        if (std::isalpha(c)) {
            char base = std::isupper(c) ? 'A' : 'a';
            char keyChar = std::toupper(key[keyIndex % keyLength]) - 'A';
            encodedText += (c - base + keyChar) % 26 + base;
            keyIndex++;
        } else {
            encodedText += c;
        }
    }
    
    encodedText = xorEncrypt(encodedText, xorKey);
    
    std::string randomPrefix = generateRandomString(150);
    std::string randomSuffix = generateRandomString(100);
    
    encodedText = randomPrefix + encodedText + randomSuffix;
    std::random_shuffle(encodedText.begin(), encodedText.end());
    
    return encodedText + xorKey;
}

std::string vigenereDecode(std::string text, const std::string &key) {
    char xorKey = text.back();
    text.pop_back();
    
    std::random_shuffle(text.begin(), text.end());
    
    std::string extractedText = text.substr(150, text.length() - 250);
    extractedText = xorEncrypt(extractedText, xorKey);
    
    std::string decodedText;
    int keyLength = key.length();
    int keyIndex = 0;
    
    for (char c : extractedText) {
        if (std::isalpha(c)) {
            char base = std::isupper(c) ? 'A' : 'a';
            char keyChar = std::toupper(key[keyIndex % keyLength]) - 'A';
            decodedText += (c - base - keyChar + 26) % 26 + base;
            keyIndex++;
        } else {
            decodedText += c;
        }
    }
    return decodedText;
}

int main() {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));
    std::string choice, key, text;
    
    std::cout << "Choose an option (1: Encode, 2: Decode): ";
    std::cin >> choice;
    
    if (choice == "1") {
        std::cout << "Enter the key: ";
        std::cin >> key;
        std::cin.ignore();
        std::cout << "Enter the text: ";
        std::getline(std::cin, text);
        std::string encodedText = vigenereEncode(text, key);
        std::cout << "Encoded Text: " << encodedText << std::endl;
    } else if (choice == "2") {
        std::cout << "Enter the key: ";
        std::cin >> key;
        std::cin.ignore();
        std::cout << "Enter the encoded text: ";
        std::getline(std::cin, text);
        if (text.length() < 250) {
            std::cerr << "Encoded text is too short. Exiting." << std::endl;
            return 1;
        }
        std::string decodedText = vigenereDecode(text, key);
        std::cout << "Decoded Text: " << decodedText << std::endl;
    } else {
        std::cerr << "Invalid choice." << std::endl;
    }
    return 0;
}
