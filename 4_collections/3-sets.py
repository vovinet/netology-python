# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

from posixpath import split


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    ]

stat = []
queries_qty = len(queries)
queries_length_variants = set()
queries_length_stat = {}

# Получим статистику запросов по длине запроса
for query in queries:
    queue_length = len(query.split())
    stat.append(queue_length)
    queries_length_variants.add(queue_length)

# Получим число запросов по уникальным вариантам длины
for queries_length_variant in queries_length_variants:
    length_count = stat.count(queries_length_variant)
    queries_length_stat[queries_length_variant] = (length_count, length_count/queries_qty)

# Выводим полученную информацию
print('Статистика запросов:')
for q_key,q_stat in queries_length_stat.items():
    print(f'Запросов длиной {q_key} слов: {q_stat[0]} ({q_stat[1]*100:.2f}%)')
