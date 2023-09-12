print("Welcome to the bill split calculator!!")
total = input("What was the total bill? Rs. ")
tb = float(total)
per = input("What percentage tip would you like to give? 10 or 12 or 15? ")
pt = int(per)
peo = input("How many people are splitting the bill? ")
np = int(peo)
tip = pt / 100 * tb
tb += tip
split = tb / np
sp = round(split , 2)
print(f"Each person should pay Rs. {sp}")
