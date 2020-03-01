import requests

# ret = requests.get('https://github.com/timeline.json')

# payload = {'key1': 'value1', 'key2': 'value2'}
# ret = requests.get("http://httpbin.org/get", params=payload)

payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.post("http://httpbin.org/post", data=payload)

print ret.url
print ret.text
