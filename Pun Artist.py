from mechanize import *
import datetime

class Answers(object):
    def __init__(self):
        self.answers = []
        self.clue = raw_input('Please enter your clue here:')
        print datetime.datetime.now()
    
    def getAnswers(self):
        rawfile = open('C:/Users/asharif/Documents/GitHub/Punday/output-final.txt')
        rawread = rawfile.readlines()
        wordslist = []
        for line in rawread:
            lineclean = line.split(',')
            for word in lineclean:
                wordlowercase = word.lower()
                wordslist.append(wordlowercase)
        for word in wordslist:
            if self.clue in word:
                self.answers.append(word)
        return self.answers
                
    def tryAnswers(self):
        self.url = 'http://www.mondaypunday.com/'
        self.guesses = self.getAnswers()
        br = Browser()
        br.open(self.url)
        for guess in self.guesses:
            br.select_form(nr=0)
            print guess
            br['answer'] = guess
            resp = br.submit()
            html = resp.read()
            try: 
                html.index('Correct!')
                print guess
                print 'woohoo'
                print datetime.datetime.now()
                return guess
                break
            except:
                pass

tryMe = Answers()
tryMe.tryAnswers()