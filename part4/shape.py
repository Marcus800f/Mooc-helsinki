def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def shape(size,character,size_two,character_two):
    size_table=[size,size_two]
    character_table=[character,character_two]
    for j in range(0,2):
        for i in range(1,size_table[j]+1):
            number_character =[i,size]
            line(number_character[j], character_table[j])
        
if __name__ == "__main__":
    shape(5, "X", 3, "*") 