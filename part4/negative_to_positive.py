number = int(input("Please type in a positive integer: "))
for i in range (-number, number+1):
    if i == 0:
        print(end ="")
    else:
        print(i)