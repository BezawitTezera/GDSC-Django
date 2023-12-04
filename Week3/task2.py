character = input("Pleaase enter the patter to be printed: ")
if character.lower() in ["a","e","i","o","u"]:
    print("Vowels aren't allowed in the input.")
elif len(character) != 1:
    print("The length of the character should be 1.")
else:
    for i in range(1,8,2):
        print(character * i)
