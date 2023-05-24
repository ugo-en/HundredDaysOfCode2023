word = input("Enter a word: ").strip().lower()

reverse_word = word[::-1]

if word == reverse_word:
    print("Statement is a palindrome")
else:
    print("This statement is NOT a palindrome!")

    
