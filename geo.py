import geocoder
from geopy.geocoders import Nominatim

# step 1: Get the current location based on IP address
g = geocoder.ip('me')
lat, lon = g.latlng

# step 2: Print the latitude and longitude with seven decimal places
print("Latitude =", format(lat, '.7f'))
print("Longitude =", format(lon, '.7f'))

# step 3: Reverse geocode to get the address
geolocator = Nominatim(user_agent="current_location_app")
location = geolocator.reverse(f"{lat}, {lon}")

# step 4: Print the complete address
print("Address = ", location.address)