# MieleLogicAlert
Just a small script that interacts with the API that mielelogic.com uses to update its web-interface.

Will alert you when assigned machines are close to being finished.

## Requirements
`requests py-notifier`

See requirements.txt

## Usage
Insert your mielelogic.com credentials in user.txt

NOTE: As of now, this is hardcoded to only check the machines at Remmen Studentboliger.

If you live at Bjolstad change this line in model/machine.py:

`response = requests.get(self.url_remmen, headers=headers)`

to

`response = requests.get(self.url_bjolstad, headers=headers)`
