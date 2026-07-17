my_lis =[]
i = 0
while True:
    print(f"The list is now {my_lisy}")
    anwser = input("a(d)d, (r)emove or e(x)it:")
    if anwser == "x":
        print("Bye!")
        break
    if anwser == "d":
        my_lisy.append(i+1)
        i+=1
    elif anwser == "r":
        my_list.pop(i-1)
        i-=1