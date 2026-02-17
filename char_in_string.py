#program to find the number of times a character appears in a string
string = input("enter a string:")
char = input("enter a character:")
count =0
for i in string:
    if i==char:
        count = count+1
print("the character",char,"appears",count,"times in the string",string)