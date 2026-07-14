def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def triangle(size):
    for i in range(0,size+1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
