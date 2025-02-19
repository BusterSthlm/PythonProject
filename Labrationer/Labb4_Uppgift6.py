# UPG 6

"""
Assume a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that calculates the average of all the numbers stored in the
file.

"""
from pyexpat.errors import messages


# Variables
def calculation():
    total_summa = 0  # Initialize sum
    count = 0  # Initialize count of numbers

    # Open the file
    try:
        with open('numbers.txt', 'r', encoding='utf-8') as file:
            print(file.read())  # Example to confirm the file can be read

            # Read each line
            file.seek(0)  # Reset file pointer after the first read

            for line in file:
                stripped_line = line.strip()  # Remove spaces
                print(f"Processing line: '{stripped_line}'")  # Debug print to show lines being processed
                if stripped_line:  # Ensure line is not empty
                    try:
                        number = int(stripped_line)  # Convert to integer
                        total_summa += number  # Add to sum
                        count += 1  # Increment count
                        print(f"Total sum so far: {total_summa}, count: {count}")
                    except ValueError:
                        print(f"Skipping invalid line: {stripped_line}")

        # Calculate and display the result
        if count > 0:
            print(f"Sum of all your numbers is: {total_summa}")
            print(f"Average of all numbers is: {total_summa / count}")
        else:
            print("Tyvärr, det saknas rader i den här filen")  # If no valid numbers were found

    except FileNotFoundError:
        print("File 'numbers.txt' not found.")


# Call the function
calculation()
