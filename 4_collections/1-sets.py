# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

match_string = 'Россия'

geo_logs_russia = []

for visit_dict in geo_logs:
    for visit_title, visit in visit_dict.items():
        if match_string in visit:
            geo_logs_russia.append({visit_title : visit})

print(geo_logs_russia)
