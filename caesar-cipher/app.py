alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == 'decode':
        shift_amount *= -1

    output_text = ''
    for letter in original_text:

        current_position = alphabet.index(letter)
        shifted_position = current_position + shift_amount
        shifted_position %= len(alphabet)

        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result {output_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text = input("Type your message\n").lower()
shift = int(input("Type a shift number\n").lower())

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
