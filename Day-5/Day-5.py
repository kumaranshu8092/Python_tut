# #the average height
# st_height=input("Enter the height of student \n").split()
# for i in range(0,len(st_height)):
#     st_height[i]=int(st_height[i])
# print(st_height)
# sum=0
# for i in range(0,len(st_height)):
#     sum+=st_height[i]
# average_height=sum/len(st_height)
# print(f"Average height of class is {round(average_height,2)}")

# highest score in the class
# highest_score=0
# score=input("Enter the score of students \n").split()
# for i in range(0,len(score)):
#     score[i]=float(score[i])
# print(score)
# for i in range(0,len(score)):
#     if(score[i]>highest_score):
#         highest_score=score[i]
# print(f"Highest score is {highest_score}")


for i in range(1,101):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
    elif(i%5==0):
        print('Buzz')
    elif(i%3==0):
        print('Fizz')
    else:
        print(i)

