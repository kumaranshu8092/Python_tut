import random
import string
alphabet=string.ascii_lowercase
Alphabet=string.ascii_uppercase
letters=list(alphabet)+list(Alphabet)
#print(letters)
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']

print("Welcome to the PyPassword Generator\n")
no_letters= int(input("how many Alphabet would you like?\n"))
no_symbols= int(input("how many Symbol would you like? \n"))
no_number= int(input("how many Number would you like? \n"))


let=(''.join(random.choice(letters) for i in range(no_letters)))
sym=(''.join(random.choice(symbols) for i in range(no_symbols)))
num=(''.join(random.choice(numbers) for i in range(no_number)))

pas=list(let)+list(sym)+list(num)
password=(''.join(random.choice(pas) for i in range(0,len(pas))))
print(password)