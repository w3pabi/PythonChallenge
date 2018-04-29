# problem : http://www.pythonchallenge.com/pc/def/map.html

import string
raw= """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""
print(ord('m')-ord('k'))
print(ord('q')-ord('o'))
print(ord('g')-ord('e'))
print(ord('a'))
print(ord('z'))

# define
def trans(raw) :
    result = ""
    for c in raw:
        if c>='a' and c<='z':
            result += chr(((ord(c)+2)-ord('a'))%26 + ord('a'))
        else:
            result +=c
    print(result)

# print hint
print(trans(raw))

# print url "map.html" trans
print(trans('map'))


# solve : http://www.pythonchallenge.com/pc/def/ocr.html
