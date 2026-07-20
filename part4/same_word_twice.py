word=[]

while True:
   word_check = input("Word: ")
   if word_check in word:
        break
   word.append(word_check)
print(f"You typed in {len(word)} different words")