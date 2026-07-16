def greatest_number(a, b, c):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    return greatest


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)