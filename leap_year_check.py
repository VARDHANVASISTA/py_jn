year = int(input("Which year do you want to check? "))
if year%4 == 0:
    if year%100 != 0:
        print(f"!!{year} is a LEAP YEAR!!")
    elif year%400 == 0:
        print(f"!!{year} is a LEAP YEAR!!")
    else:
        print(f"!!{year} is NOT a LEAP YEAR!!")
else:
    print(f"!!{year} is NOT a LEAP YEAR!!")

