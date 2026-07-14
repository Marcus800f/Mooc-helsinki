def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def square_of_hashes(size):
    for i in range(0,size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
