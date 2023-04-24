import requests

phone_number = #Your number "123-456-7890"
url = f"https://maps.googleapis.com/maps/api/geocode/json?components=phonenumber:{phone_number}&key=YOUR_API_KEY"

response = requests.get(url)
data = response.json()

if data['status'] == 'OK':
    location = data['results'][0]['formatted_address']
    print(f"The location of {phone_number} is {location}")
else:
    print(f"Unable to find the location of {phone_number}")
