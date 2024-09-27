import requests

# Вихідні дані
token = 'Токен бота'
chat_id = 'ID чату'
message = 'Повідомлення'

url = f'https://api.telegram.org/bot{token}/sendMessage'

data = {
    'chat_id': chat_id,
    'text': message
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('Повідомлення надіслано')
else:
    print(f"Повідомлення не надіслано, помилка {response.status_code}: {response.text}")
