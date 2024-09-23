def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97
            # Shift character and handle wrap-around using modulo 26
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            result += char  # Non-alphabet characters are added as is
    
    return result

# Encrypt
encrypted_text = caesar_cipher("HELLO", 3)  # Shift by 3
print(f"Encrypted Text: {encrypted_text}")

# Decrypt
decrypted_text = caesar_cipher(encrypted_text, 3, mode='decrypt')
print(f"Decrypted Text: {decrypted_text}")
