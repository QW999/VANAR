

# tep_yesterday = -5.0
# temp_today = -3.0
#
#
# if tep_yesterday < temp_today:
#     print("It is getting warmer")
# elif tep_yesterday == temp_today:
#     print("It is the same")
# else:
#     print("It is getting colder")




class Meteo:

    def __init__(self, temp, wind):
        self.temp = temp
        self.wind = wind

    def __lt__(self, other):  #comparatie
        return self.temp < other.temp

    def __eq__(self, other):
        return self.temp == other.temp


m_yesterday = Meteo(-5.0, 25.00)
m_today = Meteo(-3.0, 15.00)

# print(m_yesterday)
# print(m_today)


if m_yesterday < m_today:
    print("It is getting warmer")
elif m_yesterday == m_today:
    print("It is the same")
else:
    print("It is getting colder")



