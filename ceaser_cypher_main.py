from ceaser_cypher_functions import *

print('===CEASER CIPHER===')

yes_or_no = ['y', 'n']

answer = input('Would you like to use the Ceaser Cipher? (Y/N): ').lower()
while answer != 'n':
    while answer not in yes_or_no:
        answer = input('Invalid, yes or no? (Y/N): ').lower()
    if answer != 'n':
        ceaser_cipher()
        answer = input('Wanna do it again? (Y/N): ').lower()

print('Thank you!')
