import csv

'''открытие файла cars.txt и сбор информации о машинах'''
with (open('cars.txt', encoding='utf-8') as file):
    info = file.readline()
    cars = [i.split('$') for i in file.readlines()]

    '''создание множества марок и списка с количеством машин по маркам'''
    cars_hash = []
    marks = set(i[2] for i in cars)

    for mark in marks:
        number_of_cars = filter(lambda x: x[2] == mark, cars)
        cars_hash.append([mark, len(list(number_of_cars))])


    """создание хэш-таблицы"""
    with open('hash_table.csv', 'w', newline='', encoding='utf8') as file:
        w = csv.DictWriter(file, fieldnames=['key', 'value'])
        w.writeheader()
        for row in cars_hash:
            w.writerow({'key': row[0], 'value': row[1]})

    '''вывод из таблицы'''
    with open('hash_table.csv', newline='', encoding="UTF-8") as cfile:
        reader = list(csv.DictReader(cfile))
        count = 0
        outmarks = ['buick', 'chrysler', 'volvo', 'infiniti', 'lincoln', 'acura', 'hyundai', 'mercedes-benz', 'audi', 'bmw']
        for mark in outmarks:
            for line in reader:
                if line['key'] == mark:
                    print(f'{line['key']} {line['value']}')
                    break
