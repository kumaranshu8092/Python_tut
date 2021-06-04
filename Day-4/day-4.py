# import random
# print("Welcome to the Stone,Paper and Scissor Game")
#
# love_score=random.randint(1,100)
# print(f"Your love score is {love_score}%")

# import random
# ran_toss=random.randint(0,1)
# if(ran_toss==1):
#     print('Heads')
# else:
#     print('Tails')

# list
#import random
#name_entered=input("Enter Everybody's name in a row saperated by a comma \n")
#name_entered=['Sudarshan', 'Gucci', 'Shubh', 'Rai', 'Sethi']
#print(name_entered)
#name=name_entered.split(", ")
# total_name=len(name)
# random_index=random.randint(0,total_name-1)
# person_who_will_pay=name[random_index]
# print(f"{person_who_will_pay} is going to give treat today ")

#choice function from random module will do the work of above written prog.
#print(random.choice(name)+ " Will give party\n")

# treasure map

row1=["😍","😍","😍"]
row2=["😍","😍","😍"]
row3=["😍","😍","😍"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? \n")
horizontal=int(position[0])
vertical=int(position[1])
row_selected=map[vertical-1]
row_selected[horizontal-1]='T'
print(f"{row1}\n{row2}\n{row3}")

