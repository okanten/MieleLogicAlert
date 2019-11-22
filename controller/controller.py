from model.user import User
from model.machine import Machine
from pynotifier import Notification
import threading


class Controller:
    user = None
    message = "Maskin {} er ferdig om {} minutter"

    def __init__(self, machines, interval):
        self.machines = machines
        self.interval = int(interval)

    def read_info_from_file(self):
        with open('user.txt') as f:
            user_info = f.read().splitlines()
            self.user = User(user_info[0], user_info[1])

    def validate_credentials(self):
        self.read_info_from_file()
        return self.user is not None and self.user.login()

    def check_machines(self):
        for machine in self.machines:
            m = Machine(self.user)
            if m.get_machine_time(machine) is False:
                print("Maskin {} er ikke i bruk".format(machine))
                return False
        return True

    def start(self):

        if self.validate_credentials() and self.check_machines():
            self.update_machine_status()
        else:
            exit(1)

    def update_machine_status(self):
        if self.validate_credentials():
            threading.Timer((self.interval * 60), self.update_machine_status).start()
            times_left = []
            notifications = []
            for machine in self.machines:
                m = Machine(self.user)
                times_left.append(m.get_machine_time(machine))
            for i, time_left in enumerate(times_left):
                try:
                    if time_left <= self.interval:
                        notifications.append(self.message.format(i, time_left))
                except TypeError:
                    pass
            for notification in notifications:
                self.send_notification(notification)
        else:
            print("Feil brukernavn og passord")
            exit(2)

    def send_notification(self, notification):
        Notification(
            title='MieleLogic',
            description=notification,
            duration=60,  # Duration in seconds
            urgency=Notification.URGENCY_CRITICAL
        ).send()
