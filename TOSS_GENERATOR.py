import random
print("!!WELCOME TO TOSS GENERATOR!!")
print("Type 0 for HEADS or 1 for TAILS")
ch = int(input("HEADS or TAILS? >>")) 
cch = random.randint(0,1)
if ch == cch:
    print("You win!!")
    if cch == 0:
        print("Its HEADS!!")
    elif cch == 1:
        print("Its TAILS!!")
else:
    print("You loose!!")
    if cch == 0:
        print("Its HEADS!!")
    elif cch == 1:
        print("Its TAILS!!")
