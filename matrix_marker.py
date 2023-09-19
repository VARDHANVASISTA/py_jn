print("!!WELCOME TO MATRIX TRAINER FOR BEGINNERS IN MATRIX FORMAT")
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("This is a 3X3 matrix you have row number and column number as 1,2,3 for both")
print("To see a particular position type its row number and its column number as a continuous number")
position = input("Which position do you want to see? ")
c = int(position) % 10
r = int(int(position) / 10)
map[r - 1][c - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
