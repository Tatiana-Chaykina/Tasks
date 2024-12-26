def caesar_bruteforce(ciphertext):
    for n in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - offset - n) % 26 + offset)
            else:
                decrypted += char
        print(f"{n}: {decrypted}")


ciphertext = ""
caesar_bruteforce(ciphertext)