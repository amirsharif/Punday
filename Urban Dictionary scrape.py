from selenium import webdriver
import csv
import unittest, re

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.urbandictionary.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        totallist = []
        alphabet = 'dfv' #string.ascii_lowercase
        for letter in alphabet:                
            driver = self.driver
            driver.get(self.base_url + "/browse.php?word=" +letter+'a')
            userinput = 'yes'
            while userinput=='yes':        
                for i in range(1,300):
        	       self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                userinput = raw_input("Type yes to continue scraping this letter:")
            html_source = driver.page_source
            data = html_source.encode('utf-8')
        
            findWords = re.compile('<a href="/define.*>(.*)</a>')
            print "NOW FOR THE WORDS!"
            words = re.findall(findWords,data)
            totallist.append(words)
            print totallist
        print totallist
        fileaway = open('/Users/amirsharif/Punday/output-dfv.csv','wb')
        wr = csv.writer(fileaway)
        for word in totallist:
            wr.writerow(word)

if __name__ == "__main__":
    unittest.main()