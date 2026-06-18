def car_info(name, manufacturer, **car_data):
    car_data['name'] = name
    car_data['manufacturer'] = manufacturer
    return car_data

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)