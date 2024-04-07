#Trisearch Project - Michelle's Work
import requests 
import re
import urllib.request as ur
# r=requests.get("https://www.builtinboston.com/jobs")
# print(r)
# print(r.content)


#print('What would you like to look up?')
text = "catalant"
# search_string = text.split(' ')
# search_string = '+'.join(search_string)
search_string=text
# you can change www.bing.com to any search engine except google.
googlesearch = 'https://en.wikipedia.org/wiki/' + search_string
print(googlesearch)
source = ur.urlopen(googlesearch)
source = source.read()
source = str(source)
#print(source)
output = re.findall(r'''(?:http://|www.)[^"]+''', source)
#output = re.findall(source)
for i in range(len(output)):
    print(output[i])

