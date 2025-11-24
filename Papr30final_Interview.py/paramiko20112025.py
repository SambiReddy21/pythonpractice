"""
requests — Real-Time REST API Automation Example

Use case:
✔ Fetch device inventory
✔ Trigger API-based configurations
✔ Validate network service (ATOM/NSO/NMS/EMS)
"""

import requests

#url = "http://controller.example.com/api/devices"
url = "https://www.meesho.com/?srsltid=AfmBOop8OW4H7drUieC73Y8Fvt0Z_EgcQwtN2O_yjiGlED3qR3UZSI7h"
headers = {"Authorization": "Bearer my_token"}

responses = requests.get(url, headers=headers)

if responses. status_code == 200:
    data = responses.json()
    print("device inventory:")
    for device in data["devices"]:
        print(device["hostname"], device["ip"])
    else:
        print("API error:", responses.status_code)

#########################################################################################
