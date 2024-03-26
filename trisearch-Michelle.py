#Trisearch Project - Michelle's Work
import requests 
from bs4 import BeautifulSoup

def reformat(prop, input):
    temp=str(input)
    if prop==3:
        return temp[51:-27]
    elif prop==2:
        return temp[28:-6]
    else:
        new=temp[74:-31]
        if new[0:1]==">":
            return new[1:]
        return new

URL = "https://stockanalysis.com/stocks/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")
#print(results.prettify())
comp_elements = results.find_all("tr", class_="svelte-1jtwn20")
for comp_element in comp_elements:
    #print(job_element, end="\n"*2)
    #print(comp_element, end="\n"*2)
    #comp_ticker = comp_element.find("a", href="/stocks/")
    #print(comp_ticker)
    # print(comp_ticker.text)
    comp_props = comp_element.find_all("td", class_="svelte-1jtwn20")
    #print(comp_props.to_list())
    c_props=list(comp_props)
    comp_ticker=c_props[0:1]
    comp_name=c_props[1:2]
    comp_cap=c_props[3:4]
    print(reformat(1,comp_ticker), reformat(2, comp_name), reformat(3, comp_cap))
    # c_cap=str(comp_cap)
    # cap=c_cap[51:-27]
    # print(comp_ticker)
    # print(comp_name)





#print(page.text)
# import re
# import urllib.request as ur
# # r=requests.get("https://www.builtinboston.com/jobs")
# # print(r)
# # print(r.content)


# #print('What would you like to look up?')
# text = "catalant"
# # search_string = text.split(' ')
# # search_string = '+'.join(search_string)
# search_string=text
# # you can change www.bing.com to any search engine except google.
# googlesearch = 'https://en.wikipedia.org/wiki/' + search_string
# print(googlesearch)
# source = ur.urlopen(googlesearch)
# source = source.read()
# source = str(source)
# #print(source)
# output = re.findall(r'''(?:http://|www.)[^"]+''', source)
# #output = re.findall(source)
# for i in range(len(output)):
#     print(output[i])

