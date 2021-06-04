# # # no is even or odd
# # number=float(input("Enter the number \n"))
# # if(number%2==0):
# #     print("Number is zero")
# # else:
# #     print("Number is odd")
#
# #leap year
#
# # year=int(input("Enter the year \n"))
# # if(year%4==0 and year%400==0 and year%100!=0):
# #     print("leap year")
# # else:
# #     print("not Leap Year")
#
# # pizza order
# small_pizza = 100
# medium_pizza = 150
# large_pizza = 200
# add_small_pepperoni= 10
# add_pepperoni = 30
# add_extra_cheese= 25
# total_bill=0
#
# print("Welcome to Python Pizza Centre")
# print(f"Pricing is as follows: \nSmall pizza = Rs {small_pizza} \nMedium Pizza = Rs {medium_pizza} \nLarge Pizza = Rs {large_pizza}")
# print(f"Pepperoni:\n \tFor Small Pizza = Rs {add_small_pepperoni} \n \tfor Medium or Large Pizza = Rs {add_pepperoni}")
# print(f"Extra Cheese on any Pizza = Rs {add_extra_cheese}")
# size=input("What size pizza do you want?\nEnter S for small,M for medium and L for large size pizza\n")
#
# if(size=='s' or size=='S'):
#     total_bill += small_pizza
#     pepperoni = input("Do you want pepperoni?\nEnter Y or N\n")
#     if (pepperoni == 'y' or pepperoni == 'Y'):
#         total_bill += add_small_pepperoni
#         print("Pepperoni added")
#         extra_cheese = input("Do you want extra chees?\nEnter Y or N\n")
#         if(extra_cheese=='y'or extra_cheese=='Y'):
#             total_bill +=add_extra_cheese
#             print(f"Your bill with Extra cheese and pepperoni added = Rs {total_bill}")
#         elif (extra_cheese == 'N' or extra_cheese == 'n'):
#             total_bill += 0
#             print(f"Your bill without Extra cheese,with pepperoni = Rs {total_bill}")
#         else:
#             print("Wrong input")
#     else:
#         if(pepperoni=='N' or pepperoni=='n'):
#             extra_cheese = input("Do you want extra chees?\nEnter Y or N\n")
#             if (extra_cheese == 'y' or extra_cheese == 'Y'):
#                 total_bill += add_extra_cheese
#                 print(f"Your bill with Extra cheese and without pepperoni = Rs {total_bill}")
#             elif (extra_cheese == 'N' or extra_cheese == 'n'):
#                 total_bill += 0
#                 print(f"Your bill without Extra cheese and without pepperoni = Rs {total_bill}")
#             else:
#                 print("Wrong input")
# elif(size=='m' or size=='M'):
#     total_bill +=medium_pizza
#     pepperoni = input("Do you want pepperoni?\nEnter Y or N\n")
#     if (pepperoni == 'y' or pepperoni == 'Y'):
#         total_bill += add_pepperoni
#         print("Pepperoni added")
#         extra_cheese = input("Do you want extra chees?\nEnter Y or N\n")
#         if (extra_cheese == 'y' or extra_cheese == 'Y'):
#             total_bill += add_extra_cheese
#             print(f"Your bill with Extra cheese and pepperoni added = Rs {total_bill}")
#         elif (extra_cheese == 'N' or extra_cheese == 'n'):
#             total_bill += 0
#             print(f"Your bill without Extra cheese,with pepperoni = Rs {total_bill}")
#         else:
#             print("Wrong input")
#     else:
#         if (pepperoni == 'N' or pepperoni == 'n'):
#             extra_cheese = input("Do you want extra chees?\nEnter Y or N\n")
#             if (extra_cheese == 'y' or extra_cheese == 'Y'):
#                 total_bill += add_extra_cheese
#                 print(f"Your bill with Extra cheese and without pepperoni = Rs {total_bill}")
#             elif (extra_cheese == 'N' or extra_cheese == 'n'):
#                 total_bill += 0
#                 print(f"Your bill without Extra cheese and without pepperoni = Rs {total_bill}")
#             else:
#                 print("Wrong input")
# elif(size=='L' or size=='l'):
#     total_bill +=large_pizza
#     pepperoni= input("Do you want pepperoni?\nEnter Y or N\n")
#     if (pepperoni == 'y' or pepperoni == 'Y'):
#         total_bill += add_pepperoni
#         print("Pepperoni added")
#         extra_cheese = input("Do you want extra chees?\nEnter Y or N\n")
#         if(extra_cheese=='y'or extra_cheese=='Y'):
#             total_bill +=add_extra_cheese
#             print(f"Your bill with Extra cheese and pepperoni added = Rs {total_bill}")
#         elif (extra_cheese == 'N' or extra_cheese == 'n'):
#             total_bill += 0
#             print(f"Your bill without Extra cheese, with pepperoni = Rs {total_bill}")
#         else:
#             print("Wrong input")
#     else:
#         if(pepperoni=='N' or pepperoni=='n'):
#             extra_cheese = input("Do you want extra chees?\nEnter Y or N\n")
#             if (extra_cheese == 'y' or extra_cheese == 'Y'):
#                 total_bill += add_extra_cheese
#                 print(f"Your bill with Extra cheese and without pepperoni added = Rs {total_bill}")
#             elif(extra_cheese == 'N' or extra_cheese == 'n'):
#                 total_bill += 0
#                 print(f"Your bill without Extra cheese and without pepperoni = Rs {total_bill}")
#             else:
#                 print("Wrong input")


# # love calculator
# print("Welcome to the Love Calculator")
# #entering your name
#
# your_name= input("Enter your name\n")
# your_name= your_name.lower()
#
# #entering crush name
#
# crush_name = input("Enter your crush name\n")
# crush_name = crush_name.lower()
#
#
# #counting the t,r,u,e in your name
#
# t_in_both_name=your_name.count('t') + crush_name.count('t')
# r_in_both_name=your_name.count('r') + crush_name.count('r')
# u_in_both_name=your_name.count('u') + crush_name.count('u')
# e_in_both_name=your_name.count('e') + crush_name.count('e')
#
# #counting l,o,v,e in your name
#
# l_in_both_name=your_name.count('l') + crush_name.count('l')
# o_in_both_name=your_name.count('o') + crush_name.count('o')
# v_in_both_name=your_name.count('v') + crush_name.count('v')
# e1_in_both_name=your_name.count('e') +crush_name.count('e')
#
# #calculating
#
# print(f"t occurs {t_in_both_name} times \nr occurs {r_in_both_name} times \nu occurs {u_in_both_name} times \ne occurs {e_in_both_name} times \n\n")
# total_true=+t_in_both_name+u_in_both_name+r_in_both_name+e_in_both_name
# print("Total = ",total_true)
# '\n'
#
# print(f"l occurs {l_in_both_name} times \no occurs {o_in_both_name} times \nv occurs {v_in_both_name} times \ne occurs {e1_in_both_name} times\n\n")
# total_love=l_in_both_name+o_in_both_name+v_in_both_name+e1_in_both_name
# print("Total = ",total_love)
#
#
# sum=str(total_true)+str(total_love)
# sum=int(sum)
# print("love %=",sum)
#
# #output
#
# if(sum< 10 or sum>=90):
#     print(f"Your score is {sum},you go together like coke and mentos.")
# elif(sum>=40 and sum<=50):
#     print(f"Your score is {sum},you are alright together.")
# else:
#     print(f"Your score is {sum}.")


# love calculator
print("Welcome to the Love Calculator")
#entering your name

your_name= input("Enter your name\n")
your_name= your_name.lower()

#entering crush name

crush_name = input("Enter your crush name\n")
crush_name = crush_name.lower()


#counting the t,r,u,e in your name

t_in_both_name=your_name.count('t') + crush_name.count('t')
r_in_both_name=your_name.count('r') + crush_name.count('r')
u_in_both_name=your_name.count('u') + crush_name.count('u')
e_in_both_name=your_name.count('e') + crush_name.count('e')

#counting l,o,v,e in your name

l_in_both_name=your_name.count('l') + crush_name.count('l')
o_in_both_name=your_name.count('o') + crush_name.count('o')
v_in_both_name=your_name.count('v') + crush_name.count('v')
e1_in_both_name=your_name.count('e') +crush_name.count('e')

#calculating

print(f"t occurs {t_in_both_name} times \nr occurs {r_in_both_name} times \nu occurs {u_in_both_name} times \ne occurs {e_in_both_name} times \n")
total_true=+t_in_both_name+u_in_both_name+r_in_both_name+e_in_both_name
print(f"Total = {total_true} \n")

print(f"l occurs {l_in_both_name} times \no occurs {o_in_both_name} times \nv occurs {v_in_both_name} times \ne occurs {e1_in_both_name} times\n")
total_love=l_in_both_name+o_in_both_name+v_in_both_name+e1_in_both_name
print(f"Total = {total_love} \n")

sum=str(total_true)+str(total_love)
sum=int(sum)

#output

'\n'

if(sum< 10 or sum>=90):
    print(f"Your score is {sum}% ,you go together like coke and mentos.")
elif(sum>=40 and sum<=50):
    print(f"Your score is {sum}% ,you are alright together.")
else:
    print(f"Your score is {sum}% .")