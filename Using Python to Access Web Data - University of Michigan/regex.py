import re

file = open('sample1.txt')

sm = 0

for line in file:
    sm += sum(map(int, re.findall('[0-9]+', line)))
print(sm)
