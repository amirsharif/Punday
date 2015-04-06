from mechanize import *

url = 'http://www.mondaypunday.com'
guess = 'keeping up with the jones'

br = Browser()
br.open(url)


br.select_form(nr=0)
br['answer'] = 'poop'
resp = br.submit()

import datetime

print 'WAHOO' , datetime.datetime.now()

html = resp.read()

print 'YOOHOO' , datetime.datetime.now()

try: 
    html.index('Correct!')
    print 'yay!!!!!!!!!!!!!!!'
    print 'Zumba' , datetime.datetime.now()
except:
    print 'GROAHOO' , datetime.datetime.now()
    print 'nice try'
    br.select_form(nr=0)
    print 'NAONO' , datetime.datetime.now()
    br['answer'] = guess
    print 'TOOTOOTOO' , datetime.datetime.now()
    resp = br.submit()
    print 'WAHOO' , datetime.datetime.now()

    html = resp.read()

    print 'YOOHOO' , datetime.datetime.now()
    try: 
        html.index('Correct!')
        print 'yay!!!!!!!!!!!!!!!'
        print 'Zumba' , datetime.datetime.now()
    except:
        print 'oops'
        
        
        
