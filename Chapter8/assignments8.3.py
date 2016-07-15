fhand = open('mbox-short.txt')

for line in fhand :
    words = line.split()
    if len(words) != 0 and words[0] == 'From' :
        try :
            print words[2]
        except :
            print 'Index Error - out of boundary'
            continue
    else :
        continue