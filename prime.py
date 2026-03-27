#to find whether the given number is prime or not
#input : number
#output : prime or not
#logic : use the mod function to get reminder till half of the number given
#algorithm : get the input number
#if less than 1 print not prime
#in for loop in the range 2 to root of number 
# evaluate the mod function 

a = int(input("enter a number:"))
if a <=1:
    print("not prime")
for i in range(2,int(a**0.5)):
    n = a % i
    if n ==0:
        print("not prime")
    else:
        print("prime")