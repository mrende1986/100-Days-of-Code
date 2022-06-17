import requests

SHEETLY_URL = 'https://api.sheety.co/e5a384cfe0fceb8a85b34f908a1fe55b/flightDeals/prices'
SHEETLY_PUT_URL = 'https://api.sheety.co/e5a384cfe0fceb8a85b34f908a1fe55b/flightDeals/prices/'

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination = {}
    
    def get_sheet_data(self):
        response = requests.get(SHEETLY_URL)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEETLY_PUT_URL}/{city['id']}",json=new_data)
            print(response.text)