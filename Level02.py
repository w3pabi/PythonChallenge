#problem : http://www.pythonchallenge.com/pc/def/ocr.html

import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
raw = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

result =""
for i in raw:
    if i.isalpha():
        result+=i

print(result)

#sovle : http://www.pythonchallenge.com/pc/def/equality.html