import requests
from datetime import datetime, timedelta
from pytz import timezone
import pytz

'''
url = " https://test-bild.herokuapp.com/login?email_usuario=test.bild@gmail.com&senha_usuario=1234"
json = requests.get(url).json()
print(json)

import json
import requests
data = {'email_usuario':'teste.bild@gmail.com',
        'senha_usuario':'1234'
        }
data_json = json.dumps(data)
payload = {'json_payload': data_json, 'apikey': 'YOUR_API_KEY_HERE'}
r = requests.get('http://myserver/emoncms2/api/post', data=payload)'''