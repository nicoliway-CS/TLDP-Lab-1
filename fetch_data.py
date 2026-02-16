import requests
#asking user for a fruit name and storing it in a variable
fruit = input("Enter a fruit name: ")
#this is the variable that holds the request line
url = f"https://www.fruityvice.com/api/fruit/{fruit}" 
#this actually makes the request and stores it in the variable response
response = requests.get(url, timeout=5)
#this creates a python dictionary from the json data
fruit_data = response.json()

#try and except block to check if the fruit the user gave is in the API
try:
    #Here I am grabbing certain values from keys from the fruit_data dictionary and storing them in variables
    name = fruit_data['name']
    family = fruit_data['family']
    calories = fruit_data['nutritions']['calories']
except KeyError:
    print("Sorry, that fruit was not found in the API.")
    exit()

#this is my print statement to make a sentence.
print(f"The {name} is part of the {family} family and has {calories} calories.")