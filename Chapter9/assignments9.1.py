'''
Write a program that reads the words in words.txt and stores them as keys in
a dictionary. It doesn't matter what the values are. Then you can use the in
operator as a fast way to check whether a string is in the dictionary.
'''
test_word = raw_input("Enter a word:")
handle = open("words.txt")

words_dict = dict()

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
   
    for word in words:
    	words_dict[word] = None


print test_word in words_dict  
