'''
#Примеры из лекции
x = 1
while x < 5:
	print(x)
	x += 1


while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print(f'Сам ты {user_say}')
'''

#Задание 1
#Напишите функцию hello_user(), которая с помощью функции
#input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”

while True:
	user_input = input('Как дела? ')
	if user_input == 'Хорошо':
		break
#Задание 2
'''
Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее.
Напишите функцию ask_user() которая с помощью функции input() просит пользователя ввести вопрос, а затем, если вопрос есть в словаре, программа давала ему соотвествующий ответ. Например:
Пользователь: Что делаешь?
Программа: Программирую
'''
