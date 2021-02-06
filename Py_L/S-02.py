import requests

s = requests.get('https://www.baidu.com/')

print(s.status_code)
print(s.ok)
print(s.headers)
