
# Kapittel 6
# Exmplaination
# .strip(): Removes from both ends.
# .rstrip(): Removes only from the right (end of the string).
# Use + for multiple strings. Input functions take only one string. need + to add multiple stroing together.

#Check for empty files
#1. while line !='': typically indicate the end of the file (EOF), not a blank line in the middle of the file
# 2. Use \n if you want to check for empty lines inside a file.


# 1. Content of file

def main():
    #open file name
    outfile = open('file.text','w')
    outfile.write('John Lock\n)

    file.close()

# 2. Read from file
    outfile = open('file.text','r')
    # Read three lines from the file.

    line1 = infile.readline()
# 3. Read from speciefic placment in file
    file.seek(10)

#.4 Write and reading numerical data
    num1 = int(input('Enter number: '))

    #write number to file
    file.write(str(num1) +\n)

#.5 Convert string to int or float
    infile = open('number.text', 'r')
    string_input = infile.readline()
    float_input = infile.readline()

    value = int(string_input)
    value = float(float_input)

# 6. Using  loops for Processing files
    def main():
        #Get number of days
        num_days = int(input("for how many days do you have sales= ")))

    #open new file named .sales.txt
    sales_file = open('sales.txt', 'w')

    ##get amount of sales for each day and write it to the file
    for count in range(1, num_days +1):
        #get sales for the day
        sales = float(input('Enter the sales for the day:' +str(count) + ':'))
        sales = float(input('Enter the sales for day #' +str(count) + ': '))

# Read a file and detect the end of the file.
    #PSUEDO CODE
        # 1. Open the file
        # 2. Use Readline() to read the first line of the file # AS TEST line to decide weather we want to continue.

        # 3. while the value return from readline is not and empty str:
        # 4. Process the item that was just read from the file
        # 5. Use readline to read next line from the file.
        # 6. Close the file.

    def main():
        sales_file = open('file.txt','r')
        line = sales_file.readline()

        #Need to test the file for empty lines
        while line!= ' ':
            #convert to float
            amount = float(line)

            #format and display the amount
            print(format(amount, '.2f'))

            #Read next line
            line = sales_file.readline()

# A program that allows him to enter the running time (in seconds) of each short video in a
# project. The running times are saved to a file.
# 2. A program that reads the contents of the file, displays the running times, and then displays the
# total running time of all the segments.

# 1. Get number of videos in the projects
num_video = int(input("How many videos?"))
# 2. Open an ouput file
Video_file = open('video_file.txt','w')
# 3. for each video in the the project:
run_time = float(input("Enter runt tim" + '.2f'))
for count in range(1, num_video +1): # start at 1 an up to input, +1 to include
    run_time = float(input('Video #' + str(count) + ': '))
    video_file.write(str(run_time) + '\n')
    #get the run time

    # Write the running time to the file.
num_video.write( video file + run_time)

# 5. CLose the file.
num_video.close()

#