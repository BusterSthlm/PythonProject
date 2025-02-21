# Kapittel 6, uppgift 2 - File Head Display
"""
2. File Head Display
Write a program that asks the user for the name of a file. The program should display only the
first five lines of the file’s contents. If the file contains less than five lines, it should display the
file’s entire contents.

"""



def file_Head_Display():
    try:
        # Testar att öppna filen
        with open('numbers.txt', 'r', encoding='utf-8') as file: #öppnar filen med while på säkert sätt
            # Läser alla rader i filen
            lines = file.readlines()
            # Skriva ut första fem raderna
            for line in lines[:5]:
                print(line.strip()) # Skriva ut varje rad



    except FileNotFoundError:
        print("the file Numbers.txt was not found")


file_Head_Display()

