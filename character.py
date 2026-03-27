# Given a string, count the frequency of each character and print them in alphabetical order

a = input("enter the string:")  # input stored in s
frequency = {}  # dictionary that store the frequency
for ch in a:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

    # sorting
    for ch in sorted(frequency):
        print(f'{ch}:{frequency[ch]}')
