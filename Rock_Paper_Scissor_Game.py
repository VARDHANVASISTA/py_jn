import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("!!WELCOME TO ROCK-PAPER-SCISSOR GAME!!")
com = random.randint(0,2)
yc = int(input("Type 0 for ROCK or 1 for PAPER or 2 for SCISSORS  >>"))
if yc == 0:
  if com == 0:
    print("Your choice:\n"+rock+"!!ROCK!!")
    print("Computer's choice:\n"+rock+"!!ROCK!!")
    print("\n\n!!IT's A DRAW!!.....")
  elif com == 1:
    print("Your choice:\n"+rock+"!!ROCK!!")
    print("Computer's choice:\n"+paper+"!!PAPER!!")
    print("\n\n!!YOU LOOSE!!...!!COMPUTER WINS!!...")
  elif com == 2:
    print("Your choice:\n"+rock+"!!ROCK!!")
    print("Computer's choice:\n"+scissors+"!!SCISSORS!!")
    print("\n\nCongratulations...\n!!YOU WIN!!.....")
elif yc == 1:
  if com == 0:
    print("Your choice:\n"+paper+"!!PAPER!!")
    print("Computer's choice:\n"+rock+"!!ROCK!!")
    print("\n\nCongratulations...\n!!YOU WIN!!.....")
  elif com == 1:
    print("Your choice:\n"+paper+"!!PAPER!!")
    print("Computer's choice:\n"+paper+"!!PAPER!!")
    print("\n\n!!IT's A DRAW!!.....")
  elif com == 2:
    print("Your choice:\n"+paper+"!!PAPER!!")
    print("Computer's choice:\n"+scissors+"!!SCISSORS!!")
    print("\n\n!!YOU LOOSE!!...!!COMPUTER WINS!!...")
elif yc == 2:
  if com == 0:
    print("Your choice:\n"+scissors+"!!SCISSORS!!")
    print("Computer's choice:\n"+rock+"!!ROCK!!")
    print("\n\n!!YOU LOOSE!!...!!COMPUTER WINS!!...")
  elif com == 1:
    print("Your choice:\n"+scissors+"!!SCISSORS!!")
    print("Computer's choice:\n"+paper+"!!PAPER!!")
    print("\n\nCongratulations...\n!!YOU WIN!!.....")
  elif com == 2:
    print("Your choice:\n"+scissors+"!!SCISSORS!!")
    print("Computer's choice:\n"+scissors+"!!SCISSORS!!")
    print("\n\n!!IT's A DRAW!!.....")
else:
  print("!!ERROR!!...\nWrong choice...\nTry again...")
