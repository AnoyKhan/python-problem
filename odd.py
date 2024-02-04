print("Please input your word:")
word = input()
word = word.casefold()
reversed_word = word[::-1]
if word == reversed == reversed_word:
    print("Great! It is a pallindrome.")
else:
    print("LOL! It is not pallindrome.")




x = int(input("Enter the number:"))
if x % 2 == 0 or x % 3 == 0:
    print("Division by 2 and 3")
elif x % 3 == 0:
    print("Division by 3 but not by 2")
else:
    print("Not division by either 2 or 3")