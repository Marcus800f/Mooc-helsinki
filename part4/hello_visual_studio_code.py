editor= ""
while editor.lower() != "visual studio code":
    editor= input("Editor:")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
    elif editor.lower() ==  "notepad" or editor.lower()== "word":
        print("awful")
    else:
        print("not good")
