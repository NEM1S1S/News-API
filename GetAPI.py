import requests
from newsapi import NewsApiClient

#Her hentes dataen fra
newsapi = NewsApiClient(api_key='652c67837d0f4ab3861ba5ba6c2e55c0')

#Søgefeltet for artiklerne
keyword = input('Indtast et søgeord: ')

#Her hentes alt der indeholder søgeordet, er på engelsk og 20 sider langt.
data = newsapi.get_everything(q= keyword ,language='en', page_size=20)

#Printer statussen for koden, om det fungerer
print('Status: ' + data['status'])

#Hvor gange ordet er fundet.
print('Total Results ')
print(data['totalResults'])

type(data['articles'])

print(data['articles'][0])

#Udprintning af dataen
print(data)



#requests commands

#r = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=652c67837d0f4ab3861ba5ba6c2e55c0')

#print(dir(r))
#print(r.content)

def sort(data):
    for data[0] in range(len(data)):
    #laver en løkke der tjekker index
        mini = data[0]
        #kalder mindsteværdien som i
        for data[1] in range(data[0]+1, len(data)):
        #laver en løkke der tjekker elementerne i listen
            if data[1] < items[mini]:
            #tjekker om værdien er mindre end mindsteværdien
                mini = data[1]
                #sætter mindsteværdien til den værdi i
                #tilfælde af at den er mindre
        data[0], data[mini] = data[mini], data[0]
        #mindsteværdien bytter plads med første værdi i den usorterede række
    return data
