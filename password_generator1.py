#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("!!WELCOME TO THE STRONG-PASSWORD GENERATOR!!")
pl= int(input("What should be the length of your password?\n>>")) 
ns = int(input("How many symbols would you like?\n>>"))
nn = int(input("How many numbers would you like?\n>>"))
pt = []
for n in range(0,(pl-ns-nn)):
  pt.append(random.choice(letters))
for n in range(0,ns):
  pt.append(random.choice(symbols))
for n in range(0,nn):
  pt.append(random.choice(numbers))
  
#for the below version of shuffling the list there is a function called shuffle() the code using it is at the last>>
sp = []
for n in range(0,len(pt)):
  t=(random.choice(pt))
  sp.append(t)
  for i in numbers:
    if i == t:
      pt.remove(t)
  for i in symbols:
    if i == t:
      pt.remove(t)
print("Your Strong-Password is >>")
for i in sp:
  print(i,end='')

#shuffling list using shuffle() function >>easier version
random.shuffle(pt)
print("Your Strong-Password is >>")
for i in pt:
  print(i,end='')
