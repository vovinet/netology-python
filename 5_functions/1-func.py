import numbers

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_name_by_doc_num(doc_number,delete=False):
    name = None
    for document in documents:
        if document.get('number') == doc_number:
            if delete:
                document.clear
            return document.get('name')

def get_shelf_by_doc_num(doc_number,detele=False):
    shelf = None
    for shelf,docs in directories.items():
        if doc_number in docs:
            if detele:
                docs.remove(doc_number)
            return shelf

def list_documents():
    for document in documents:
        print(f'{document["type"]} \"{document["number"]}\" \"{document["name"]}\"')

def add_document(type, number, name, shelf):
    if directories.get(shelf) == None:
        return 'NoShelf'
    else:
        documents.append({'type': type, 'number': number, 'name': name})
        directories[shelf].append(number)
        return False

def move_document(doc_number,new_shelf):
    if directories.get(shelf) != None:
        if get_shelf_by_doc_num(doc_number,True) != None:
            directories[new_shelf].append(doc_number)
            return False
        else:
            return 'NoDocument'
    else:
        return 'NoShelf'

def add_shelf(shelf):
    if directories.get(shelf) == None:
        directories.update({shelf: []})
    else:
        return True


while True:
    print()
    print('Доступные действия:')
    print('p - показать владельца по номеру документа')
    print('s - показать полку по номеру документа')
    print('l - показать список всех документов')
    print('a - добавить документ')
    print('d - удалить документ')
    print('m - переместить документ')
    print('as - добавить полку')
    print('q - выход из программы')
    command = input('Введите дейтствие: ')
    
    if command == 'p':
        print(get_name_by_doc_num(input('Введите номер документа: ')))

    elif command == 's':
        print(get_shelf_by_doc_num(input('Введите номер документа: ')))

    elif command == 'l':
        list_documents()

    elif command == 'a':
        type = input('Введите тип документа: ')
        number = input('Введите номер документа: ')
        name = input('Введите владельца документа: ')
        shelf = input('Введите номер полки: ')
        
        result = add_document(type, number, name, shelf)

        if not result:
            print('Документ добавлен успешно')
        elif result == 'NoShelf':
            print('Введенной вами полки не существует!')

    elif command == 'd':
        doc_num = input('Введите номер документа: ')
        shelf = get_shelf_by_doc_num(doc_num,True)
        if get_name_by_doc_num(doc_num,True)==None & shelf==None:
            print('Документа с таким номером не существует')

    elif command == 'm':
        doc_num = input('Введите номер документа: ')
        shelf = input('Введите номер полки: ')
        
        result = move_document(doc_num, shelf)

        if not result:
            print('Документ перемещен')
        elif result == 'NoDocument':
            print('Указанный документ не существует')
        elif result == 'NoShelf':
            print('Указанной полки не существует')

    elif command == 'as':
        result = add_shelf(input('Введите номер полки: '))

        if not result:
            print('Полка добавлена успешно')
        else:
            print('Эта полка уже существует!')

    elif command == 'q':
        break
    else:
        print('Данная команда не поддерживается')


    # print(documents)
    # print(directories)