from bs4 import BeautifulSoup
import urllib.request
import os
#imported libraries
url="https://en.wikipedia.org/wiki/Deep_learning"


#parsing the source code
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")


#Printing the page title
print(soup.title.string)


#finding the links in the page with 'a' tag and return the attribute 'href'
for link in soup.find_all('a'):
    print(link.get('href'))
