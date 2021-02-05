import requests
from newsapi import NewsApiClient

#Her hentes dataen fra
newsapi = NewsApiClient(api_key='652c67837d0f4ab3861ba5ba6c2e55c0')

#Søgefeltet for artiklerne
keyword = input('Indtast et søge ord: ')

#Her hentes alt der indeholder søgeordet, er på engelsk og 20 sider langt.
data = newsapi.get_everything(q= keyword ,language='en', page_size=20)

#Udprintning af dataen
print(data)

#r = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=652c67837d0f4ab3861ba5ba6c2e55c0')

#print(dir(r))
#print(r.content)

    def sort():
        
