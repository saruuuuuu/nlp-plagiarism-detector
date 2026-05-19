def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    text = "Hello, World!"
    shift = 4
    print(f"Original Text: {text}")
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted Text with shift {shift}: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
