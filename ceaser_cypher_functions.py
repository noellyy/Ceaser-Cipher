import string

entire_alphabet = list(string.ascii_lowercase)

alphabet_length = len(entire_alphabet)

answer_list = ['e', 'd']


def ceaser_cipher():
    user_input = input('Type in the message you wish to encrypt or decrypt: ')
    key = int(input('What is the key: '))
    mode = input('Are we [e]ncrypting or [d]ecrypting (E/D): ').lower()
    while mode not in answer_list:
        print('Invalid input')
        mode = input('Encrypting or decrypting (E/D): ').lower()

    message = user_input.lower()  # Input Validation

    encrypt_decrypt(message, key, mode)


def encrypt_decrypt(text, key, mode):
    result = ''
    for character in text:
        if character in entire_alphabet:
            index = entire_alphabet.index(character)
            if mode == 'e':
                shift = (index + key) % alphabet_length
            else:
                shift = (index - key) % alphabet_length
            result += entire_alphabet[shift]
        else:
            result += character  # Handles spaces and other characters

    print(f'The Original Text: {text}')
    print(f'Processed Text: {result}')
