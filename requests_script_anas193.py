import requests
r = requests.head('http://sql-ex.ru/')
print("Код статуса ответа: ", r.status_code)
print("Заголовки ответа: ", r.headers)
print("Ответ: ", r.text)
u = requests.get('http://sql-ex.ru/')
print("Код статуса ответа: ", u.status_code)
print("Заголовки ответа: ", u.headers)
print("Ответ: ", u.text[:100])





