# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is the super class


class Vehicle:
    pass

# Vehicle has 2 subclasse: GroundVehicle and FlightVehicle


class GroundVehicle(Vehicle):
    pass


class FlightVehicle(Vehicle):
    pass

# GroundVehicle has 2 subclasses: Car and Motorcycle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# FlightVehicle has 2 subclasses: Airplane and Starship


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
