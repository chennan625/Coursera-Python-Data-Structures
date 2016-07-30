'''
Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation or anything other than the letters a-z. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies.
'''
import string

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hist = dict()

for line in handle:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    
    if len(words) == 0 : continue
    
    for word in words: 
        for letter in word:
            if letter.isalpha():
                hist[letter] = hist.get(hist[letter],0) + 1

print sorted(hist.items())