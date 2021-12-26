import requests
city_id = 524901 # "Moscow,RU"
appid = "b54b8cab1588458aee0b1880f1038108"


def getWeatherByCityId(cityId: int) -> str:
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': cityId, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("temp_min:", data['main']['temp_min'])
        print("temp_max:", data['main']['temp_max'])

        text = "Погода в городе " + data['name'] + " - " + data['weather'][0]['description']
        text += "\r\nТемпература: " + str(data['main']['temp'])
        text += "\r\nМинимальная температура: " + str(data['main']['temp_min'])
        text += "\r\nМаксимальная температура: " + str(data['main']['temp_max'])

        return text
    except Exception as e:
        print("Ошибка:", e)
        pass