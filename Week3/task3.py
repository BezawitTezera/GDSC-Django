word = input("Please enter the word to check: ")
if word[::]== word[::-1]:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} isn't a palindrome, because {''.join(word[::-1])} isn't the same as {word}.")
