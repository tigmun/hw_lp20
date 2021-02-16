#Создайте словарь:{"city": "Москва", "temperature": "20"}
wheather = {'city': 'Moscow',
			'temperature': '20'
			}
#Выведите на экран значение ключа city
print(wheather['city'])

#Уменьшите значение "temperature" на 5
'''
#мой неоптимальный код:
wheather['temperature'] = int(wheather['temperature'])
wheather['temperature'] (-= 5
wheather['temperature'] = str(wheather['temperature'])
'''
#правильный код
wheather['temperature'] = str(int(wheather['temperature']) - 5)

#Выведите на экран весь словарь
print (wheather)

#Проверьте, есть ли в словаре ключ country
'country' in wheather

#Выведите значение по-умолчанию "Россия" для ключа country
print(wheather.get('country', 'Russia'))

#Добавьте в словарь элемент date со значением "27.05.2019"
wheather['date'] = '27.05.2019'

#Выведите на экран длину словаря
print(len(wheather))