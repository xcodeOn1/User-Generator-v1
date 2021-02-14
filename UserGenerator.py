import random
import sys
import os
import time

os.system("clear")
os.system("figlet User Generator v1 ")
print("\n")
print("#Coded-By   : Xcode")
time.sleep(2)
print("#Twitter  : XcodeOn1")
time.sleep(1)
print("\n")




#================================================
allchars = 'asdfghjklzxcvbnmqwertyuiop1234567890' 
amount = input('How many user you want ? : ')
amount = int(amount)

length2 = input('How much chars you want ? : ')
length2 = int(length2)
print("\n")


for Users in range(amount):
    Users = ''
    
    
    for item in range(length2):
         Users = ''
    for item in range(length2):
        Users += random.choice(allchars)
Snapchat: gtoe 



    print (Users)
    with open('Users.txt', 'a') as x:
     x.write(Users + '\n')
print("\n")
print('Plese check of Text-file could " # Users.txt "')
