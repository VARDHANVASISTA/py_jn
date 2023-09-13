height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kg: "))
b1 = weight/height**2
b = b1
bmi = round(b1)
if bmi < 18.5:
    print(f"Your BMI is: {b}\n i.e., approx. BMI: {bmi}\n!!You are UNDERWEIGHT!!")
elif bmi<=25:
    print(f"Your BMI is: {b}\n i.e., approx. BMI: {bmi}\n!!You have a NORMAL WEIGHT!!")
elif bmi<=30:
    print(f"Your BMI is: {b}\n i.e., approx. BMI: {bmi}\n!!You are SLIGHTLY OVERWEIGHT!!")
elif bmi<=35:
    print(f"Your BMI is: {b}\n i.e., approx. BMI: {bmi}\n!!You are OBESE!!")
else:
    print(f"Your BMI is: {b}\n i.e., approx. BMI: {bmi}\n!!You are CLINICALLY OBESE!!")
