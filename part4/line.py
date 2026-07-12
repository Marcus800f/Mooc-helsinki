def line(number, character):
    if character== "":
        print("*"*number)
    print(character[0]*number)
if __name__ == "__main__":
    line(3, "")