import string 

# plain_text = "hello world"
# shift = 7
# shift %= 26 

# alphabet = string.ascii_lowercase
# shifted  = alphabet[shift:] + alphabet[:shift]
# table = str.maketrans(alphabet, shifted)

# encrypted = plain_text.translate(table)

# print(encrypted)

def caesar( text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabets = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabets)
    return text.translate(table)


plain_text = "this is a test, Hello World !!"
print(caesar(plain_text, 8, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

