
# Application Programing Interface

# features:
# -str parsing
# -input/output
# -module + installing packages
# get data from internet

# aka - whois
# urlib - exist in pyhon

# pip - tool -


name = input("\nEnter a domain/ip: ")


# request info
import requests
url = 'http://ip-api.com/csv/' + name
response = requests.get(url)

# process info
data = response.text.split(",")


# print info
if data[0] == 'success':
    print('\nInfo found!')
    print('reason: ', response.reason)
    print('Location: ', data[1])
    print('ip: ', data[-1])
    print(data)
else:
    print('\nNo info found!')


print('\n\nresponse.status_code: ', response .status_code)
if response.status_code == 200:
    print('Success!')

    print('\n status_code is less than 400: ', response.ok)


    print('\ncontent: ', response.content)
    print('headers: ', response.headers)
    print('headers_Content-Type: ', response.headers['Content-Type'])

    print('\nlinks: ', response.links)
    print('\nurl: ', response.url)

elif response.status_code == 404:
    print('Not Found.')


response.close()




