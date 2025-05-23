import requests, random
from django.core.cache import cache
COUNTRY_URL="https://countriesnow.space/api/v0.1/countries/capital"

def get_random_country():
    response = requests.get(COUNTRY_URL)
    if response.status_code == 200:
        countries = response.json().get("data", [])
        cache.set("all_countries", countries, timeout=60*60*24)
        random_country = random.choice(countries).get("name", None)
        return random_country

def get_capital(country):
    response = requests.post(COUNTRY_URL, json={"country": country})
    if response.status_code == 200:
        capital = response.json().get("data", {})
        return capital.get("capital", None)
