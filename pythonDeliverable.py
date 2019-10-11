import requests
import re
from tld import get_tld
from urlextract import URLExtract
import tldextract

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
    r = requests.get("https://links.datapor.no/")
    result = re.findall(r"\w+://\w+\.\w+\.\w+/?[\w\.\?=#]*", r.text)
    urls = result
    for url in urls:
        info = get_tld(url, as_object=True)
        print("Suffix: ", info.suffix)

def task_4():
    r = requests.get("https://links.datapor.no/")
    result = re.findall(r"\w+://\w+\.\w+\.\w+/?[\w\.\?=#]*", r.text)
    urls = result
    for url in urls:
        info = get_tld(url, as_object=True)
        print("Suffix: ", info.domain)


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
