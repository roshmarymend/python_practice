text = input("Enter a string: ")
word = input("Enter a word to count its frequency: ")
words = text.split()
print("The frequency of", word, "in the string is:", words.count(word))