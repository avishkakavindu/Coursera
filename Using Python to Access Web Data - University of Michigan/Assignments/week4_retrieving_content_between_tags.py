from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl

#ignore SSl cetificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
html = urlopen(url, context=ctx).read()
soup = bs(html, "html.parser")

#retrieve data from <span> tags
tags = soup('span')
sm = 0

for tag in tags:
    sm += int(tag.contents[0])
print('sum: ', sm)
