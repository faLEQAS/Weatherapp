import pyowm
import requests as rq 
from vars import weatherapikey


def find_location():


    ip = rq.get('https://api.ipify.org').text

    url = "https://ipinfo.io/"+ip+"?token=2ac976cc487b9a"

    r = rq.get(url)

    r_dict = r.json()

    city = r_dict["city"]

    return city;

def get_weather(): 
    city = find_location()

    apikey = weatherapikey 

    owm = pyowm.OWM(apikey) 

    mgr = owm.weather_manager() 

    observation = mgr.weather_at_place(city) 

    w = observation.weather 

    temperature = w.temperature('celsius') 

    temp = str(int(temperature['temp'])) 

    status = w.detailed_status 

    return temp, status

