from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bidders = []
winner = {}
print("...!!!WELCOME TO BLIND AUCTION!!!...")
def ab():
    bidders.append({
        "Name": input("Enter your name >> "),
        "Bid": int(input("Enter your bid >> ₹"))
    })

ab()
rpt = True
while rpt:
    ob = input("Are there any other bidders? Type yes/no >> ").lower()
    if ob == "yes":
        clear()
        ab()
    elif ob =="no":
        max = 0
        for i in bidders:
            if i["Bid"] > max:
                max = i["Bid"]
                winner = {}
                winner = {
                    "N": i["Name"],
                    "B": i["Bid"],
                }
        rpt = False
    else:
        print("Wrong input!!! Try again...")

clear()
print("The Bids are:")
for i in bidders:
    print(f"Name: {i['Name']}     Bid: {i['Bid']}")
print(f"The winner is '{winner['N'].upper()}' with a bid of ₹ {winner['B']}\n{logo}")
