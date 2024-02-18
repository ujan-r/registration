from bs4 import BeautifulSoup
import urllib.request

enteringLinks = True
links = []
while enteringLinks:
    link = input("Please enter in the link for major lists of the college, or enter 'D' to run the file: ")
    if link.upper() == 'D':
        enteringLinks = False
    else:
        links.append(link)
hyperlinkExport = []
for link in links:
    html_page = urllib.request.urlopen(link)
    soup = BeautifulSoup(html_page, "html.parser")
    for link in soup.findAll('a'):
        hyperlinkExport.append(link.get('href'))


# for component in hyperlinkExport:
#     if component == None:
#         hyperlinkExport.remove(component)
#     elif 'areas/' not in component:
#         hyperlinkExport.remove(component)
hyperlinkExport = [component for component in hyperlinkExport if component is not None and 'areas/' in component]
hyperlinkExport = list(set(hyperlinkExport))
#print(hyperlinkExport)         #Debug

file = open('hyperlinks.txt','w')
for item in hyperlinkExport:
    file.write(item + "\n")
file.close()