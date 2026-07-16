
def same_chars(string_taken, first_number, second_number):
    try:
        return string_taken[first_number] == string_taken[second_number]
    except IndexError:
        return False
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))