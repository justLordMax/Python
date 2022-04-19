
# from turtle import position


# from turtle import position


row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

postion = input("Where do you want to put the treasure? ")

# METHOD 1

# side1 = ["x", "⬜️", "⬜️"]
# side2 = ["⬜️", "x", "⬜️"]
# side3 = ["⬜️", "⬜️", "x"]

# if postion == 11:
#     print(f"{side1}\n{row2}\n{row3}")
# elif postion == 21:
#     print(f"{side2}\n{row2}\n{row3}")
# elif postion == 31:
#     print(f"{side3}\n{row2}\n{row3}")
# elif postion == 12:
#     print(f"{row1}\n{side1}\n{row3}")
# elif postion == 22:
#     print(f"{row1}\n{side2}\n{row3}")
# elif postion == 32:
#     print(f"{row1}\n{side3}\n{row3}")
# elif postion == 13:
#     print(f"{row1}\n{row2}\n{side1}")
# elif postion == 23:
#     print(f"{row1}\n{row2}\n{side2}")
# elif postion == 33:
#     print(f"{row1}\n{row2}\n{side3}")

# METHOD 2

horizontal = int(postion[0])
vertical = int(postion[1])  

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")