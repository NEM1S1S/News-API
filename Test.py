import requests
from newsapi import NewsApiClient


def getData(keywords):
    #Her hentes dataen fra
    newsapi = NewsApiClient(api_key='652c67837d0f4ab3861ba5ba6c2e55c0')

    #Her hentes alt der indeholder søgeordet, er på engelsk og hvor mange artikler skal fremvises på en gang.
    data = newsapi.get_everything(q= keywords ,language='en', page_size=100)

    #Her angives en variable articles som værende data's individuelle artikler.
    articles = data['articles']

    #Her optilles søgningens forskellige titler for de fundne artikler.
    for x, y, z in enumerate(articles):
        print(f'{x+1}    {y["title"]}    {z["author"]}')


    return data

def UI():
    menuInput = ''
    while menuInput != 'exit':
        #Søgefeltet for artiklerne
        keywords = input('Indtast dine søgeord: ')
        #Kald functionen GetData
        theData = getData(keywords)

        #Printer statussen for koden, om det fungerer
        print('Status: ' + theData['status'])

        #Hvor gange ordet er fundet.
        print('Total Results ')
        print(theData['totalResults'])

        #Udprintning af dataen
        print(theData)

        menuInput = input('skriv "exit" for at afslutte, ENTER for at søge igen.')

UI()
#requests commands

#r = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=652c67837d0f4ab3861ba5ba6c2e55c0')

#print(dir(r))
#print(r.content)
