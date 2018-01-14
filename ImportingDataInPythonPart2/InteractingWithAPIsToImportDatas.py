'''
Created on Aug 9, 2017

@author: idolchevic
'''
import json

print("---------------------------------------------------")
print("   Loading and exploring a JSON ")
print("---------------------------------------------------")

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])




print("---------------------------------------------------")
print("   Pop quiz: Exploring your JSON ")
print("---------------------------------------------------")

with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
    

print('title : ', json_data['Title'])
print('year : ', json_data['Year'])


print("---------------------------------------------------")
print("  API requests  ")
print("---------------------------------------------------")

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)



print("---------------------------------------------------")
print("   JSON–from the web to Python ")
print("---------------------------------------------------")

# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])



print("---------------------------------------------------")
print("   Checking out the Wikipedia API ")
print("---------------------------------------------------")

# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

