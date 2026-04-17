#read a .txt file and print count,sum and average
#algorithm
#open the file in read mode
#remove space,tabs and blanks
#assign it to a list 
#use inbuilt functions to print the values

with open("input.txt","r")as file:
    numbers = [int(line.strip()) for line in file if line.strip()]
    print("count:" ,len(numbers))
    print("sum:" ,sum(numbers))
    average = sum(numbers)/len(numbers)
    print("average" ,average)

