# Український алфавіт
UA_ALPHABET = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
UA_ALPHABET_UPPER = UA_ALPHABET.upper()
ALPHABET_LEN = len(UA_ALPHABET)

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch in UA_ALPHABET:
            idx = UA_ALPHABET.index(ch)
            new_idx = (idx + shift) % ALPHABET_LEN
            result.append(UA_ALPHABET[new_idx])
        elif ch in UA_ALPHABET_UPPER:
            idx = UA_ALPHABET_UPPER.index(ch)
            new_idx = (idx + shift) % ALPHABET_LEN
            result.append(UA_ALPHABET_UPPER[new_idx])
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift):
    result = []
    for ch in text:
        if ch in UA_ALPHABET:
            idx = UA_ALPHABET.index(ch)
            new_idx = (idx - shift) % ALPHABET_LEN
            result.append(UA_ALPHABET[new_idx])
        elif ch in UA_ALPHABET_UPPER:
            idx = UA_ALPHABET_UPPER.index(ch)
            new_idx = (idx - shift) % ALPHABET_LEN
            result.append(UA_ALPHABET_UPPER[new_idx])
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    text = input("Введіть текст для шифрування: ")
    shift = int(input("Введіть зсув: "))
    encrypted = caesar_encrypt(text, shift)
    print("Зашифровано:", encrypted)
    decrypted = caesar_decrypt(encrypted, shift)
    print("Розшифровано:", decrypted)