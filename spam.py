print("\n Welcome To Oxy Python Program")

print("\n What is Your Name? ")

name = input()

print(  " So, Your Name is " + str(name ))

print("\n How Are You?")

input()

print("\nWhat is Your Age? " + name + " (In Integers)")

age = int(input())

if age >= 50:

  print("Old Is Gold")

  if age >=100:

    print("Invalid-age, Please Try again Later")

    print("\n Program Stopped, To Run, Execute It Again")

    exit()

print("\nOpening Spam Machine...")

print("\n3" + "\n2" + "\n1")

  

print("Type What You Want to Spam")

spam = input()

print("How Many Times , You want to spam" + " \n Note: The More The Amount The More Time It Will Take ")

times = int(input())

print(spam * int(times) + "\n Successfully Spammed " + str("`"+spam+"`") +" "+ str(times) + " Times")

   

   
