while True:
    city_A = 0
    city_B = 10
    city_C = 110
    city_D = 150
    city_E = 200

    volume = float(input('Full fuel supply: '))
    consume = 2.5/100
    remaining_fuel = 0

    distance_1 = city_B - city_A
    consume_1 = distance_1 * consume
    if consume_1 <= volume:
        remaining_fuel = volume - consume_1
        print('Next station city_B: ', distance_1, 'km'
        ' The car will consume: ', consume_1, 'L', 'remaining fuel', remaining_fuel, 'l')
    if remaining_fuel <= 0:
        print('Not enough fuel till city_B!')
        break

    distance_2 = city_C - city_B
    consume_2 = distance_2 * consume
    if consume_2 <= volume:
        remaining_fuel = remaining_fuel - consume_2
        print('Next station city_C: ', distance_2, 'km'
        ' The car will consume: ', consume_2, 'L', 'remaining fuel', remaining_fuel, 'l')
    if remaining_fuel <= 0:
        print('Not enough fuel till city_C!')
        break

    distance_3 = city_D - city_C
    consume_3 = distance_3 * consume
    if consume_3 <= volume:
        remaining_fuel = remaining_fuel - consume_3
        print('Next station city_D: ', distance_3, 'km' 
        ' The car will consume: ', consume_3, 'L', 'remaining fuel', remaining_fuel, 'l')
    if remaining_fuel <= 0:
        print('Not enough fuel till city_D!')
        break

    distance_4 = city_E - city_D
    consume_4 = distance_4 * consume
    if consume_4 <= volume:
        remaining_fuel = remaining_fuel - consume_4
        print('Next station city_E: ', distance_4, 'km'
        ' The car will consume: ', consume_4, 'L', 'remaining fuel', remaining_fuel, 'l')
    if remaining_fuel <= 0:
        print('Not enough fuel till city_E!')
        break