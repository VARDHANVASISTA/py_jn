print("Welcome to BMI Calculator!!!")
height = input("Enter your height in metres: ")
weight = input("Enter your weight in kg: ")
b = float(weight)/float(height)**2
b1 = int(b)
bs = str(b)
b1s = str(b1)
print("Your BMI is: " + bs + "\n approx. BMI: " + b1s)
