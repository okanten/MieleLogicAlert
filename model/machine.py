import json
import requests


class Machine:
    debug = True
    debug_json = '{"MachineStates":[{"LaundryNumber":9263,"GroupNumber":0,"UnitName":"Machine 1","MachineSymbol":0,"MachineColor":2,"Text1":"Time left: 3 min.","Text2":""},{"LaundryNumber":9263,"GroupNumber":1,"UnitName":"Machine 2","MachineSymbol":1,"MachineColor":1,"Text1":"Idle","Text2":""},{"LaundryNumber":9263,"GroupNumber":0,"UnitName":"Machine 3","MachineSymbol":0,"MachineColor":2,"Text1":"Time left: 12 min.","Text2":""},{"LaundryNumber":9263,"GroupNumber":1,"UnitName":"Machine 4","MachineSymbol":1,"MachineColor":1,"Text1":"Idle","Text2":""},{"LaundryNumber":9263,"GroupNumber":0,"UnitName":"Machine 5","MachineSymbol":0,"MachineColor":2,"Text1":"Time left: 13 min.","Text2":""},{"LaundryNumber":9263,"GroupNumber":1,"UnitName":"Machine 6","MachineSymbol":1,"MachineColor":1,"Text1":"Idle","Text2":""},{"LaundryNumber":9263,"GroupNumber":0,"UnitName":"Machine 7","MachineSymbol":0,"MachineColor":1,"Text1":"Idle","Text2":""},{"LaundryNumber":9263,"GroupNumber":1,"UnitName":"Machine 8","MachineSymbol":1,"MachineColor":1,"Text1":"Idle","Text2":""},{"LaundryNumber":9263,"GroupNumber":2,"UnitName":"Machine 9","MachineSymbol":0,"MachineColor":1,"Text1":"Idle","Text2":""},{"LaundryNumber":9263,"GroupNumber":3,"UnitName":"Machine 10","MachineSymbol":1,"MachineColor":1,"Text1":"Idle","Text2":""}],"ResultText":"","ResultOK":true}'
    url_remmen = 'https://api.mielelogic.com/v3/Country/NO/Laundry/9263/laundrystates?language=en'
    url_bjolstad = 'https://api.mielelogic.com/v3/Country/NO/Laundry/9108/laundrystates?language=en'

    def __init__(self, user):
        self.user = user

    def get_washer_json(self):
        token = self.user.get_token()
        headers = {
            'Authorization': 'Bearer {}'.format(token),
        }
        response = requests.get('https://api.mielelogic.com/v3/Country/NO/Laundry/9263/laundrystates?language=en', headers=headers)

        # response = requests.get('https://api.mielelogic.com/v3/Country/NO/Laundry/9108/laundrystates?language=en', headers=headers)
        return json.loads(response.text)

    def get_machine_time(self, number):
        number = int(number) - 1
        if self.debug is True:
            machine = json.loads(self.debug_json)["MachineStates"][number]
        else:
            machine = self.get_washer_json()["MachineStates"][number]
        # Splitter her for å unngå å tenke på RH valuen til tørketromlene. Fungerer for både vask og trommel.
        values = machine["Text1"].splitlines()
        try:
            n = int(''.join(c for c in values[0] if c.isdigit()))
        except:
            n = False
        return n