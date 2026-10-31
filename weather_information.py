import json
import pandas as pd

data = '''
{
    "cities": [
        {
            "location": {"city": "Kochi", "country": "India"},
            "weather": {"temperature": 30, "humidity": 75}
        },
        {
            "location": {"city": "Chennai", "country": "India"},
            "weather": {"temperature": 34, "humidity": 60}
        },
        {
            "location": {"city": "Delhi", "country": "India"},
            "weather": {"temperature": 28, "humidity": 55}
        }
    ]
}
'''

weather_data = json.loads(data)

records = []

for city in weather_data["cities"]:
    records.append({
        "City": city["location"]["city"],
        "Country": city["location"]["country"],
        "Temperature": city["weather"]["temperature"],
        "Humidity": city["weather"]["humidity"]
    })

df = pd.DataFrame(records)

print("Weather Report")
print(df.to_string(index=False))

print("\nWeather Summary")
print("Average Temperature:", df["Temperature"].mean(), "°C")
print("Average Humidity:", df["Humidity"].mean(), "%")
print("Highest Temperature:", df["Temperature"].max(), "°C")

