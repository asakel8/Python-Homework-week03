word = input("Enter a word: ")

#reverses the word
reverse = word[::-1]

if word == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
