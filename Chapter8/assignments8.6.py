'''
Rewrite the program that prompts the user for a list of numbers and prints out the 
maximum and minimum of the numbers at the end when the user enters "done". 
Write the program to store the numbers the user enters in a list and use the max() and min() 
functions to compute the maximum and minimum numbers after the loop completes.
'''
numlist = list()
while(True):
	inp = raw_input('Enter a number:')
	if inp == 'done' : break
	try:
		value = float(inp)
	except:
		print 'Error: please enter a numeric value'
		continue
	numlist.append(value)

if len(numlist) == 0 :
	print 'The list is empty.'
else:
	print 'Maximum:', max(numlist)
	print 'Mnimum:', min(numlist)