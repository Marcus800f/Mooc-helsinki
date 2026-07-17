def first_word(sentence):
    for i in range(len(sentence)):
        if sentence[i]== " ":
            return sentence[0:i]
    return sentence

def second_word(sentence):
    count = len(first_word(sentence))
    sentence = sentence[count+1:]
    return first_word(sentence)

def last_word(sentence):
    for i in range(len(sentence)):
        if sentence[i]== " ":
            sentence_final = sentence[i+1:]
    return sentence_final



if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    