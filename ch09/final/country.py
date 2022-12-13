import requests

class CountryAPI:
    def __init__(self,country):
      self.url = "https://api.apilayer.com/geo/country/name/"+country
      self.payload = {}
      self.headers= {"apikey": "XXrJdluTDzedhgm8pyi813IXihYryC7U"}
    def get(self):
      response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
      capital = response.json()[0]['capital']
      return capital

  


class CurrencyAPI:
   def __init__(self,country):
      self.url = "https://api.apilayer.com/geo/country/name/"+country
      self.payload = {}
      self.headers= {"apikey": "XXrJdluTDzedhgm8pyi813IXihYryC7U"}
   def get(self):
      response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
      currency = response.json()[0]['currencies'][0]
      return currency

