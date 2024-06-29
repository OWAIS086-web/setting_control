import requests
import json

base_url = 'http://127.0.0.1:5000'

update = {
      "title": "Car Wait Time",
            "type": "value hh",
            "default_value_bool": 500
}
response = requests.post(f'{base_url}/settings/page1/car_wait_time', json=update)
