#to find factorial of a given number   
#input : a number
#output : factorial
#logic: n*(n-1)*(n-2)*........*1

a = int(input("enter the number:"))
fact = 1
for i in range(1,a+1):
    fact= fact * i
print("factorial:",fact)