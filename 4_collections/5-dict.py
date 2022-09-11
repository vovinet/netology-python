# *Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

import re


raw_list = ['2018-01-01', 'yandex', 'cpc', 100]

if len(raw_list) > 2: 
    start = raw_list[-1]
    result = {}
else:
    print('Введите список с 2 и более элементов')
    die()

if start:
    for id,item in enumerate(raw_list[len(raw_list)-2::-1]):
        result[item] = start
        start = dict.copy(result)
        result = {}
        
    print(start)
    
