#Code for 3 asynchronous http requests
import grequests

url_list = [
    "https://webhook.site/5c47eedc-4610-4511-8aa2-0cc257c7fe91",
    'https://webhook.site/b20da944-b613-481d-8f9b-597e43f10d53',
    'https://webhook.site/fdf19e6a-3f0d-43d1-8d74-59515d4c4c29'
]

raw_resp = (grequests.get(u) for u in url_list)
responses = grequests.map(raw_resp) 
for resp in responses:
    print(resp.headers['Date'])