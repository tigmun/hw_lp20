#Создать список из десяти целых чисел.
#Вывести на экран каждое число, увеличенное на 1.
'''
for i in range (10):
    i += 1
    print (i)


#Ввести с клавиатуры строку.
#Вывести эту же строку вертикально: по одному символу на строку консоли.

input_word = str(input('Введите текст: '))
word = input_word
for letter in word:
    print (letter)

'''

#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

students_scores = [{'school_class': '4a',
                    'scores': [3,4,5,2]
                    },
                    {'school_class': '9c',
                    'scores': [2,1,3,2]
                    },
                    {'school_class': '2b',
                    'scores': [3,4,5,2]
                    },
                    {'school_class': '4b',
                    'scores': [3,4,5,2]
                    },
                    {'school_class': '7a',
                    'scores': [3,4,5,2]
                    }
                    ]

for score in students_scores:
    