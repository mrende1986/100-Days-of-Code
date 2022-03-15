# with open("iCloud/Documents/100 Days of Code/Day 24/my_file.txt") as file:

#     contents = file.read()
#     print(contents)

with open("iCloud/Documents/100 Days of Code/Day 24/my_file.txt", mode="a") as file:

    file.write("\nnew text.")

with open("iCloud/Documents/100 Days of Code/Day 24/new_file.txt", mode="w") as file:
    file.write("\nnew text.")
