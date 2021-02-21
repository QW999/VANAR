
import datetime

while True:

    d_1900_01_01 = datetime.date(1900, 1, 1)
    print('Starting from: ', d_1900_01_01)
    # print(type(d_1900_01_01))

    t_day = datetime.date.today()
    print('Date t_day: ', t_day)
    # print(type(t_day))


    age = 0

    year = int(input('Enter a year: '))
    # if year >= 1900 and year <= t_day.year:
    #     print('Processing...')
    # else:
    #     print('Pls enter correct year!')

    month = int(input('Enter a month: '))
    # if month >= 1 and month <= 12:
    #     print('Processing...')
    # else:
    #     print('Pls enter correct month!')

    day = int(input('Enter a day: '))
    #     print('Processing...')
    # else:
    #     print('Pls enter correct day!')

    birth_date = datetime.date(year, month, day)
    print('Date entered: ',birth_date)
    # print(type(birth_date))

    days_since_birth = (t_day - birth_date)
    print(days_since_birth)
    # print(type(days_since_birth))


    if birth_date >= d_1900_01_01 and birth_date < t_day:
        print('Processing...')
        age = (t_day.year - year)
        print('Your age: ', age)
        print(type(age))
    else:
        print('Pls enter correct birth date!')


    if age >= 1 and age <= 3:
        print('baby')
    if age >= 4 and age <= 9:
        print('kid')
    if age >= 10 and age <= 15:
        print('teen')
    if age >= 16 and age <= 18:
        print('young')
    if age >= 19 and age <= 50:
        print('adult')
    if age >= 50 :
        print('old')
    break