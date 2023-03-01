import requests
import json
import creds

def getWeather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={creds.api_key}"
    response = requests.get(url)
    if response.json()['cod'] == '404':
        print('No City Found')
    else:
        if response.status_code == 200:
            data = json.loads(response.text)

            # Parse the weather data
            try:
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
            except KeyError as e:
                print(f"KeyError: {e}. JSON response may be missing expected keys.")
            
            # Display the weather data
            print(f"Temperature: {temp} F")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} mph")
        elif response.status_code == 401:
            print("Error: 401 Unauthorized. Invalid API key.")
        else:
            print(f"Error: {response.status_code}. Failed to retrieve weather data.")

def main():
    city = input("Enter a city: ")
    getWeather(city)


main()