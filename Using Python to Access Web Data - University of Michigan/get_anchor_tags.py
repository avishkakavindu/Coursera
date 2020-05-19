import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# --- ignore ssl certificate ---
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read() #read returns entire webpage -UTF-8
print(html)
soup = bs(html, 'html.parser')  #returns soup object(cleaned html)

#retrieve all <a> tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
