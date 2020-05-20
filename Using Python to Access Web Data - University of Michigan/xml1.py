import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone>+4543651356</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
