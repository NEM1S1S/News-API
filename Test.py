from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='652c67837d0f4ab3861ba5ba6c2e55c0')

data = newapi.get_everything()

print(data)
