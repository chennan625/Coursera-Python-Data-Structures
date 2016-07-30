'''
This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e. the whole
e-mail address). At the end of the program print out the contents of your
dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

domains = dict()

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' or len(words) < 1: continue

    pos = words[1].find('@')
    domains[words[1][pos:]] = domains.get(words[1][pos:],0) + 1
    

print domains