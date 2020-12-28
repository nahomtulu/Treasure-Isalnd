
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

row_numb = int(position[1]) - 1
column_numb = int(position[0]) - 1

deciding_row =  map[int(position[1]) - 1]
deciding_column = deciding_row[int(position[0]) - 1]

map[row_numb][column_numb] = "x"

print(f"{row1}\n{row2}\n{row3}")
