import requests, json

url = "https://api.openweathermap.org/data/2.5/forecast?q=jakarta,id&appid=27edaa711aa55803ce95bab5bdaa2129"

response = requests.get(url)

data = response.json()
print(response)

def get_Weather(a):
    weather = None
    population = None
    coord = None

    for el in a["list"]:
        if "weather" in el and el["weather"][0]["description"] == "light rain":
            weather = el["weather"][0]["description"]
            break

    if "city" in a and "population" in a["city"]:
        population = a["city"]["population"]

    if "city" in a and "coord" in a["city"]:
        coord = a["city"]["coord"]

    output = {
        "weather": weather,
        "population": population,
        "coord": coord
    }

    return output

results = get_Weather(data)
results_json = json.dumps(results, indent=2)
print(results_json)

# Invoke-WebRequest -Uri "https://api.openweathermap.org/data/2.5/forecast?q=jakarta,id&appid=27edaa711aa55803ce95bab5bdaa2129"