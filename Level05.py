# problem : http://www.pythonchallenge.com/pc/def/peak.html

from urllib.request import urlopen
import pickle


raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(raw)

for line in data:
    print("".join([k*v for k, v in line ]))

# solve: http://www.pythonchallenge.com/pc/def/channel.html
