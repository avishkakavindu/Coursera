from urllib.request import urlopen
import json
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
print('Retrieving ', url)

data = urlopen(url, context=ctx).read()
print('Retrieved: {} characters'.format(len(data)))

info = json.loads(data)

comments = info['comments']
print('Count: {}'.format(len(comments)))
sm = sum([comment['count'] for comment in comments ])
print('Sum: {}'.format(sm))
