# Kapittel 6, uppgift 2 - File Head Display
"""
2. File Head Display
Write a program that asks the user for the name of a file. The program should display only the
first five lines of the file’s contents. If the file contains less than five lines, it should display the
file’s entire contents.

"""
from tkinter.messagebox import showinfo

from pyexpat.errors import messages


def file_Head_Display():
    try:
        # Open the file to read
        with open('numbers.txt', 'r', encoding='utf-8') as file:
            # Läser alla rader i filen
            lines = file.readlines()
            # Skriva ut första fem raderna
            for line in lines[:5]:
                print(line.strip()) # Skriva ut varje rad
            if line < lines[5]:
                    print(lines)

    except FileNotFoundError:
        print("the file Numbers.txt was not found")


print(file_Head_Display())

"""
            # Read lines one by one
            for i, line in enumerate(file):
                if i < 5:  # Only process the first 5 lines
                    print(line.strip())  # Remove leading/trailing whitespace and print
                else:
                    break  # Stop after the first 5 lines

    except FileNotFoundError:
        print("The file 'numbers.txt' was not found.")

# Call the function
file_Head_Display()


"""