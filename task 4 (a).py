import requests

# Вихідні дані
token = 'Токен бота'
chat_id = 'ID чату'

url = f'https://api.telegram.org/bot{token}/getChatAdministrators'

parametrs = {
    'chat_id': chat_id
}

response = requests.get(url, params=parametrs)

if response.status_code == 200:
    users = response.json()['result']
    for user in users:
        print(f"User: {user['user']['first_name']}")
else:
    print(f"Отримати користувачів не вдалося, помилка {response.status_code}: {response.text}")
