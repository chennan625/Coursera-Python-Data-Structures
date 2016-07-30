'''
Write a program that categorizes each mail message by which day of the week
the commit was done. To do this look for lines which start with "From", then
look for the third word and then keep a running count of each of the days of
the week. At the end of the program print out the contents of your dictionary
(order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

days = dict()

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue

    try:
        days[words[2] = days.get(words[2],0) + 1
    except:
        print 'Index Error - out of boundary'
        continue

print days