#to print fibinocci series to n
# algorithm : get the n as input 
#in the for loop add i to the count which is intially 0
#input : n
#output : 0 1 1 2 3 5 .........

n = int(input("enter n:"))
a = 0
b= 1

for i in range(n):
   print(a)
   a,b=b,a+b
