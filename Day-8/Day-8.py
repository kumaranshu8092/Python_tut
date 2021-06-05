# def my_func():
#     print("Hello")
#     print("This is my 1st function")
#     print("My tutor is Dr. Angela Yu")
#
# my_func()

# def challenge(name,location):
#     print(f"hello my name is {name}")
#     print(f"I live in {location}")
#
# challenge(location='Ranchi',name='Sudarshan')

# exercise-8.1
# import math
# def paint_calc(height,width,cover):
#     area=height*width
#     can_required= (height* width)/coverage
#     print(f"Can required to paint the whole wall {math.ceil(can_required)}")
#
# test_h =int(input("Height of wall: \n"))
# test_w =int(input("Width of wall : \n"))
# coverage=5
# paint_calc(width=test_w,height=test_h,cover=coverage)

# prime_no
# n=int(input("Enter the no you want to check"))
#
# def prime(number):
#
#     for i in range(2,number):
#         if number >1 and number%i==0:
#             print("Not prime")
#             break
#         else:
#             print("prime")
#             break
#
# prime(number=n)
#or

def prime_check(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime= False
    if is_prime:
        print("YEssss")
    else:
        print("Not a prime no")
prime_check(5)