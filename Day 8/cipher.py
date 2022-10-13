#encrypting and decrypting text

def caesar(text,shift,direction):
    result=""
    if direction=="encode":
        for letter in text:
            result+=alphabet[shift+alphabet.index(letter)]
    elif direction=="decode":
        for letter in text:
            result+=alphabet[alphabet.index(letter)+26-shift]
    print(f"The {direction}d text is {result}")
        

# def encrypt(text,shift):
#     result_encrypt=""
#     for letter in text:
#         result_encrypt+=alphabet[shift+alphabet.index(letter)]
#     print(f"Your encrypted message is {result_encrypt}")

# def decrypt(text,shift):
#     result_decrypt=""
#     for letter in text:
#         result_decrypt+=alphabet[alphabet.index(letter)+26-shift]
#     print(f"Your decrypted message is {result_decrypt}")



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']
choice="yes"
while choice=="yes":
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    # if direction=="encode":
    #     encrypt(text,shift)
    # if direction=="decode":
    #     decrypt(text,shift)
    choice=input("To continue press yes else press no: ")