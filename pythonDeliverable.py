import requests
import re

def task_1():
    r = requests.get("https://links.datapor.no/")
    print(r.text)

def task_2():
    counterHttp = 0
    counterHttps = 0
    r = requests.get("https://links.datapor.no/")
    linksHttp = re.findall('http://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
    linksHttps = re.findall('https://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
    for link in linksHttp:
        counterHttp+=1
        trash, link2 = link.split("//")
        print(link2)
    for link in linksHttps:
        counterHttps+=1
        print(link)
    print("Number of http links:",counterHttp)
    print("Number of https links:",counterHttps)


def task_3():
    r = requests.get("https://links.datapor.no/")
    pattern = '/(?:[a-zA-Z]*\.)+([a-zA-Z]+)(?:\/.*)?'
    tlds = re.findall(pattern, r.text)
    print(tlds)

def task_4():
    r = requests.get("https://links.datapor.no/")
    linksHttp = re.findall('http://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
    linksHttps = re.findall('https://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
    linkList = []
    for link in linksHttp:
        if not link in linkList:
            linkList.append(link)
            trash, link2 = link.split("//")
            print(link2)
    for link in linksHttps:
        if not link in linkList:
            linkList.append(link)
            trash, link2 = link.split("//")
            print(link2)

def task_5():
    r = requests.get("https://links.datapor.no/")
    tags = re.findall(r'<[^>][a-z.A-Z.0-9]*>', r.text)
    tagsList = []
    for tag in tags:
        if not tag in tagsList:
            tagsList.append(tag)
            print(tag)

def task_6():
    r = requests.get("https://links.datapor.no/")
    linksHttp = re.findall('http://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
    linksHttps = re.findall('https://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
    linkList = []
    for link in linksHttp:
        if not link in linkList:
            linkList.append(link)
    for link in linksHttps:
        if not link in linkList:
            linkList.append(link)
    for link in linkList:
        print(link) #bare for å vise alle linkene i linklist
        l = requests.get(link)
        linkTittel = re.findall('<title.*?>(.+?)</title>', l.text)
        print(linkTittel)


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
