import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

# Get location name from user
location_name = input("Enter your location name: ")

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapi")

# Get coordinates
location = geolocator.geocode(location_name)

if location:
    # Get latitude and longitude
    lat = location.latitude
    lon = location.longitude 

    # Create a map centered on the user's location
    my_map = folium.Map(location=[lat, lon], zoom_start=12) 

    # Add a marker
    marker = folium.Marker([lat, lon], popup=location_name)
    marker.add_to(my_map)

    # Display the map
    display(HTML(my_map._repr_html_()))
    # display(my_map)

else:
    print("😞 Location not found! Please choose another.")
