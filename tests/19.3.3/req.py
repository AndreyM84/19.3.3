import requests

# Вариант 1

# res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

# Вариант из видео

status = 'available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
# res = requests.get(f'{base_url}/user/login?login={username}&password={password}',
#                    headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
