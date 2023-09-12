print("Welcome to BMI Calculator!!!")
height = input("Enter your height in metres: ")
weight = input("Enter your weight in kg: ")
bmi = float(weight)/float(height)**2
b1 = int(bmi)
print("Your BMI is: " + bmi + "\n approx.: " + b1)
