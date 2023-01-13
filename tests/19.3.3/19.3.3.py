import requests
import config
import json

base_url = 'https://petstore.swagger.io/v2'

# GET /user/login  Logs user into the system
username = config.username
password = config.password

res = requests.get(f'{base_url}/user/login?login={username}&password={password}', headers={'accept': 'application/json'})

print('GET /user/login  Logs user into the system')
print(' Статус запроса:', res.status_code)
print(' Ответ сервера body:', res.json())
print(' Ответ сервера header:', res.headers, '\n')


# POST /user  Create user
body = json.dumps(config.created_user)

res = requests.post(f'{base_url}/user', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=body)

print('POST /user  Create user')
print(' Статус запроса:', res.status_code)
print(' Ответ сервера body:', res.json(), '\n')


# PUT /user/{username} Updated user
username = config.created_user['username']
body = json.dumps(config.updated_user)

res = requests.put(f'{base_url}/user/{username}', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=body)

print('PUT /user/{username} Updated user')
print(' Статус запроса:', res.status_code)
print(' Ответ сервера body:', res.json(), '\n')


# GET /user/{username} Get user by user name (before delete)
username = config.updated_user['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print('GET /user/{username} Get user by user name (before delete)')
print(' Статус запроса:', res.status_code)
print(' Ответ сервера body:', res.json(), '\n')


# DELETE /user/{username} Delete user
username = config.updated_user['username']

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print('DELETE /user/{username} Delete user')
print(' Статус запроса:', res.status_code)
print(' Ответ сервера body:', res.json(), '\n')


# GET /user/{username} Get user by user name (after delete)
username = config.updated_user['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print('GET /user/{username} Get user by user name (after delete) expected code 404')
print(' Статус запроса:', res.status_code)
print(' Ответ сервера body:', res.json(), '\n')