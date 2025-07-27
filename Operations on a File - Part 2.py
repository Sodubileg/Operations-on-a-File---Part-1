file = open('codingal.txt','r')
print("reading first line...")
print(file.readline())
file.close()

#read first three lines of file
file = open('codingal.txt','r')
print("reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('codingal.txt','r')
print("looping through the lines...")
for line in file:
    print(line)
file.close()