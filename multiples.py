#to print numbers from 1 to 50 and print pause for every 5's multiple and breal for every 10's multiple
for i in range (1,20):
    if i%10 == 0 :
        print("pause")
    elif i%5 == 0 :
        print("break")
    else:
        print(i)