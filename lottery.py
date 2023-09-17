#Basic version
import random
print("!!WELCOME to LOTTERY systems!!")
names_string = input("Enter everybody's names separated by a comma and a space. \n>>")
names = names_string.split(", ")
ch = random.randint(0,(len(names)-1))
n = names[ch].upper()
print("Congratulations... "+n+"\nYou have WON the LOTTERY!!")

#shortened version of the above
import random
print("!!WELCOME to LOTTERY systems!!")
names_string = input("Enter everybody's names separated by a comma and a space. \n>>")
names = names_string.split(", ")
print("Congratulations... "+names[random.randint(0,(len(names)-1))].upper()+"\nYou have WON the LOTTERY!!")



#Below one is an easier version
import random
print("!!WELCOME to LOTTERY systems!!")
names_string = input("Enter everybody's names separated by a comma and a space. \n>>")
names = names_string.split(", ")
n = random.choice(names).upper()
print("Congratulations... "+n+"\nYou have WON the LOTTERY!!")

#shortened version of the above
import random
print("!!WELCOME to LOTTERY systems!!")
names_string = input("Enter everybody's names separated by a comma and a space. \n>>")
names = names_string.split(", ")
print("Congratulations... "+(random.choice(names)).upper()+"\nYou have WON the LOTTERY!!")
