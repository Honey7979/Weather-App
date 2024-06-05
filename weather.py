import json
import http.client
import urllib.parse

def fetch_weather_data(city):
    API_KEY = 'e3cb3c930ab6454130e91932140a0679'
    try:
        # URL encode the city name to handle spaces and special characters
        encoded_city = urllib.parse.quote(city)
        
        # Set up the connection
        conn = http.client.HTTPSConnection("api.openweathermap.org")
        
        # Make the request
        conn.request("GET", f"/data/2.5/weather?q={encoded_city}&appid={API_KEY}")
        
        # Get the response
        res = conn.getresponse()
        
        # Check if the response status is OK (200)
        if res.status != 200:
            print(f"Error: Received response status {res.status}")
            return None
        
        # Read and decode the response data
        data = res.read().decode("utf-8")
        
        # Parse the JSON data
        return json.loads(data)
    
    except Exception as e:
        print(f"Error: {e}")
        return None
