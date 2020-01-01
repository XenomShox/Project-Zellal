import urllib
from urllib.request import urlopen

try:
    website = urlopen("http://127.0.0.1:3000/vidal/vidal-Sommaires-Substances-A.htm")
except urllib.error.HTTPError as e:
    print("shit")
    try:
        website = urlopen("http://127.0.0.1:3000/www.vidal.com/vidal-Sommaires-Substances-A.htm")
    except urllib.error.HTTPError as e:
        print("shit")
        website = urlopen("http://127.0.0.1:3000/vidal-Sommaires-Substances-A.htm")