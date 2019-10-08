from urllib.request import urlopen
import re


def task_1():
    html = urlopen("https://links.datapor.no/")
    content = html.read()
    print(content)


def task_2():
    r = urlopen("https://links.datapor.no/")
    http = re.findall('^http?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
    return http
    https = re.findall('^https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
    return https


if __name__ == "__main__":
    task_1()
    task_2()
