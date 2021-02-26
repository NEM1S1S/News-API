import requests
from newsapi import NewsApiClient


def getData(keywords):
    #Her hentes dataen fra
    newsapi = NewsApiClient(api_key='652c67837d0f4ab3861ba5ba6c2e55c0')

    #Her hentes alt der indeholder søgeordet, er på engelsk og 20 sider langt.
    data = newsapi.get_everything(q= keywords ,language='en', page_size=20)

    return data

menuInput = ''
while menuInput != 'exit':
    #Søgefeltet for artiklerne
    keywords = input('Indtast et søgeord: ')
    #Kald functionen GetData
    theData = getData(keywords)

    #Printer statussen for koden, om det fungerer
    print('Status: ' + theData['status'])

    #Hvor gange ordet er fundet.
    print('Total Results ')
    print(theData['totalResults'])

    type(theData['articles'])

    #Udprintning af dataen
    print(theData)

    menuInput = input('skriv "exit" for at afslutte, ENTER for at søge igen.')

#requests commands

#r = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=652c67837d0f4ab3861ba5ba6c2e55c0')

#print(dir(r))
#print(r.content)
