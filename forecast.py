import forecastio
import re
from geopy.geocoders import Nominatim

geolocator = Nominatim()

f = open('api.txt', 'r')

api_key = f.read()

zip = input("Enter your zip: ")
zip = str(zip)

zipCode = re.compile(r"^\d{5}(-\d{4})?$")

if zipCode.match(zip):
    location = geolocator.geocode(zip)

    forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude)

    current_temp = forecast.currently()

    print "Current temp is:",current_temp.temperature
    print "Currently it is:",current_temp.summary
    print "Nearest storm is:",current_temp.nearestStormDistance,"miles."

else:
    print "The zip is not valid."



byDay = forecast.daily()
for dailyData in byDay.data:
   print dailyData.time,dailyData.temperatureMax,dailyData.temperatureMin
