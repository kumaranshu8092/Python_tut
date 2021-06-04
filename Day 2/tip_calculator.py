print("Welcome to the tip calculator")
total_amt=input("What was the total bill amount? \n $")
total_amt=float(total_amt)
no_of_people=input("How many people are there to split the bill? \n")
no_of_people=int(no_of_people)
tip=float(input("how much tip you would like to give in %? 10% or 15% or 20% \n %"))
if(tip==10):
    tip=(10*total_amt)/100
elif(tip==15):
    tip=(15*total_amt)/100
elif(tip==20):
    tip=(20*total_amt)/100

if(no_of_people < 0 or no_of_people==0):
    per_person_payment="{:.2f}".format(total_amt+tip)
    print(f"Amount you have to pay is {per_person_payment}")
else:
    per_person_payment="{:.2f}".format((total_amt+tip)/no_of_people)
    print("Amount each person have to pay is : \n $",per_person_payment)