workdone = "a"
power = "b"
kinetic_energy = "c"
potential_energy = "d"
efficency = "e"

print("a=workdone"
      "b=power"
      "c=kinetic_energy"
      "d=potential_energy"
      "e=efficency")
user = input("enter what physics topic to solve: ")
if user == workdone:
    force = int(input("enter force: "))
    distance = int(input("enter distance: "))
    workdone = force * distance
    print(workdone)
elif user == power:
    workdone = int(input("enter workdone: "))
    time = int(input("enter time: "))
    power = workdone / time
    print(power)
elif user == kinetic_energy:
    mass = int(input("enter mass: "))
    velocity = int(input("enter velocity: "))
    kinetic_energy = 0.5 * mass * velocity**2
    print(kinetic_energy)
elif user == potential_energy:
    mass = int(input("enter mass: "))
    height = int(input("enter height: "))
    gravity = int(input("enter gravity: "))
    potential_energy = gravity * height * mass
    print(potential_energy)
elif user == efficency:
    mechanical_advantage = int(input("enter mechanical advantage: "))
    velocity_ratio = int(input("enter velocity ratio: "))
    efficency =mechanical_advantage / velocity_ratio * 100
    print(efficency)
print("thank you for participating")
