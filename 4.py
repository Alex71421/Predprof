'''открытие файла cars.txt и сбор информации о машинах'''
with open('cars.txt', encoding='utf-8') as file:
    info = file.readline()
    cars = [i.split('$') for i in file.readlines()]

    '''создаем множество существующих цветов машин'''
    colors = set(i[-1].strip() for i in cars)

    '''словарь вида цвет: список машин такого цвета'''
    cars_by_colors = {}

    '''создаем списки машин по цвету'''
    for color in colors:
        cars_by_colors[color] = list(filter(lambda x: x[-1].strip() == color, cars))

    '''вывод'''
    for color in colors:
        print(f'{len(cars_by_colors[color])} машин цвета {color} есть сегодня в наличии.')