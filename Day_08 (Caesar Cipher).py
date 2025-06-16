alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']



def caesar(og_text, shift_amt, encode_or_decode):
    output = ""
    if encode_or_decode == "decode":
        shift_amt *= -1

    for letter in og_text:
        if letter not in alphabet:
            output += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amt
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no:\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
