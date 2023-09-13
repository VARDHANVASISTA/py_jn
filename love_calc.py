print("!!Welcome to the Love Calculator!!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n1 = name1.upper()
n2 = name2.upper()
t1 = n1.count("T")
t2 = n2.count("T")
T = t1 + t2
r1 = n1.count("R")
r2 = n2.count("R")
R = r1 + r2
u1 = n1.count("U")
u2 = n2.count("U")
U = u1 + u2
e1 = n1.count("E")
e2 = n2.count("E")
E = e1 + e2
left = T+R+U+E
l1 = n1.count("L")
l2 = n2.count("L")
l = l1 + l2
o1 = n1.count("O")
o2 = n2.count("O")
o = o1 + o2
v1 = n1.count("V")
v2 = n2.count("V")
v = v1 + v2
right = l+o+v+E
score = left * 10 + right
if score<10 or score>90:
    print(f"Your score is {score}\n!!PERFECT MATCH!!")
elif score>40 and score<50:
    print(f"Your score is {score}\n!!GOOD MATCH!!")  
else:
    print(f"Your score is {score}")
