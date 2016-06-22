'''
Write a while loop that starts at the last character in the string and works its way
backwards to the first character in the string, printing each letter on a separate line, except backwards.
'''


text = raw_input("Enter a word:")
count = 0

while count < len(text):
	count = count + 1
	print text[len(text)-count]
	
