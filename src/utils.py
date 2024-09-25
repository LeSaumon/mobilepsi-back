from typing import Dict
import requests

def get_free_bikes_data() -> Dict[str, str]:
    response = requests.get("https://gbfs.getapony.com/v1/Angers/en/free_bike_status.json")
    return response.json()