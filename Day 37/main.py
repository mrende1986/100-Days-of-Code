import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'mrende'
TOKEN = 'birdsofafeatherhieahreah'

parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}

# response = requests.post(pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()
today = today.strftime("%Y%m%d")

todays_ride = {
    'date': today,
    'quantity': '22.5',
}

# response = requests.post(url=post_endpoint, json= todays_ride, headers=headers)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

new_pixel_data = {
    'quantity': "15.2"
}

# response = requests.put(url=update_endpoint, json= new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)