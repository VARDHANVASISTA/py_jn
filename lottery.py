import random
print("!!WELCOME to LOTTERY systems!!")
names_string = input("Enter everybody's names separated by a comma and a space. \n>>")
names = names_string.split(", ")
ch = random.randint(0,(len(names)-1))
n = names[ch].upper()
print("Congratulations... "+n+"\nYou have WON the LOTTERY!!")
