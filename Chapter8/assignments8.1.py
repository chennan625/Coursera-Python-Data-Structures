'''
write a function called 'chop' that takes a list and modifies it, removing the first and last elements, 
and returns 'None'.
write a function called 'middle' that takes a list and returns a new list that contains all but the 
first and last elements.
'''
lstChop = [1, 2, 3, 4, 5]
lstMiddle = [1, 2, 3, 4, 5]

def chop(lst):
	del lst[0]
	del lst[-1]

def middle(lst):
	return lst[1:-1]


if len(lstChop) <= 1 or len(lstMiddle) <= 1: 
	print 'Cannot delete two elements, exit program'
	exit()

print 'Original list:', lstChop
print 'Calling chop() function, it returns:', chop(lstChop)
print 'Modified list:', lstChop
print '###############'
print 'Original list:', lstMiddle
print 'Calling middle() function, it returns:', middle(lstMiddle)