#to find frequency of characterin a string
string = input("enter the string:")
char = input ("enter the character to find frequency of: ")
freq_char = 0
for i in string:
    if i == char:
        freq_char += 1
    
print ("frequency of character",char,"string",string,"is",freq_char)
