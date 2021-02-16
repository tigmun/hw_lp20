x = input('insert your name: ')
y = input('insert your second name: ')


def comparison (f_name, s_name):
    if f_name.isalpha() == False or s_name.isalpha() == False:
        print('0')
    elif f_name == s_name:
        print ('1')
    elif len(f_name) > len(s_name):
        print('2')
    elif f_name != s_name and s_name == 'learn':
        print('3')
z = comparison(x,y)
'''
a = ''

while not a.isnumeric():
    if a != '':
        print(f'{a} is not a number')
    a = input("Enter a number: ")
    '''