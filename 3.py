'''открытие файла cars.txt и сбор информации о машинах'''
with open('cars.txt', encoding='utf-8') as file:
    info = file.readline()
    cars = [i.split('$') for i in file.readlines()]

    '''запрашиваем ввод бюджета, если ввод = стоп, заканчиваем программу'''
    budget = input('Введите верхнюю и нижнюю границы бюджета: ')
    while budget!= 'стоп':

        '''определяем границы и создаем список для подходящих машин'''
        min_input, max_input = [int(i) for i in budget.split()]
        found_cars = []

        '''ортируем исходные данные по бюджету'''
        for car in cars:
            if min_input <= float(car[0]) <= max_input:

                price = car[0].strip()
                year = car[1].strip()
                manufacturer = car[2].strip()
                model = car[3].strip()
                odometer = car[4].strip()
                paint_color = car[5].strip()

                found_cars.append(f'{manufacturer} {model} цена {price}, пробег данной машины составляет {odometer}')

        '''если нашлись машины - выводим их, если нет - выводим что ничего не нашлось'''
        if len(found_cars) > 0:
            for n in range(len(found_cars)):
                print(f'{n + 1}. {found_cars[n]}')
        else:
            print('К сожалению, под ваш бюджет ничего не удалось найти')

        '''повторно запрашиваем бюджет'''
        print()
        budget = input('Введите верхнюю и нижнюю границы бюджета: ')