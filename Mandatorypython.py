import urllib3
import json


def task_1():
    http = urllib3.PoolManager()
    r = http.request(
        'GET',
        'https://links.datapor.no',
        headers={
            'X-Something': 'value'
        })
    json.loads(r.data.decode('utf-8'))['headers']
    {'X-Something': 'value'}


if __name__ == "__main__":
    task_1()
