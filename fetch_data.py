import requests

url = "https://www.fruityvice.com/api/fruit/apple"

response = requests.get(url)

fruit_data = response.json()

name = fruit_data['name']
family = fruit_data['family']
calories = fruit_data['nutritions']['calories']

print(f"The {name} is part of the {family} family and has {calories} calories.")