#problem: http://www.pythonchallenge.com/pc/def/hockey.html
#problem: http://www.pythonchallenge.com/pc/def/oxygen.html

import requests
import re
from io import BytesIO
from PIL import Image


img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

print(img.width)
print(img.height)
print(img.getpixel((0,0)))

row = [img.getpixel((x, img.height/2)) for x in range(img.width)]
print(row)

row = row[::7]
print(row)

ords = [ r for r,g,b,a in row if r==g==b]
tmp = "".join(map(chr, ords))
print(tmp)

nums= re.findall("\d+", "".join(map(chr, ords)))
print(nums)

print("".join(map(chr, map(int, nums))))

#solve: http://www.pythonchallenge.com/pc/def/integrity.html
