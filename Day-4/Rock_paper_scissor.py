Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
value=input("What do you choose? \nType 0 for Rock 1 for Paper 2 for Scissors. \n")
computer_choose=random.randint(0,2)
print(f"Computer choose {computer_choose}")
value=int(value)
if(value==0):
    print(f"Rock \n{Rock}")
elif(value==1):
    print(f"Paper \n{Paper}")
elif(value==2):
    print(f"Scissors \n{Scissor}")
else:
    print("Invalid Input\n")

if(computer_choose==0):
    print(f"Rock \n{Rock}")
elif(computer_choose==1):
    print(f"Paper \n{Paper}")
elif(computer_choose==2):
    print(f"Scissors \n{Scissor}")
else:
    print("Invalid Input\n")

if(value==computer_choose):
    print("Match draw")
elif(value==0 and computer_choose==2 or value==1 and computer_choose==0 or value==2 and computer_choose==1):
    print("You win")
else:
    print("Computer Wins")