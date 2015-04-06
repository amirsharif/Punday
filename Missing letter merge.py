import csv

rawfile = open('/Users/amirsharif/Punday/output.csv')
rawread = rawfile.readlines()
wordslist = []
for line in rawread:
    lineclean = line.split(',')
    for word in lineclean:
        wordlowercase = word.lower()
        wordslist.append(wordlowercase)

print len(wordslist)
        
rawfile_dfv = open('/Users/amirsharif/Punday/output-dfv.csv')
rawread_dfv = rawfile_dfv.readlines()
wordslist_dfv = []
for line in rawread_dfv:
    lineclean_dfv = line.split(',')
    for word in lineclean_dfv:
        wordlowercase_dfv = word.lower()
        wordslist_dfv.append(wordlowercase_dfv)

print len(wordslist_dfv)

newwords = []

for word in wordslist_dfv:
    print wordslist_dfv.index(word)
    if word not in wordslist:
        print word
        wordslist.append(word)
        newwords.append(word)

print newwords
print len(newwords)
print len(wordslist)

fileaway = open('/Users/amirsharif/Punday/output-test.txt','w')
wr = csv.writer(fileaway)
wr.writerow(wordslist)