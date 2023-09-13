print("!!Welcome to PIZZA BILLING!!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want PIRI-PIRI MASALA? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: Rs.{bill}")
    else:
        print(f"Your final bill is: Rs.{bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: Rs.{bill}")
    else:
        print(f"Your final bill is: Rs.{bill}"))
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: Rs.{bill}")
    else:
        print(f"Your final bill is: Rs.{bill}")
else:
  print("!!WRONG SIZE!!\nENTER AGAIN>>")
