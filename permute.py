def substitution_cipher(text, cipher_dict, mode='encrypt'):
    result = ""
    
    # If decryption is requested, reverse the cipher dictionary
    if mode == 'decrypt':
        cipher_dict = {v: k for k, v in cipher_dict.items()}
    
    for char in text:
        if char.isalpha():
            # Preserve case by checking upper and lower separately
            if char.isupper():
                result += cipher_dict.get(char, char)
            else:
                result += cipher_dict.get(char.upper(), char.upper()).lower()
        else:
            result += char  # Non-alphabet characters remain unchanged

    return result

# Example usage
# Permutated alphabet cipher dictionary
cipher_dict = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 
    'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 
    'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z', 'U': 'X', 
    'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'
}

# Encrypt
encrypted_text = substitution_cipher("HELLO", cipher_dict, mode='encrypt')
print(f"Encrypted Text: {encrypted_text}")

# Decrypt
decrypted_text = substitution_cipher(encrypted_text, cipher_dict, mode='decrypt')
print(f"Decrypted Text: {decrypted_text}")
