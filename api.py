import requests

city = input("Enter the city:")

api_key = <API KEY>
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)

status = requests.get(url).status_code

json_data = requests.get(url).json()

if status == 200:
    temp1 = json_data['main']['temp']
    whether1 = json_data['weather'][0]['main']

    print("The temperature of city {} is:{} and weather: {}".format(city, temp1, whether1))

else:
    print("City not found or something went wrong.")

