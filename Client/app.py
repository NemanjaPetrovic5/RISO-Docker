import http.client
import json

connection = http.client.HTTPConnection("localhost:5000")
payload = json.dumps(
  {'ime': 'Nemanja',
  'prezime': 'Petrovic',
  'username': 'npetrovic',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'AIOS', 'espb': 8},
     {'ime': 'C# programiranje', 'espb': 8}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}

connection.request("POST", "/users", payload, headers)
response = connection.getresponse()
dataDisplay = response.read()
print(dataDisplay.decode("utf-8"))