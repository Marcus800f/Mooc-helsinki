def line(size):
    print("*"*size)


def space(iteration):
    print(" "*iteration,end ="")
    
def spruce(size):
    print("a spruce!")
    for i in range(size):
        space(size - i - 1)
        line(2*i + 1)
    space(size - 1)
    line(1)
        
            


if __name__ == "__main__":
    spruce(5)