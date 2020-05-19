from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)                      #gets entire tag
    print('URL:', tag.get('href', None))    #gets value belongs to attribute 'href'
    print('Contents:', tag.contents[0])     #gets content between the tags
    print('Attrs:', tag.attrs)              #gets attributes of the tags and there values returns a dictionary
