a = 'Мир'
b = 'Привет'

print(a +  ' ' + b + '!')

a = 'Мир'
b = 'Привет'
c = '{} {}!'.format(a, b)

print(c)

a = 'Мир'
b = 'Привет'
c = 2

'''
d = a + ' ' + b + c + '!'

print(d)
'''

d = '{} {}{}'.format(a, b, c)

print(d)


user = 'Миша'

b = f'Привет {user}'

print(b)


a = 'Hello'
b = 'World'

c = f'{a}{b}'

print(len(c))


a = 'Hello'.upper()
print(a)

b = 'World'.lower()
print(b)

c = 'python'.capitalize()
print(c)

a = None

b = '0'
print(a is None)
print(b is None)

a = 2
print(type(a))
b = '2'
print(type(b))

c = 2.0
print(type(c))

'''
name = input ('Insert your name: ')
print(f'Hello, {name}')
'''
'''
age = int(input('How old you? '))
birth_year = 2017 - age
print(f'You in {birth_year} year.')
'''


product = {
	'name': 'IPhone Xs',
	'stock': 24,
	'price': 65555
}

product['memory'] = 64

product.get('discount', 0)

print(product)