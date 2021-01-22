import requests

r = requests.get('https://newsapi.org/')

#print(dir(r))
print(r.text)
