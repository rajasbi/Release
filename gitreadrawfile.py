  1 import requests
  2 from os import getcwd
  3 import requests.packages.urllib3
  4 requests.packages.urllib3.disable_warnings()
  5 
  6 url = "https://raw.githubusercontent.com/rajasbi/Release/master/git1.py"
  7 directory = getcwd()
  8 filename = 'somefile.txt'
  9 r = requests.get(url)
 10 
 11 f = open(filename,'w')
 12 f.write(r.content)
