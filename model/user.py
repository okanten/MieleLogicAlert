import json
import requests


class User:
    token = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password,
            'client_id': 'YV1ZAQ7BTE9IT2ZBZXLJ',
            'scope': 'NO'
        }

        r = requests.post('https://sec.mielelogic.com/v3/token', data=data)
        if r.status_code == 200:
            self.token = json.loads(r.text)["access_token"]
            return True
        else:
            return r.text

    def get_token(self):
        return self.token
