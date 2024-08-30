import requests

BASE_URL = 'http://localhost:3000'

def get_token():
    response = requests.post(f'{BASE_URL}/get-token')
    return response.json().get('token')

def hello(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{BASE_URL}/hello', headers=headers)
    print(response.text)

def send_command(token, command):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(f'{BASE_URL}/drone', json={'command': command}, headers=headers)
    print(response.text)

if __name__ == '__main__':
    token = get_token()
    if token:
        hello(token)
        send_command(token, 'fly')
