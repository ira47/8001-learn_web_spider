import requests


def foo1():
    response = requests.get("http://www.baidu.com")
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(len(response.text))
    print(response.cookies)


def foo2():
    response = requests.get("http://httpbin.org/get?name=Tom&age=20")
    print(response.text)


def foo3():
    data = {
        "name": "Tom",
        "age": 20
    }
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.text)


def foo4():
    import json
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print(type(response.json()))
    print(type(json.loads(response.text)))


foo4()
