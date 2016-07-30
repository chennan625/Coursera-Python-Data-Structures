'''
Write a program to read through a mail log, and build a histogram using a
dictionary to count how many messages have come from each email address and
print the dictionary.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue

    try:
        emails[words[1]] = emails.get(words[1],0) + 1
    except:
        print 'Index Error - out of boundary'
        continue


print emails