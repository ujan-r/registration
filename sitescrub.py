import requests
from bs4 import BeautifulSoup



URLs = []
with open('hyperlinks.txt') as file:
    for line in file:
        URLs.append('https://catalog.drake.edu' + line.strip())
#print(URLs)  #Debug
#print((requests.get(URLs[0])).text)

majors = []
for URL in URLs:
    textAlpha = URL.split('areas/')
    splitList = textAlpha[1].split('/')
    text = splitList[0].upper()
    majors.append(text)
    #print(text)         #Debug
#print(majors)          #Debug

htmlDataList = []
for URL in URLs:
    page = requests.get(URL)
    htmlDataList.append(page.text)
#print(htmlDataList)        #Debug



majorSpecificClassList = []
for htmlText in htmlDataList:
    soup = BeautifulSoup(htmlText, 'html.parser')
    tdElements = soup.find_all('td', style=True)
    #print(tdElements)           #Debug
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9']
    classList = [item for td in tdElements if ' ' in td.get_text(strip=True) for item in td.get_text(strip=True).split(', or')] #Original
    #print(classList)            #Debug
    for element in classList:
        safe = False
        for i in nums:
            #print(element, i)  #Debug
            if i in element:
                safe = True
        if len(element) >= 69:
            safe = False
        if not safe:
            classList.remove(element)
        if safe:
            newClass = element.replace('\xa0', ' ').replace('*','').replace('**','')
            index = classList.index(element)
            classList[index]=newClass
            #print(element + " removed")    #Debug
    print(classList)     #Debug

    majorSpecificClassList.append(classList)
    #print(majorSpecificClassList)        #Debug
    
    

    classDictionary = {key: value for key, value in zip(majors, majorSpecificClassList)}
    ''' Debug
    print("Keys:", list(classDictionary.keys()))
    print("Values:", list(classDictionary.values()))
    print(classDictionary)
    '''
    print(classDictionary)


    


#print(htmlDataList)     #Debug
#print(htmlDataList[0])  #Debug