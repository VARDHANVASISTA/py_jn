from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""




def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def pow(a, b):
    return a**b

def mod(a, b):
    return a%b

def sqrt(a):
    return a**0.5

def nth_root(a, n):
    return a**(1/n)

def log_a_base_b(a, b):
    return b**(1/a)

def log_base_10(a):
    return 10**(1/a)

operation2n = {
    "+": add,
    "-": subtract,
    "*": mul,
    "/": div,
    "**": pow,
    "mod": mod,
    "nth_root": nth_root,
    "log(a)_base(b)": log_a_base_b,
}
operation1n = {
    "sqrt": sqrt,
    "log_base_10": log_base_10,
}
print(logo)
ta = True
while ta:
    i = input("Type 1 for Single number operation\nType 2 for Double number operation\nType any other key to quit\nEnter your choice >> ")
    if i == "1":
        n = float(input("Enter the number >> "))
        for i in operation1n:
            print(i)
        print("Choose any one operation from the above... ")
        opv = True
        while opv:
            o = input("Enter the operation >>")
            if o in operation1n:
                opf = operation1n[o]
                r = opf(n)
                print(f"{o} {n} = {r}")
                co = True
                while co:
                    cnq = input(f"To continue operation with {r}, Type c  OR\nTo do a new calculation, Type n  OR\nTo quit type any other key >> ").lower()
                    if cnq == "c":
                        nc = input("Type 1 for Single number operation\nType 2 for Double number operation\nType any other key to quit\nEnter your choice >> ")
                        if nc == "1":
                            n = r
                            clear()
                            for i in operation1n:
                                print(i)
                            print("Choose any one operation from the above... ")
                            o = input("Enter the operation >> ")
                            if o in operation1n:
                                opf = operation1n[o]
                                r = opf(n)
                                print(f"{o} {n} = {r}")
                                nn = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                if nn == "c":
                                    clear()
                                    continue
                                else:
                                    opv = False
                                    co = False
                                    ta = False
                                    print("Thank you for using the calculator...\nGoodbye...")
                                    break
                            else:    
                                print("Invalid choice...")
                                nn = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                if nn == "c":
                                    clear()
                                    continue
                                else:
                                    opv = False
                                    co = False
                                    ta = False
                                    print("Thank you for using the calculator...\nGoodbye...")
                                    break
                        elif nc == "2":
                            clear()
                            fs = int(input(f"For {r} to be 1st number, Type 1 OR For {r} to be 2nd number, Type 2 >> "))
                            if fs == 1:
                                a = r
                                b = float(input("Type the second number >> "))
                                if b == 0:
                                    vv = input("With b = 0, You cannot perform division...\nIf you want to choose operation other than division, Type c\nIf you want to re-enter, Type r\nOR Type any other key to quit >> ").lower()
                                    if vv == 'c':
                                        for i in operation2n:
                                            if i == '/':
                                                continue
                                            print(i)
                                        print("Choose any one operation from the above... ")
                                        o = input("Enter the operation >> ")
                                        if o in operation2n:
                                            opf = operation2n[o]
                                            r = opf(a, b)
                                            print(f"{a} {o} {b} = {r}")
                                        else:
                                            print("Invalid choice...")
                                            gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                            if gg == 'c':
                                                clear()
                                                continue
                                            else:
                                                opv = False
                                                co = False
                                                ta = False
                                                print("Thank you for using the calculator...\nGoodbye...")
                                                break
                                    elif vv == 'r':
                                        b = float(input("Type the second number >> "))
                                        for i in operation2n:
                                            print(i)
                                        print("Choose any one operation from the above... ")
                                        o = input("Enter the operation >> ")
                                        if o in operation2n:
                                            opf = operation2n[o]
                                            r = opf(a, b)
                                            print(f"{a} {o} {b} = {r}")
                                        else:
                                            print("Invalid choice...")
                                            gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                            if gg == 'c':
                                                clear()
                                                continue
                                            else:
                                                opv = False
                                                co = False
                                                ta = False
                                                print("Thank you for using the calculator...\nGoodbye...")
                                                break
                                    else:
                                        opv = False
                                        co = False
                                        ta = False
                                        print("Thank you for using the calculator...\nGoodbye...")
                                        break    
                                else:
                                    for i in operation2n:
                                        print(i)
                                    print("Choose any one operation from the above... ")
                                    o = input("Enter the operation >> ")
                                    if o in operation2n:
                                        opf = operation2n[o]
                                        r = opf(a, b)
                                        print(f"{a} {o} {b} = {r}")
                                    else:
                                        print("Invalid choice...")
                                        gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                        if gg == 'c':
                                            clear()
                                            continue
                                        else:
                                            opv = False
                                            co = False
                                            ta = False
                                            print("Thank you for using the calculator...\nGoodbye...")
                                            break
                            elif fs == 2:
                                b = r
                                a = float(input("Type the first number >> "))
                                for i in operation2n:
                                    print(i)
                                print("Choose any one operation from the above... ")
                                o = input("Enter the operation >> ")
                                if o in operation2n:
                                    opf = operation2n[o]
                                    r = opf(a, b)
                                    print(f"{a} {o} {b} = {r}")
                                else:
                                    print("Invalid choice...")
                                    gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                    if gg == 'c':
                                        clear()
                                        continue
                                    else:
                                        opv = False
                                        co = False
                                        ta = False
                                        print("Thank you for using the calculator...\nGoodbye...")
                                        break
                            else:
                                print("Invalid choice...")
                                gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                if gg == 'c':
                                    clear()
                                    continue
                                else:
                                    opv = False
                                    co = False
                                    ta = False
                                    print("Thank you for using the calculator...\nGoodbye...")
                                    break
                        else:
                            print("Invalid choice...")
                            gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                            if gg == 'c':
                                clear()
                                continue
                            else:
                                opv = False
                                co = False
                                ta = False
                                print("Thank you for using the calculator...\nGoodbye...")
                                break
                    elif cnq == 'n':
                        clear()
                        print(logo)
                        opv = False
                        co = False
                        continue
                    else:
                        opv = False
                        co = False
                        ta = False
                        print("Thank you for using the calculator...\nGoodbye...")
                        break                                
            else:
                print("Invalid operator...\nEnter any one from the given list...")
                sd = input("Type y to try again OR any other key to quit >> ").lower()
                if sd == 'y':
                    continue
                else:
                    print("Thank you for using the calculator...\nGoodbye...")
                    opv = False
                    ta = False
    elif i == "2":
        a = float(input("Enter the first number >> "))
        b = float(input("Enter the second number >> "))
        for i in operation2n:
            print(i)
        print("Choose any one operation from the above... ")
        opv = True
        while opv:
            o = input("Enter the operation >> ")
            if o in operation2n:
                opf = operation2n[o]
                r = opf(a, b)
                print(f"{a} {o} {b} = {r}")
                co = True
                while co:
                    cnq = input(f"To continue operation with {r}, Type c  OR\nTo do a new calculation, Type n  OR\nTo quit type any other key >> ").lower()
                    if cnq == "c":
                        nc = input("Type 1 for Single number operation\nType 2 for Double number operation\nType any other key to quit\nEnter your choice >> ")
                        if nc == "1":
                            n = r
                            clear()
                            for i in operation1n:
                                print(i)
                            print("Choose any one operation from the above... ")
                            o = input("Enter the operation >> ")
                            if o in operation1n:
                                opf = operation1n[o]
                                r = opf(n)
                                print(f"{o} {n} = {r}")
                                nn = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                if nn == "c":
                                    continue
                                else:
                                    opv = False
                                    co = False
                                    ta = False
                                    print("Thank you for using the calculator...\nGoodbye...")
                                    break
                            else:    
                                print("Invalid choice...")
                                nn = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                if nn == "c":
                                    continue
                                else:
                                    opv = False
                                    co = False
                                    ta = False
                                    print("Thank you for using the calculator...\nGoodbye...")
                                    break
                        elif nc == "2":
                            clear()
                            fs = int(input(f"For {r} to be 1st number, Type 1 OR For {r} to be 2nd number, Type 2 >> "))
                            if fs == 1:
                                a = r
                                b = float(input("Type the second number >> "))
                                if b == 0:
                                    vv = input("With b = 0, You cannot perform division...\nIf you want to choose operation other than division, Type c\nIf you want to re-enter, Type r\nOR Type any other key to quit >> ").lower()
                                    if vv == 'c':
                                        for i in operation2n:
                                            if i == '/':
                                                continue
                                            print(i)
                                        print("Choose any one operation from the above... ")
                                        o = input("Enter the operation >> ")
                                        if o in operation2n:
                                            opf = operation2n[o]
                                            r = opf(a, b)
                                            print(f"{a} {o} {b} = {r}")
                                        else:
                                            print("Invalid choice...")
                                            gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                            if gg == 'c':
                                                continue
                                            else:
                                                opv = False
                                                co = False
                                                ta = False
                                                print("Thank you for using the calculator...\nGoodbye...")
                                                break
                                    elif vv == 'r':
                                        b = float(input("Type the second number >> "))
                                        for i in operation2n:
                                            print(i)
                                        print("Choose any one operation from the above... ")
                                        o = input("Enter the operation >> ")
                                        if o in operation2n:
                                            opf = operation2n[o]
                                            r = opf(a, b)
                                            print(f"{a} {o} {b} = {r}")
                                        else:
                                            print("Invalid choice...")
                                            gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                            if gg == 'c':
                                                continue
                                            else:
                                                opv = False
                                                co = False
                                                ta = False
                                                print("Thank you for using the calculator...\nGoodbye...")
                                                break
                                    else:
                                        opv = False
                                        co = False
                                        ta = False
                                        print("Thank you for using the calculator...\nGoodbye...")
                                        break    
                                else:
                                    for i in operation2n:
                                        print(i)
                                    print("Choose any one operation from the above... ")
                                    o = input("Enter the operation >> ")
                                    if o in operation2n:
                                        opf = operation2n[o]
                                        r = opf(a, b)
                                        print(f"{a} {o} {b} = {r}")
                                    else:
                                        print("Invalid choice...")
                                        gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                        if gg == 'c':
                                            continue
                                        else:
                                            opv = False
                                            co = False
                                            ta = False
                                            print("Thank you for using the calculator...\nGoodbye...")
                                            break
                            elif fs == 2:
                                b = r
                                a = float(input("Type the first number >>"))
                                for i in operation2n:
                                    print(i)
                                print("Choose any one operation from the above... ")
                                o = input("Enter the operation >> ")
                                if o in operation2n:
                                    opf = operation2n[o]
                                    r = opf(a, b)
                                    print(f"{a} {o} {b} = {r}")
                                else:
                                    print("Invalid choice...")
                                    gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                    if gg == 'c':
                                        continue
                                    else:
                                        opv = False
                                        co = False
                                        ta = False
                                        print("Thank you for using the calculator...\nGoodbye...")
                                        break
                            else:
                                print("Invalid choice...")
                                gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                                if gg == 'c':
                                    continue
                                else:
                                    opv = False
                                    co = False
                                    ta = False
                                    print("Thank you for using the calculator...\nGoodbye...")
                                    break
                        else:
                            print("Invalid choice...")
                            gg = input("Do you want to continue? Type c to continue OR\nType any other key to quit >> ").lower()
                            if gg == 'c':
                                continue
                            else:
                                opv = False
                                co = False
                                ta = False
                                print("Thank you for using the calculator...\nGoodbye...")
                                break
                    elif cnq == 'n':
                        clear()
                        print(logo)
                        opv = False
                        co = False
                        continue
                    else:
                        opv = False
                        co = False
                        ta = False
                        print("Thank you for using the calculator...\nGoodbye...")
                        break 
            else:
                print("Invalid operator...\nEnter any one from the given list...")
                sd = input("Type y to try again OR any other key to quit >> ").lower()
                if sd == 'y':
                    continue
                else:
                    print("Thank you for using the calculator...\nGoodbye...")
                    opv = False
                    ta = False
    else:
        print("Invalid choice...\nEnter 1 or 2...")
        sd = input("Type y to try again OR Any other key to quit >> ").lower()
        if sd == "y":
            clear()
        else:
            print("Thank you for using the calculator...\nGoodbye...")
            ta = False
