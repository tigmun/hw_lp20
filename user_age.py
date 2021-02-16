#age = int(input('insert your age: '))
def user_age(age):
    if age   <= 7:
        return ('Пользователь ходит в детский сад')
    elif age > 8 and  age <= 17:
        return('Пользователь учится в школе')
    elif age > 18 and  age <= 23:
        return ('Пользователь учится в университете')
    else:
        return ('Пользователь работает')

#user = user_age

x = user_age(abs(int(input('Введите возраст: '))))


print (x)