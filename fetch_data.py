import requests
#this is the variable that holds the request line
url = "https://www.fruityvice.com/api/fruit/apple"
#this actually makes the request and stores it in the variable response
response = requests.get(url, timeout=5)
#this creates a python dictionary from the json data
fruit_data = response.json()
#Here I am grabbing certain values from keys from the fruit_data dictionary and storing them in variables
name = fruit_data['name']
family = fruit_data['family']
calories = fruit_data['nutritions']['calories']

#this is my print statement to make a sentence.
print(f"The {name} is part of the {family} family and has {calories} calories.")