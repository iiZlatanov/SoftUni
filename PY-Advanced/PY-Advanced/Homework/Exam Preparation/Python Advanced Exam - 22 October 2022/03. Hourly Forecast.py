def forecast(*args):
    sunny_locations = {}
    cloudy_locations = {}
    rainy_locations = {}
    result = ""
    for el in args:
        city = el[0]
        weather = el[1]
        if weather == "Sunny" and (city not in sunny_locations):
            sunny_locations[city] = weather
        elif weather == "Cloudy" and (city not in cloudy_locations):
            cloudy_locations[city] = weather
        elif weather == "Rainy" and (city not in rainy_locations):
            rainy_locations[city] = weather

    for key, value in sorted(sunny_locations.items(), key=lambda x: x[0]):
        result += f"{key} - {value}\n"
    for key, value in sorted(cloudy_locations.items(), key=lambda x: x[0]):
        result += f"{key} - {value}\n"
    for key, value in sorted(rainy_locations.items(), key=lambda x: x[0]):
        result += f"{key} - {value}\n"

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))