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
    for link in linksHttps:
        counterHttps+=1
    print("Number of http links:",counterHttp)
    print("Number of https links:",counterHttps)



def task_3():
    test


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
