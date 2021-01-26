import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=652c67837d0f4ab3861ba5ba6c2e55c0')
r = requests.get(url)
print (r.json())
