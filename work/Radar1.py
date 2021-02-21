
car_speed = int(input('Introduceti viteza: '))

if car_speed > 0:
    print('Procesare date!')

if car_speed <= 0:
    print('Viteza presupune deplasare!')

if car_speed > 60 and car_speed <= 70:
    print('Depăşirea vitezei de circulaţie stabilită '
          'pe sectorul respectiv de drum de la 10 la 20 km/oră'
          '600-900/3 p.p.')
elif car_speed > 70 and car_speed <= 90:
    print('Depăşirea vitezei de circulaţie stabilită '
          'pe sectorul respectiv de drum de la 20 la 40 km/oră'
          '900-1200/4 p.p.')
elif car_speed > 90:
    print('Depăşirea vitezei de circulaţie stabilită '
          'pe sectorul respectiv de drum mai mult de 40 km/oră'
          '1500-1800/5 p.p.')
else:
    print('Nu ati depasit limita de viteza')

