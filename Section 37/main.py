import requests
from datetime import datetime

USERNAME = 'username'
TOKEN = 'token_with_at_least_8_characters'
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': "100 days of code",
    'type': 'int',
    'unit': 'Km',
    'color': 'shibafu'
}

header = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
post_endpoint = f'{graph_endpoint}/{graph_config["id"]}'
today= datetime.now()
post_config = {
    'date': today.strftime("%Y%m%d"),
    # 'date': "20220903",
    'quantity': input('Enter an integer: ')
}
# response = requests.post(url=post_endpoint, json=post_config, headers=header)
# print(response.text)
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{today.strftime("%Y%m%d")}'

pixel_data = {
    'quantity': "7"
}
# response = requests.put(url=update_endpoint, json=pixel_data, headers=header)
# print(response.text)
delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{today.strftime("%Y%m%d")}'
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
