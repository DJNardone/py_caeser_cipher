from art import logo
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart_prog = False

while not restart_prog:
    def caeser(input_text, shift_amt, dir_choice):
        output_text = []
        if dir_choice == "decode":
            shift_amt *= -1 #subtraction method
        for char in input_text:
            if char not in alphabet:
                nonletters = text.index(char)
                output_text.append(text[nonletters])
            else:
                text_indices = alphabet.index(char)
                output_indices = text_indices + shift_amt
                output_text.append(alphabet[output_indices])
        print(f"The {dir_choice}d text is {''.join(output_text)}.")
    
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).


    print(logo)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    
    caeser(text, shift, direction)

    go_again = input("Run the Cipher again? y or n\n").lower()
    if go_again == "y":
        clear()
    else:
        restart_prog = True
        print("Cipher terminated.")
    
# def encrypt(plain_text, shift_amt):
#     cipher_text = []
#     for char in plain_text:
#         text_indices = alphabet.index(char)
#         cipher_indices = text_indices + shift_amt
#         cipher_text.append(alphabet[cipher_indices])
#     print(f"The encoded text is {''.join(cipher_text)}.") 

# def decrypt(encrypted_text, shift_amt):
#     decipher_text = []
#     for char in encrypted_text:
#         text_indices = alphabet.index(char)
#         decipher_indices = text_indices - shift_amt
#         decipher_text.append(alphabet[decipher_indices])
#     print(f"The decoded text is {''.join(decipher_text)}.") 

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)


