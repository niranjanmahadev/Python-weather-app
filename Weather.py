import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current_condition"][0]

    print("\n===== WEATHER REPORT =====")
    print(f"City: {city}")
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Feels Like: {current['FeelsLikeC']}°C")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind Speed: {current['windspeedKmph']} km/h")
    print(f"Condition: {current['weatherDesc'][0]['value']}")

except requests.RequestException:
    print("Unable to fetch weather data.")
except (KeyError, IndexError, ValueError):
    print("Unexpected weather data received.")
