# Copy here code of line function from previous exercise
def line(number, character):
    for i in range (0,number):
        if character== "":
            print("*"*10)
        print(character[0]*10)

def box_of_hashes(height):
    line(height, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
