from controller.controller import Controller

print("Skriv inn hvilke maskiner du vil få varsel om når de er ferdig, skill med komma")
print("Eksempel: 1,7,4,3")
machines = input("Maskiner: ")
machines = machines.split(",")
for machine in machines:
    machine = int(machine)
print("Hvor mange minutter før vil du varsles? (min: 1)")
interval = int(input("Minutter: "))
controller = Controller(machines, int(interval))
controller.start()
