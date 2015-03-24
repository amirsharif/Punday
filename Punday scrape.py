import urllib

url = 'http://mondaypunday.com/'

def getLatestPun():
    site = urllib.urlopen(url)
    content = site.read()
    site.close()
    maxnumber = int(content[content.index('<title>')+7:content.index('<title>')+10])
    return maxnumber

def alysabtu(maxNumber, firstPun):
    urlset = []
    for i in xrange(firstPun,maxNumber+1):
        urlset.append(url+str(i))
    return urlset

def getAllThePuns(maxNumber,firstPun=0):
    if firstPun == 0: firstPun=maxNumber
     
    imageset = []
    for page in alysabtu(maxNumber, firstPun):
        sock = urllib.urlopen(page)
        content = sock.read()
        sock.close()
        snipstart = content.index('post type-post status-publish format-standard hentry category-uncategorized')
        snippet = content[snipstart:snipstart+600]
        startmarker = snippet.index('src')
        start = startmarker+5   
        try: jpg = snippet.index('jpg')
        except ValueError: jpg=5000
        try: png = snippet.index('png')
        except ValueError: png=5000
        try: jpeg = snippet.index('jpeg')+1
        except ValueError: jpeg=5000
        indices = min([jpg,png,jpeg])    
        end = indices+3
        imagescrape = snippet[start:end]
        imageset.append(imagescrape)
    return imageset

import time
previousClue = ""

def TimedPinger(secondsBtwnChecks, previous=previousClue):
    while True:
        print "Polling..."
        newClue = getAllThePuns(getLatestPun())
        if newClue != previous:
            print newClue
        print "Sleeping..."
        previous = newClue

        time.sleep(secondsBtwnChecks)


print getAllThePuns(getLatestPun(),1)