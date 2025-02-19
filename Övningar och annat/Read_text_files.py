
## Commands
"""
Read Only - ('r') Open textfile
write Only ('w') - open file for´writing
Append Only ('a') - open file for write /create if does not exist.

Write and read('r+')
Read and Write(w+')
Append and read('a+')



"""
counter = 0
#airplanes = open('Mylist','w') # Write,write over
airplanes = open('Mylist','a') #Append, adds another
airplanes.write("Piper Arrow II\n") # override what ever is in Mylist


for planes in range(3):
    a = (input("Enter an airplane: "))
    airplanes.write(f"{counter}. {a}\n")
    counter +=1

airplanes.close()

### Other
"""
### READ
file= open(example.text, 'r'),
line = file.readline() - Read a single line
lines = file.readlines() - Read all lines

### WRITE TO FILES 
1:
with open(example.txt, 'w') as file: 
file.write("This is a new line of text ")
2:
with open('example.text', 'a') as file: 
file.write("appending a new line.\n")

### Loop THROUGH FILES
with open('example.txt', 'r') as file: 
    for line in file:
        print(line.stip())
        
### COPY BETWEEN FILES
with open("example.txt", "r") as source, open('destination.text', 'r') as destination: 
    for line in source:
        destination.write(line) 

### Check if file Exist
import os 


if os.path.exists(example.txt):
    with.open('file.txt','r') as file: 
        print(file.read())
else:
    print("File not found")
"""
#