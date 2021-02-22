import time

print("\n Welcome To Oxy Python Program")

print("\n What is Your Name? ")

name = input()

print("So, Your Name is " + str(name))

print("\n How Are You?")

how = input()

if how == "Fine":

  print("That's Good")

else:

    print("_")

print("\n Do You Want to Use Spam-Tool? " + "Type [Y] or [n]")

y = input()

if y == "Y":

  print("\nOpening Spam Tool...")

else:

 if y != "Y":
  exit()

   print("Program Finished")

time.sleep(3)

print("\nType What Do You Want to Spam?")

spam = input()

print("How Many Times , You want to spam" + " \n (Note: The More The Amount The More Time It Will Take) ")

times = int(input())

print("Spamming " + spam)

time.sleep(2)

print( spam * int(times) + "\n Successfully Spammed " + str("`"+spam+"`") +" "+ str(times) + " Times")

time.sleep(1)

print("\nPython Spam-Tool By Oxy")

time.sleep(1)

print("\nExecuted By " + name)

time.sleep(1)

print("\n To Contact Oxy - Paste This URL On Browser")

time.sleep(1)

print("\n https://www.instagram.com/_ig_oxy_/")
