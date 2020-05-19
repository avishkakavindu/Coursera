from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl

#ignore SSl cetificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
position = 18
count = 0
while True:

    html = urlopen(url, context=ctx).read()
    soup = bs(html, "html.parser")

    #retrieve data from <span> tags
    tags = soup('a')
    url = tags[position-1].get('href', None)    # renew the url
    count += 1
    if count >= 7:
        print('Last name in sequence: ', tags[position-1].contents[0])
        break
