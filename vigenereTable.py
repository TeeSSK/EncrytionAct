# def main():
#   print("Start create table")
#   real_all_letter = 'abcdefghijklmnopqrstuvwxyz'
#   all_letter = 'bcdefghijklmnopqrstuvwxyza'
#   vig_table = dict()
#   for i in range(len(all_letter)):
#     vig_table[real_all_letter[i]] = all_letter[i:] + all_letter[:i]
#   print(vig_table)

# if __name__ == '__main__':
#   main()

def generate_vigenere_table():
    # Create a 2D matrix (list of lists) for the Vigenère table
    table = []
    for i in range(26):
        row = []
        for j in range(26):
            # Calculate the character for each cell in the table
            char = chr(((i + j) % 26) + ord('A'))
            row.append(char)
        table.append(row)
    return table

def vigenere_encrypt(plaintext, key, table):
    plaintext = plaintext.upper()  # Convert plaintext to uppercase
    key = key.upper()  # Convert the key to uppercase

    ciphertext = ""
    key_length = len(key)
    table_size = len(table)

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Calculate the row and column indices in the Vigenère table
            row = ord(key[i % key_length]) - ord('A')
            col = ord(plaintext[i]) - ord('A')
            ciphertext += table[row][col]
        else:
            ciphertext += plaintext[i]

    return ciphertext

def vigenere_decrypt(ciphertext, key, table):
    ciphertext = ciphertext.upper()  # Convert ciphertext to uppercase
    key = key.upper()  # Convert the key to uppercase

    plaintext = ""
    key_length = len(key)
    table_size = len(table)

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Calculate the row index in the Vigenère table (corresponding to the key)
            row = ord(key[i % key_length]) - ord('A')
            # Find the column index in the Vigenère table to retrieve the original plaintext character
            col = table[row].index(ciphertext[i])
            plaintext += chr(col + ord('A'))
        else:
            plaintext += ciphertext[i]

    return plaintext

# Generate the Vigenère table
vigenere_table = generate_vigenere_table()

# Example usage:
plaintext = "HELLOWORLD"
key = "CAT"
encrypted_text = vigenere_encrypt(plaintext, key, vigenere_table)
print("Encrypted:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key, vigenere_table)
print("Decrypted:", decrypted_text)
