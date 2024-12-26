def create_cipher_map(key):
    cipher_map = {}
    length = len(key)
    for i in range(0, length, 2):
        char1 = key[i]
        char2 = key[i + 1]
        cipher_map[char1] = char2
        cipher_map[char2] = char1
        cipher_map[char1.upper()] = char2.upper()
        cipher_map[char2.upper()] = char1.upper()
    return cipher_map

def encode(message, key):
    cipher_map = create_cipher_map(key)
    return "".join(cipher_map.get(char, char) for char in message)

def decode(encrypted_message, key):
    return encode(encrypted_message, key)

print(encode("ABCD", "gaderypoluki"))
print(encode("Ala has a cat", "gaderypoluki"))

print(decode("Dkucr pu yhr ykbir", "politykarenu"))
print(decode("Hmdr nge brres", "regulaminowy"))