import requests
from country import CountryAPI
from country import CurrencyAPI


def main():
  country_input = input("Enter a country: ")
  selection_capital = CountryAPI(country_input)
  capital = selection_capital.get()
  selection_currency = CurrencyAPI(country_input)
  currency = selection_currency.get()
  


  
  api_key = 'b0a4f9a26558ef23e0f3b39722f53bb9'
  capital_input = capital

  city_information = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={capital_input}&appid={api_key}")
  temperature = city_information.json()['main']['temp']


  celsius = temperature - 273.15
  fahrenheit = round(celsius * (9/5) +32 )
  new_temp = fahrenheit

  
  print (f"The city {capital_input} is the capital of  {country_input}.It's currency is {currency} and has the temperature of {new_temp}°F" )

main()





