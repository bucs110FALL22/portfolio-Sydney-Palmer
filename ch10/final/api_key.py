import requests
country = input("Enter a country: ")
url = "https://api.apilayer.com/geo/country/name/"+country

payload = {}
headers= {
  "apikey": "XXrJdluTDzedhgm8pyi813IXihYryC7U"
}

response = requests.request("GET", url, headers=headers, data = payload)


result = response.text
capital = response.json()[0]['capital']
print(result)
#print(f"The capital of {country} is {capital}")






api_key = 'b0a4f9a26558ef23e0f3b39722f53bb9'
city_input = input("Enter the capital: ")



city_information = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}")
temperature = city_information.json()['main']['temp']

#print (city_information.json())

celsius = temperature - 273.15
fahrenheit = round(celsius * (9/5) +32 )
new_temp = fahrenheit


print (f"The capital {city_input} is in the country {country} and has a temperature of {new_temp}°F" )
