import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encodeDecode(text, shift, encodeOrDecode):
    if shift > 26:
        shift = shift % 26
    finalLetters = alphabet[0:shift]
    alphabetOfCode = alphabet[shift:] + finalLetters
    if encodeOrDecode == 'encode':
        cipherText = ''
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                cipherText += alphabetOfCode[position]
            else:
                cipherText += letter
        print(f"The encoded text is {cipherText}")
    else:
        normalText = ''
        for letter in text:
            if letter in alphabet:
                position = alphabetOfCode.index(letter)
                normalText += alphabet[position]
            else:
                normalText += letter
        print(f'The decoded text is {normalText}')


print(art.logo)
while True:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == 'decode' or direction == 'encode':
            break
        else:
            print('Type a valid entry!')
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encodeDecode(text, shift, direction)
    while True:
        decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        if decision == 'no' or decision == 'yes':
            break
        else:
            print('Type a valid entry!')
    if decision == 'no':
        print('Goodbye friend')
        break

