from urllib.request import urlopen
import re


def task_1():

    html = urlopen("https://links.datapor.no/")
    content = html.read()
    print(content)

def task_2():
    


if __name__ == "__main__":
    task_1()
    task_2()
