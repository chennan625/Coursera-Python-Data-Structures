
'''
Revise a previous program as follows: Read and parse the "From" lines and
pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read print the person with the most commits by
creating a list of (count, email) tuples from the dictionary and then sorting
the list in reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

name = raw_input("Enter file:")
handle = open(name)

emails = dict()

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' or len(words) < 1: continue

    emails[words[1]] = emails.get(words[1],0) + 1

result = sorted([(v,k) for k,v in emails.items()],reverse = True)[0]

print result[1], result[0]



