
import folium
import phonenumbers
number = input("Enter Phone Number: ")
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(ch_number, "en")
print("Location: ",yourLocation)

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("ISP : ",carrier.name_for_number(service_number, "en"))

Key = "c279c69b67044644b994023f4ed81e63"

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print("Cordinates: ",lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start= 9)

folium.Marker([lat,lng], popup=yourLocation).add_to((myMap))

myMap.save("myLocation.html")