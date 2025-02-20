# UPG 6 - Average numbers

"""
Assume a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that calculates the average of all the numbers stored in the
file.

"""

# Variables
def calculation():
    total_summa = 0  # Initialize sum
    count = 0  # Initialize count of numbers

    # Open the file
    try:
        with open('numbers.txt', 'r', encoding='utf-8') as file:

            for line in file:
                stripped_line = line.strip()  # Strip tar birt onödiga mellanrum

                if stripped_line:  # kollar att filen inte är tom
                    try:
                        number = int(stripped_line)  # Convert to integer
                        total_summa += number  # Lägger
                        count += 1  # Plussar på det nya värdet
                    except ValueError:
                        print(f"struntade i ogilltiga rader: {stripped_line}")

            # Räknar och skriver ut total summan delat på antalet
            if count > 0:
                print(f"summan av alla nummer är: {total_summa}")
                print(f"genomsnittet är: {total_summa / count}")
            else:
                print("Tyvärr, det saknas rader i den här filen")

    except FileNotFoundError:
        print("Filen 'numbers.txt' hittades inte.")


# kallar funktionen
if __name__ == '__main__':
    calculation()

