# Create an application that allows you to input the string
# Then, the application goes through the whole file and checks if the requested string exists in each line
# Then, it shows to user how many lines have been found during the search process
# additional


word_to_find = input("Please enter the word you want to find in the file: \n")
line_tracker = 0

with open("rockyou.txt", encoding="latin-1") as file:
    line_list = [item.replace("\n", "").split() for item in file.readlines()]

    for check in line_list:
        if word_to_find in check:
            line_tracker += 1

print(f"The word '{word_to_find}' was found in {line_tracker} lines")
