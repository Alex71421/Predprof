'''открытие файла cars.txt и сбор информации о машинах'''
with open('cars.txt', encoding='utf-8') as file:
    info = file.readline()
    cars = [i.split('$') for i in file.readlines()]

    '''писок машин с серебряным цветом'''
    silver_cars = []

    '''создание результирующего файла'''
    with open('odometer_car.txt', 'w', encoding='utf-8') as res:

        '''сортировка машин по пробегу и запись результирующих параметров
        в файл odometer_car.txt'''
        for car in cars:

            price = car[0].strip()
            year = car[1].strip()
            manufacturer = car[2].strip()
            model = car[3].strip()
            odometer = car[4].strip()
            paint_color = car[5].strip()

            '''если пробег меньше 10000, то записываем в файл'''
            if float(odometer) < 10000:
                res.write(f'{manufacturer} {model}; Цвет: {paint_color}; Пробег: {odometer}; Цена: {price}\n')

                '''если машина серебряная, то добавляем ее в список silver_cars'''
                if paint_color == 'серебро':
                    silver_cars.append(f'{manufacturer} {model} есть машина серебряного цвета. Ее стоимость {price} и пробег: {odometer}')

    '''Вывод машин с цветом серебро и пробегом до 1000'''
    print('\n'.join(silver_cars))
