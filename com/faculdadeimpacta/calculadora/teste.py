import requests
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from dateutil.parser import parse
data = [
        {
                'dt_agendamento' :"Wed, 11 Nov 2020 20:22:22 GMT"
        },
        {
                'dt_agendamento' :"Wed, 11 Nov 2020 10:10:10 GMT"
        }
        ]
for item in data:
        dt = parse(item['dt_agendamento'])
        final = str(dt.date()) +' '+str(dt.time())
        item['dt_agendamento'] = final
print(data)

'''
data_e_hora = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
fuso_horario = timezone("America/Sao_Paulo")
data_final = data_e_hora.astimezone(fuso_horario)
print(data_final)
lista = {}
lista['a'] = 4
lista['a'] = 7
print(lista['a'])
'''

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