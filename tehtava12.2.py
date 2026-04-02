import requests
import json
sijainti=input("Minkä paikkakunnan sään haluat tietää?")
sijainti=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={sijainti}&limit=5&appid=928a0cc6d83129325fce1d479c0505e1")
print(json.dumps(indent=2))