#https://learn.python.ru/lessons/08_functions.html?full#cover
'''
price = 200
discount = 5

price_with_discount = price * discount / 100

#print(price_with_discount)
'''

def discounted(price, discount):
    price_with_discount =  price - (price * discount / 100)
    print(price_with_discount)

price = 200
discount = 5

discounted(price, discount)

one = input()
two = input()

def get_summ(one, two, delimetr='&'):
    
    get_sum = f'{one}{delimetr}{two}' 
    print (get_sum.upper())

get_summ(one, two)


price = int(12)
def format_price(price):

    return f'Price: {price} usd'

x = format_price(56.24)
print(x)