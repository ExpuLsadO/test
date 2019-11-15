from urllib import request, parse
import sys

url = "https://google.com/search?"
value = {'q': 'kavo'}
try:
    myd = parse.urlencode(value)
    print(myd)
    url+=myd
    req  = request.Request(url)
    answ = request.urlopen(req)
    answ = answ.readables
    for line in answ:
        print(line)
except Exception:
    print("опа")
    print(sys.exc_info()[1])