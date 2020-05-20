from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

#ignore SSL certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
print('Retrieving ', url)

data = urlopen(url, context=ctx).read()
print ("Retrieved: {} characters".format(len(data)))
tree = ET.fromstring(data)
lst = tree.findall('.//count')

sm = 0
for item in lst:
    sm += int(item.text)

print('Count: {}\nSum: {}'.format(len(lst), sm))
