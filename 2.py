'''открытие файла cars.txt и сбор информации о машинах'''
with open('cars.txt', encoding='utf-8') as file:
    info = file.readline()
    cars = [i.split('$') for i in file.readlines()]

    '''создание списка для отсортировки'''
    sorted_cars = []

    '''пока в списке cars есть элементы, берем минимальный из них
    и закидываем в sorted_cars,  сам этот элемент удаляем из cars'''
    while cars != []:
        car = min(cars, key=lambda x: float(x[0]))
        sorted_cars.append(car)
        cars.remove(car)

    '''Вывод 3 самых дешевыхе машин'''

    print('Вам могут подойти:')

    for i in range(3):

        car = sorted_cars[i]

        price = car[0].strip()
        year = car[1].strip()
        manufacturer = car[2].strip()
        model = car[3].strip()
        odometer = car[4].strip()
        paint_color = car[5].strip()

        print(f'{manufacturer} {model}; Цвет: {paint_color} ; Пробег: {odometer}; Цена: {price}')