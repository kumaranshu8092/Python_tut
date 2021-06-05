alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text,shift):
#     cypher_text=""
#     for letter in text:
#         position=alphabet.index(letter)
#         new_position= position + int(shift)
#         new_letter=alphabet[new_position]
#         cypher_text+=new_letter
#     print(f"The encoded text is {cypher_text}")
#
# def decrypt(text,shift):
#     cypher_text=""
#     for letter in text:
#         position=alphabet.index(letter)
#         new_position=position - int(shift)
#         new_letter=alphabet[new_position]
#         cypher_text+=new_letter
#     print(f"The decoded text is {cypher_text}")
# if direction=='encode':
#     encrypt(text,shift)
# elif direction=='decode':
#     decrypt(text,shift)

def ceasar(text,shift,direction):
    cypher_text=""
    if direction == 'encode':
        shift *= +1
    elif direction == 'decode':
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position= position + shift
            new_letter=alphabet[new_position]
            cypher_text+=new_letter
        else:
            cypher_text+= letter
    print(f"The {direction} text is {cypher_text}")

again=True
while again:
    direction=input("type 'encode' to encrypt or type 'decode' to decrypt\n")
    text=input("type your message\n").lower()
    shift=int(input("Type the shift number \n"))
    shift=shift%26
    ceasar(text, shift, direction)
    enter=input("You want to continue enter 'Yes' if don't type 'No' \n")
    if enter=='No' or enter=='no':
        again=False
        print("GoodBye!")
    elif enter=='Yes' or enter=='yes':
        again=True
    else:
        print("Invalid input")
        break