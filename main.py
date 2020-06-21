import requests as req
from pprint import pprint

def get_my_ip():
    url = "http://ip-api.com/json/"
    JSON = req.get(url).json()

    return JSON

def doubler(n):
    return n * 2


if __name__ == "__main__":
    print(doubler(3))
    print(doubler(5))
    print(doubler(100))

    pprint(get_my_ip())
