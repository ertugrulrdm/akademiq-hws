from math import sqrt as karekok, pi
from inhertitance import Car
import requests

print(karekok(25))
print(pi)

car = Car("Honda")
car.start()

response = requests.get("https://google.com")
print(response.status_code)