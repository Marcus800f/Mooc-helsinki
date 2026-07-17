list_original= [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Index : "))
        if index == -1:
            break
        
        new_value = input("New value: ")
        list_original[index] = int(new_value)
        print(list_original)
    except IndexError:
        print()