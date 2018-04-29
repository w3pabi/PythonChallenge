# problem : http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
content = urlopen(uri % num).read().decode()
pattern = re.compile("and the next nothing is (\d+)")


while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)

num = str(16022/2) # "Yes Divide by two and keep going" message reset num to 16044/2

while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)

# solve : http://www.pythonchallenge.com/pc/def/peak.html