import requests
url_list = [
    "https://webhook.site/5c47eedc-4610-4511-8aa2-0cc257c7fe91",
    'https://webhook.site/b20da944-b613-481d-8f9b-597e43f10d53',
    'https://webhook.site/fdf19e6a-3f0d-43d1-8d74-59515d4c4c29'
]

for url in url_list:
    response = requests.get(url)
    print(response.headers['Date'])
    #webpage = urllib.request.urlopen(url)
    #print(webpage.info())
