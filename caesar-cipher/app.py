alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message\n").lower()
shift = int(input("Type a shift number\n").lower())


def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for letter in original_text:
        current_position = alphabet.index(letter)
        shifted_position = current_position + shift_amount
        final_position = shifted_position % len(alphabet)

        encrypted_text += alphabet[final_position]

    print(f"Here is the encoded result {encrypted_text}")


encrypt(text, shift)
