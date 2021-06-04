import random
from word_list import word_list
from word_list import stages
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
name1=str(random.choice(word_list))
name1=name1.lower()
length=len(name1)
print(logo)



display=[]
for i in range(length):
    display +='_'
print(f"Word you have to guess have {len(display)} letters \n")
print(display)
end_of_game=False
life=6



while not end_of_game:
    guess=input("Guess the letter:").lower()
    print(guess)
    for i in range(length):
        letter=name1[i]
        if(letter==guess):
            display[i]=guess

    if guess not in name1:
        life-=1
        print(stages[life])
        if life==0:
            end_of_game=True
            print("Game Over.You are out of the life")
    print(f"{display}.Remaining life is {life}")

    if "_" not in display:
        end_of_game=True
        print("You Win")
print(''.join(display))
print(f"Correct word is {name1}")